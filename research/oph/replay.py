"""Independent arithmetic checks against a pinned OPH checkout.

Only standard-library code runs. OPH JSON files are read, not imported.
"""
import argparse
import gzip
import hashlib
import itertools
import json
import subprocess
import tarfile
from decimal import Decimal as D, getcontext
from fractions import Fraction as F
from pathlib import Path

REV = "3edcfa2af4387d6bda5634f0bf65f253f7faef65"
CODATA = D("137.035999177")
REFERENCE_U = D("0.000000021")
getcontext().prec = 60


def require(condition, message):
    if not condition:
        raise ValueError(message)


def alpha(root):
    data = root / "code/P_derivation/runtime"
    rows = json.loads((data / "selection_accounting.json").read_text())["historical_outputs"]
    for row in rows[:2]:
        lo, hi = (D(row["alpha_inv_enclosure"][k]) for k in ("lo", "hi"))
        require(lo < hi < CODATA - REFERENCE_U, "interval comparison failed")
        print(f'{row["id"]}: {1_000_000 * ((lo+hi)/2/CODATA-1):.6f} ppm')
    j = json.loads((data / "empirical_thomson_endpoint_current.json").read_text())
    i = j["inputs"]
    a = D(i["source_anchor_inv_alpha_MZ"]) + D(i["lepton_transport_delta_inv_alpha"])
    d, u = D("0.027609"), D("0.000112")
    center, lo, hi = (a/(1-x) for x in (d, d-u, d+u))
    expected = [j["endpoint"]["alpha_inv_central"], *j["endpoint"]["alpha_inv_interval"]]
    require(all(abs(x-D(y)) < D("1e-55") for x,y in zip((center,lo,hi), expected)),
            "empirical endpoint mismatch")
    required = 1-a/CODATA
    require(hi < CODATA-REFERENCE_U and required > d+u, "empirical comparison failed")
    print(f"fixed anchor + hadrons: {center:.10f} [{lo:.10f}, {hi:.10f}]")
    print(f"required hadronic input: {required:.12f} vs {d} ± {u}")
    spectral = D("137.035999189566")  # point printed in upstream public-data audit
    print(f"spectral candidate: {(spectral-CODATA)/REFERENCE_U:+.4f} reference u only")


def invert(rows):
    n = len(rows)
    a = [list(row) + [F(i == j) for j in range(n)] for i,row in enumerate(rows)]
    for j in range(n):
        p = next(i for i in range(j,n) if a[i][j])
        a[p],a[j] = a[j],a[p]
        divider = a[j][j]
        a[j] = [x/divider for x in a[j]]
        for i in range(n):
            if i != j:
                coeff = a[i][j]
                a[i] = [x-coeff*y for x,y in zip(a[i],a[j])]
    require(all(a[i][j] == (i == j) for i in range(n) for j in range(n)),
            "inverse reduction failed")
    return [row[n:] for row in a]


def matvec(a,x):
    return [sum(i*j for i,j in zip(row,x)) for row in a]


def frame():
    # Geometric design from the paper, not its decoder implementation.
    pairs = list(itertools.combinations(range(3),2))
    points = [[F(1),0,0,0]]
    for axis, sign in itertools.product(range(3),(1,-1)):
        points.append([F(5,3)] + [F(4*sign,3) if i == axis else 0 for i in range(3)])
    points.extend([[F(3)] + [2 if i in p else 0 for i in range(3)] for p in pairs])
    require(all(u[0]>0 and u[0]**2-sum(z*z for z in u[1:]) == 1 for u in points),
            "not unit future-timelike")
    ix = list(itertools.combinations_with_replacement(range(4),2))
    a = [[F(u[i]*u[j]*(1+(i!=j))) for i,j in ix] for u in points]
    b = invert(a)
    norms = [sum(map(abs,row)) for row in b]
    m = max(norms)
    require(m == F(17,8), "incorrect operator norm")
    sharpness_input = [1 if x >= 0 else -1 for x in b[norms.index(m)]]
    require(max(map(abs, matvec(b,sharpness_input))) == m, "sharpness not attained")
    for k in range(10):
        witness = [row[k] for row in b]
        require(any(witness) and matvec(a,witness) == [int(i==k) for i in range(10)],
                "missing-probe countermodel failed")
    # A common additive error is indistinguishable from a metric term.
    eta = [F((-1 if i == 0 else 1) if i == j else 0) for i,j in ix]
    require(matvec(b,[F(1)]*10) == [-x for x in eta], "metric-mode control failed")
    print("ten-observer tensor decoder: exact rank 10/10, sharp max-coordinate norm 17/8")
    print("missing-probe null witnesses: 10/10; common unit offset decodes to -g")


def validate_projection(archive, sample):
    expected_sha = "8f2801a69663ef1142bb05660e0118ef7b1e0bdf3d05afba434a0569023b98ab"
    with archive.open("rb") as source:
        require(hashlib.file_digest(source, "sha256").hexdigest() == expected_sha,
                "unexpected official ACT archive SHA256")
    chains = {chain["member"]: chain["rows"] for chain in sample["chains"]}
    seen = set()
    with tarfile.open(archive, "r|gz") as bundle:
        for member in bundle:
            if member.name not in chains:
                continue
            require(member.isfile() and member.name not in seen, "invalid raw chain")
            seen.add(member.name)
            with bundle.extractfile(member) as stream:
                headers = stream.readline().decode("ascii").lstrip("#").split()
                wi, ni = headers.index("weight"), headers.index("ns")
                actual = ((tokens[wi], tokens[ni])
                          for line in stream
                          if (tokens := line.decode("ascii").split())
                          and not tokens[0].startswith("#"))
                for row, saved in itertools.zip_longest(actual, chains[member.name]):
                    require(saved is not None and row == tuple(saved),
                            f"raw chain token disagreement: {member.name}")
    require(seen == chains.keys(), "missing raw chains")
    print("all projected weight/ns tokens cross-checked against four official ACT chains")


def tilt(root, archive):
    path = root / "code/cosmology/tilt_posterior/act_dr6_ns_weight.json.gz"
    print("upstream chain projection SHA256:", hashlib.sha256(path.read_bytes()).hexdigest())
    with gzip.open(path,"rt") as stream:
        sample = json.load(stream)
    require(len(sample["chains"]) == 4 and D(sample["burn_in_fraction"]) == D("0.5"),
            "unexpected chain contract")
    if archive is not None:
        validate_projection(archive, sample)
    phi = (1 + D(5).sqrt())/2
    pi = D("3.14159265358979323846264338327950288419716939937510582097494")
    def prediction(a_inv):
        return 1-(phi+pi.sqrt()/a_inv)/48
    thresholds = [prediction(a) for a in (CODATA, D("136.9948351774129373"),
                                          D("137.0356601369465766"))]
    total_rows = total_weight = 0
    tails = [0]*len(thresholds)
    per_chain = []
    for chain in sample["chains"]:
        rows = chain["rows"]
        retained = rows[len(rows)//2:]
        total_rows += len(retained)
        wsum = 0
        counts = [0]*len(thresholds)
        for weight, ns in retained:
            weight, ns = int(weight), D(ns)
            wsum += weight
            for i,t in enumerate(thresholds):
                if ns <= t:
                    counts[i] += weight
        total_weight += wsum
        per_chain.append((counts[0], wsum))
        tails = [x+y for x,y in zip(tails,counts)]
    require((total_rows,total_weight,tails[0]) == (379175,508985,3114),
            "posterior reduction disagrees with the pinned reported result")
    for i,t in enumerate(thresholds):
        print(f"n_s={t:.16f}: {tails[i]}/{total_weight} = {100*D(tails[i])/total_weight:.9f}%")
    print("per-chain percentages:", ", ".join(f"{100*D(n)/w:.5f}%" for n,w in per_chain))


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("upstream", type=Path, help="checkout of OPH at the pinned revision")
    p.add_argument("--act-archive", type=Path, help="optional official ACT tar.gz")
    args = p.parse_args()
    root = args.upstream.resolve()
    revision = subprocess.check_output(["git","-C",str(root),"rev-parse","HEAD"],text=True).strip()
    require(revision == REV, f"expected OPH revision {REV}, got {revision}")
    changed = subprocess.check_output(["git","-C",str(root),"status","--porcelain","--",
        "code/P_derivation/runtime", "code/cosmology/tilt_posterior"],text=True).strip()
    require(not changed, "upstream evidence files are modified")
    alpha(root)
    frame()
    tilt(root, args.act_archive)

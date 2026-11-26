# OPH-006 — Physical photon dispersion (FZ-12 seam-edge symbol)

- Unit: OPH-006
- Claim under test: "Does the finite seam-edge symbol describe the actual photon sector in the same frame and units?"
- Pinned revision: FloatingPragma/observer-patch-holography @ 3edcfa2af4387d6bda5634f0bf65f253f7faef65, `docs/FROZEN_PREDICTION_LADDER.md#fz-12`
- Verdict: **INCONCLUSIVE** for the physical photon claim. The finite mathematics of the symbol is **independently confirmed**; the bridge to the actual photon sector (scale, frame, same-operator link, eligible observation) is not supplied at the pinned commit, so no comparison can confirm or refute it.

## Assumptions

Written before computing (in a local pre-registration note, reproduced here in substance). No changes to the plan were made after computation began.

- A1. The support is the 30 signed unit directions w_j of the icosahedron edge differences (15 axes, two signs each).
- A2. Lambda_a(k,n) = (1/(5a^2)) sum_j [1 - cos(a k w_j.n)] is a spatial kinetic eigenvalue, not automatically omega^2 (stated in the pinned receipt).
- A3. I6 is the A5-invariant rank-6 harmonic normalized to I6 = 1 on the 12 vertex ("port") directions.
- A4. "Photon sector in the same frame and units" means: omega^2 = Lambda_a for both transverse polarizations, in a declared frame with a boost map, with a physical value of a in eV^-1 (or metres).
- A5. External comparison basis (Pierre Auger, JCAP 01 (2022) 023, arXiv:2112.06773): E^2 = p^2 + delta_gamma,n E^(2+n), photon-only LIV, Lorentz-invariant e+/e-, CMB rest frame. Published bound delta_gamma,2 > -1e-58 eV^-2, only in the alternative scenario with a subdominant proton component.

## Falsifier

- Mathematics refuted if: the moments S2 = sum (w.n)^2 != 10, S4 != 6 (isotropic), S6 != 30/7 - (2/7) I6, any rank-2 or rank-4 anisotropy appears, or the series coefficients differ from (C4, B0, B6) = (-a^2/20, a^4/840, -a^4/12600).
- The physical claim is confirmed only if the pinned sources supply all of: (i) a source-derived physical scale with a_min > 0 in comparison units, (ii) a declared frame and boost map, (iii) a same-operator proof that photon omega^2 equals Lambda_a on both polarizations, (iv) an eligible post-freeze observation.
- The physical claim is refuted only if (i)-(iii) hold and an eligible observation excludes the linked manifold for every a >= a_min at >= 5 sigma (FZ12-R04).
- If any of (i)-(iv) is missing, the result is INCONCLUSIVE. A null with no positive scale floor cannot exclude the branch.

## Method

1. Built the icosahedron exactly in Q(sqrt5) with sympy. Extracted the 30 edges and the 30 signed unit edge directions, and checked they coincide with the signed edge-midpoint (2-fold) axes.
2. Computed the exact polynomials S2, S4, S6 in n = (x,y,z). Checked isotropy and that S6 - (30/7) r^6 is harmonic, so it is pure rank 6. Normalized I6 at a vertex and checked I6 = 1 on all 12 vertices.
3. Expanded Lambda_a with sympy to O(k^6) and read off C4, B0, B6, the scale-free ratios and the Auger-basis delta_4,iso = d - 2c^2.
4. Contrast with FZ-11 (12 vertex directions, weight 1/(2a^2)): recomputed its C4, B0, B6.
5. Remainder check at 50-digit precision (mpmath) on 300 random directions with ak in {1e-3, 1e-2, 1e-1}: |exact - series| / (ak)^8 must stay below the analytic ceiling sum(c^8)/(5*8!) <= 10/201600.
6. Under the *unproven* identification omega^2 := Lambda_a, derived the radial group velocity and compared it with the pinned `fz12_observation_map_receipt.json`.
7. Units: converted the Auger bound to a bound on a (CODATA 2022 hbar*c, l_P). Estimated a time-of-flight delay for a = l_P. Showed that any null bound leaves a nonempty admissible interval for a when there is no floor.
8. Audited the pinned receipts for the status of the physical bridges. The receipts were read as data only; their SHA-256 values match the pins in the Auger receipt.
   - `seam_current_edge_prediction_receipt.json`: sha256 0b8f0f75…2915
   - `fz12_observation_map_receipt.json`: sha256 0b34218b…1d17

## Results

Mathematics: confirmed (exact):

| Quantity | Pinned claim | Independent result |
|---|---|---|
| edges / signed directions | 30 / 30 | 30 / 30; directions = ±edge-midpoint axes |
| S2, S4 | 10, 6 | 10 r^2, 6 r^4 (exact) |
| S6 | 30/7 - (2/7) I6 | 30/7 r^6 + H6, Laplacian(H6) = 0, H6(port) = -2/7 |
| k^2 coefficient | 1 | 1 |
| C4, B0, B6 | -a^2/20, a^4/840, -a^4/12600 | same |
| B0/C4^2, B6/C4^2, B6/B0 | 10/21, -2/63, -1/15 | same |
| delta_4,iso (Auger basis) | -2a^4/525 | -2a^4/525 |
| FZ-11 contrast | C4 = -a^2/20, B6/C4^2 = 32/315 | same; S6(ports) = 12/7 + (64/175) I6 |
| remainder / (ak)^8 | O(k^8) | max 1.80e-5 ≤ ceiling 4.96e-5 |
| formal radial v_g | 1 - 3a^2k^2/40 + a^4(19/13440 - I6/5040)k^4 | same |
| I6 range on S^2 | — | [-0.556, 1.000] |

No rank-2 or rank-4 anisotropy was found, and the rank-6 sign is opposite to FZ-11, as stated.

Physical photon identification: not established at the pinned commit:

| Requirement | Status in pinned sources |
|---|---|
| (i) physical scale a and source-derived a_min > 0 | OPEN (gates "finite physical carrier scale", "source-derived positive physical scale lower bound", owner #664) |
| (ii) frame / boost map | OPEN (`preferred_frame_or_boost_map = false`; gate "frame, boost, readout, nuisance, and exclusivity contract") |
| (iii) same-operator photon link | OPEN (`spatial_symbol_to_frequency_squared_proved = false`, `time_evolution_proved = false`; "physical scalar or polarization-independent sector" gate open; a photon reading needs identical action on both transverse polarizations, and the symbol is scalar) |
| (iv) eligible observation | none (`comparison_permitted = false`, `comparison_state = INELIGIBLE_UNARMED_PHYSICAL_PRODUCER_OPEN`) |

Units / exposure (diagnostic only, retrospective):
- Auger delta_gamma,2 > -1e-58 eV^-2 with delta_gamma,2 = C4 = -a^2/20 gives a < sqrt(20)·1e-29 eV^-1 = 4.472e-29 eV^-1 = 0.5460 l_P = 8.825e-36 m. This matches the repo's diagnostic receipt.
- At a = l_P: C4 = -3.354e-58 eV^-2. The ladder's "-5.47e-58" corresponds to a^2 = 1.631 l_P^2; its "natural scale a = sqrt(P) l_P" is a hypothesis and is not derived in the FZ-12 source.
- Time-of-flight sensitivity at a = l_P (E = 13 TeV, D ≈ 650 Mpc, non-cosmological approximation): Δt ≈ 5.7e-15 s, which is undetectable. Only threshold-type (scenario-dependent) probes reach this scale.
- For a null bound |C4| < X, the admissible interval is a ∈ (0, sqrt(20X)). It is nonempty for any X (checked for 1e-58, 1e-70 and 1e-100 eV^-2), so without a_min > 0 a null excludes nothing.

Negative / corrected attempts (recorded):
- The first symbolic midpoint-axis comparison returned False. This came from set deduplication of unsimplified surds, not from the geometry. A numeric check (tol 1e-12) then gave True.
- The first float64 remainder test gave ratios ~1.8 and then ~343. The cause was cancellation in 1-cos, then a unit vector that was not renormalized at 50 digits. After fixing both, the result is 1.80e-5, within the analytic ceiling.

## Limitations

- I did not re-check the Lean proofs, the D6 seam-current image, or the claim that the 30-seam incidence current *is* this edge orbit. I took A1 as the geometric input.
- I did not try to derive the vector/gauge (two-polarization) version of the symbol. Whether a lattice Maxwell operator on this support splits polarizations is open and decides (iii).
- I did not re-simulate the Auger bound. It is scenario-dependent (no bound without protons above 1e19 eV), states no confidence level for this case, and predates the FZ-12 freeze, so it is ineligible.
- The time-of-flight estimate uses a flat-space approximation and one representative energy and distance. It is an order-of-magnitude estimate only.
- The constants carry CODATA 2022 nominal values without uncertainty propagation.

## Reproduce

```
python3 -m venv .venv && .venv/bin/pip install sympy==1.14.0 numpy==2.5.5
R=https://raw.githubusercontent.com/FloatingPragma/observer-patch-holography/3edcfa2af4387d6bda5634f0bf65f253f7faef65
curl -sSfo ladder.md $R/docs/FROZEN_PREDICTION_LADDER.md
curl -sSfo edge.json $R/code/a5_fingerprint/runtime/seam_current_edge_prediction_receipt.json   # sha256 0b8f0f75...2915
curl -sSfo obsmap.json $R/code/a5_fingerprint/runtime/fz12_observation_map_receipt.json          # sha256 0b34218b...1d17
curl -sSfo auger.json $R/code/a5_fingerprint/runtime/fz12_auger_threshold_diagnostic_receipt.json
# save the script below as check_oph006.py, then:
.venv/bin/python check_oph006.py      # sha256 6c487ab7807e83f6dc74eadb3cb883873b4291b840a0589083b602b50f620cf7; ~3 s; prints every number above
```

Expected output: every line of the Results tables above; runtime ~3 s.

### check_oph006.py (inlined so this report is self-contained)

```python
"""Independent local check for Warp Commons unit OPH-006 (FZ-12 seam-edge symbol)."""
import itertools, math
import numpy as np
import sympy as sp

phi = (1 + sp.sqrt(5)) / 2
# Icosahedron vertices: cyclic permutations of (0, +-1, +-phi)
V = []
for s1, s2 in itertools.product([1, -1], repeat=2):
    base = (0, s1, s2 * phi)
    for r in range(3):
        V.append(tuple(sp.nsimplify(base[(i - r) % 3]) for i in range(3)))
assert len(V) == 12
d2 = lambda u, v: sp.simplify(sum((ui - vi) ** 2 for ui, vi in zip(u, v)))
edges = [(i, j) for i in range(12) for j in range(i + 1, 12) if d2(V[i], V[j]) == 4]
print("edges:", len(edges), "(expect 30); seam difference norm^2 = 4")
# signed edge directions (unit), deduplicated
dirs = []
for i, j in edges:
    for s in (1, -1):
        w = tuple(sp.simplify(s * (V[i][k] - V[j][k]) / 2) for k in range(3))
        if w not in dirs:
            dirs.append(w)
print("distinct signed unit edge directions:", len(dirs), "(expect 30; 60 directed labels -> 2 per direction)")
assert len(dirs) == 30
Vn = np.array([[float(c) for c in v] for v in V])
Wn = np.array([[float(c) for c in w] for w in dirs])
Mn = np.array([Vn[i] + Vn[j] for i, j in edges]); Mn /= np.linalg.norm(Mn, axis=1)[:, None]; Mn = np.vstack([Mn, -Mn])
print("signed edge directions == signed edge-midpoint axes (numeric, tol 1e-12):",
      all(np.min(np.linalg.norm(Mn - w, axis=1)) < 1e-12 for w in Wn) and all(np.min(np.linalg.norm(Wn - m, axis=1)) < 1e-12 for m in Mn))

x, y, z = sp.symbols("x y z", real=True)
r2 = x**2 + y**2 + z**2
S = {p: sp.expand(sum((w[0]*x + w[1]*y + w[2]*z) ** p for w in dirs)) for p in (2, 4, 6)}
print("S2 - 10 r^2 =", sp.simplify(S[2] - 10*r2))
print("S4 - 6 r^4  =", sp.simplify(S[4] - 6*r2**2))
H6 = sp.expand(S[6] - sp.Rational(30, 7) * r2**3)
lap = lambda f: sp.diff(f, x, 2) + sp.diff(f, y, 2) + sp.diff(f, z, 2)
print("Laplacian(S6 - 30/7 r^6) == 0 (pure rank 6):", sp.simplify(lap(H6)) == 0)
vhat = [c / sp.sqrt(1 + phi**2) for c in V[0]]
h6_vertex = sp.nsimplify(sp.simplify(H6.subs({x: vhat[0], y: vhat[1], z: vhat[2]})))
print("H6 at port direction =", h6_vertex, "(expect -2/7, i.e. coefficient of I6 is -2/7 with I6(port)=1)")
I6 = sp.expand(H6 / h6_vertex)
# all 12 vertices give I6 = 1
print("I6 = 1 on all 12 ports:", all(sp.simplify(I6.subs({x: v[0]/sp.sqrt(1+phi**2), y: v[1]/sp.sqrt(1+phi**2), z: v[2]/sp.sqrt(1+phi**2)}) - 1) == 0 for v in V))

# Series of Lambda_a along a direction n: sum_j [1-cos(a k c_j)] with c_j = w_j.n
a, k = sp.symbols("a k", positive=True)
c = sp.Symbol("c")
term = sp.series(1 - sp.cos(a*k*c), k, 0, 8).removeO()
# replace c^p by moment S_p (linear in moments)
coeff = sp.Poly(sp.expand(term), c)
Lam = 0
for (p,), cf in coeff.terms():
    Lam += cf * sp.Symbol(f"S{p}")
Lam = sp.expand(Lam / (5*a**2))
I6s = sp.Symbol("I6")
Lam = Lam.subs({"S2": 10, "S4": 6, "S6": sp.Rational(30, 7) - sp.Rational(2, 7)*I6s})
C2 = Lam.coeff(k, 2); C4 = Lam.coeff(k, 4); K6 = sp.expand(Lam.coeff(k, 6))
B0 = K6.subs(I6s, 0); B6 = K6.coeff(I6s)
print("Edge (FZ-12): k^2 coeff =", C2, "| C4 =", C4, "| B0 =", B0, "| B6 =", B6)
print("  B0/C4^2 =", sp.simplify(B0/C4**2), " B6/C4^2 =", sp.simplify(B6/C4**2), " B6/B0 =", sp.simplify(B6/B0))
print("  Auger-basis delta4_iso = d - 2c^2 =", sp.simplify(B0 - 2*C4**2))

# FZ-11 contrast: 12 port unit directions, weight 1/(2a^2)
P = {p: sp.expand(sum(((v[0]*x+v[1]*y+v[2]*z)/sp.sqrt(1+phi**2))**p for v in V)) for p in (2, 4, 6)}
# fit P6 = alpha r^6 + beta I6 using two sample directions
al, be = sp.symbols("al be")
pts = [(0, 0, 1), tuple(vhat)]
eqs = [sp.Eq(sp.nsimplify(sp.simplify(P[6].subs(dict(zip((x,y,z), p))))), al + be*sp.nsimplify(sp.simplify(I6.subs(dict(zip((x,y,z), p)))))) for p in pts]
sol = sp.solve(eqs, [al, be])
print("Ports: S2 =", sp.simplify(P[2].subs({x:0,y:0,z:1})), " S4 =", sp.simplify(P[4].subs({x:0,y:0,z:1})), " S6 = %s + (%s) I6" % (sol[al], sol[be]))
print("  check S6 - fit == 0 identically:", sp.simplify(P[6] - sol[al]*r2**3 - sol[be]*I6) == 0)
pC4 = -sp.Rational(1, 2)*P[4].subs({x:0,y:0,z:1})/24
pB0 = sp.Rational(1, 2)*sol[al]/720; pB6 = sp.Rational(1, 2)*sol[be]/720
print("Vertex (FZ-11): C4/a^2 =", sp.simplify(pC4), " B0/a^4 =", sp.simplify(pB0), " B6/a^4 =", sp.simplify(pB6), " B6/C4^2 =", sp.simplify(pB6/pC4**2))

# Numerical: exact symbol vs truncated series at 50-digit precision, random directions
import mpmath as mp
mp.mp.dps = 50
rng = np.random.default_rng(6)
I6f = sp.lambdify((x, y, z), I6, "numpy")
I6m = sp.lambdify((x, y, z), I6, "mpmath")
Wm = [[mp.mpf(str(sp.N(c, 60))) for c in w] for w in dirs]
worst = 0
for _ in range(300):
    n = rng.normal(size=3); n /= np.linalg.norm(n); nm = [mp.mpf(float(t)) for t in n]; nrm = mp.sqrt(sum(t*t for t in nm)); nm = [t/nrm for t in nm]
    for ak in (mp.mpf("1e-3"), mp.mpf("1e-2"), mp.mpf("1e-1")):
        exact = sum(1 - mp.cos(ak*(w[0]*nm[0]+w[1]*nm[1]+w[2]*nm[2])) for w in Wm)/5
        ser = ak**2 - ak**4/20 + ak**6/840 - ak**6/12600*I6m(*nm)
        worst = max(worst, abs(exact-ser)/ak**8)
print("max |exact - series| / (ak)^8 over 900 samples (50 digits) = %.3e; analytic ceiling sum c^8/(5*8!) <= 10/201600 = %.3e" % (float(worst), 10/201600))
I6vals = np.array([I6f(*(v/np.linalg.norm(v))) for v in rng.normal(size=(20000,3))])
print("I6 range on sphere: [%.4f, %.4f]" % (I6vals.min(), I6vals.max()))

# Units: Auger-conditional bound and photon time-of-flight scale
hbarc = 1.973269804e-7  # eV m (CODATA 2022)
lP = 1.616255e-35       # m
lP_eV = lP/hbarc
a_max = math.sqrt(20e-58)
print("Auger(-1e-58 eV^-2) => a < %.4e eV^-1 = %.4f l_P = %.4e m" % (a_max, a_max/lP_eV, a_max*hbarc))
print("delta_gamma2 at a = l_P: %.3e eV^-2" % (-(lP_eV**2)/20))
print("ratio 5.47e-58 / (l_P^2/20) = implied P = %.4f (repo's 'natural scale a = sqrt(P) l_P')" % (5.47e-58/(lP_eV**2/20)))
# GRB 221009A-like TOF delay for a = l_P (non-cosmological approx, D ~ 650 Mpc, E = 13 TeV)
D = 650*3.0857e22; E = 13e12
dt = 1.5*(lP_eV**2/20)*E**2*D/2.998e8
print("TOF delay at a=l_P, E=13 TeV, D=650 Mpc: %.2e s (undetectable)" % dt)
# Null without a floor: any bound |C4|<X leaves (0, sqrt(20X)) admissible
for X in (1e-58, 1e-70, 1e-100):
    print("bound |C4| < %.0e eV^-2 -> admissible a in (0, %.3e) eV^-1: nonempty, branch not excluded" % (X, math.sqrt(20*X)))

# Formal group velocity IF omega^2 := Lambda (the unproven photon identification), radial direction
q = sp.Symbol("q", positive=True)
om = sp.sqrt(q**2 + C4*q**4 + K6*q**6)
vg = sp.expand(sp.series(sp.diff(om, q), q, 0, 6).removeO())
print("formal d omega/dk =", sp.collect(vg, q), "(repo map receipt: 1 - 3a^2/40 k^2 + a^4(19/13440 - I6/5040) k^4)")
```

## Assistance

Prepared with an AI agent (Grok Bot) running locally on behalf of the contributor; all calculations were run locally with sympy/numpy/mpmath. The contributor reviewed the report before publication. Pinned repository files and the Auger paper were used as data only.


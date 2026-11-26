# OPH-007 — Same-source gravity (matched regional Einstein limit)

- Unit: OPH-007
- Claim under test: "Does one native refinement provide proper regions, entropy, area and conserved stress together?"
- Desk test: "Trace each input to actual source records, test o(r^4) residuals or identify the first missing premise."
- Pinned revision: FloatingPragma/observer-patch-holography @ 3edcfa2af4387d6bda5634f0bf65f253f7faef65, `code/matched_einstein_limit/PROOF.md`
- Verdict: **INCONCLUSIVE, leaning negative.** The conditional mathematics (small-ball expansion, ten-observer decoder, 17/8 bound, residual constant 255/(32π)) is **independently confirmed exactly**. No single native refinement at the pinned commit supplies all four inputs together. The **first missing premise is G1**: there is no common Lorentzian metric with proper-volume geodesic balls on the native source. The only native family with refinement data (the protected `collar_scaling` balls, 80 → 327 680 cells) has a stationarity residual that scales as **Θ(ℓ⁴), not o(ℓ⁴)**. Its log–log slope is 4.00 (global tag) and 3.90 (ancestor tag), and residual/(2πℓ⁴) does not decrease. So the o(r^4) estimate fails on the one family where it can be measured.

## Assumptions

Written before any computation in a local pre-registration note (`oph-007/PRE-REGISTRATION.md`, 2026-11-26 13:19 CET). Only the directory README had been read at that point. The plan did not change after computation began.

- A1. "Native refinement" means one Interval Echo / OPH state family, with the same admitted state, refinement index and proper-time normalization, from which **all four** readouts come. Four separate toy preparations do not count.
- A2. The Einstein implication is conditional on G1–G6 (README table) plus o(ℓ⁴) small-ball errors and a positive limit coefficient η*. I check the conditional theorem (tensor algebra, 17/8, eq. (5)) separately as mathematics. It is not evidence for the physical inputs.
- A3. An "actual source record" is a committed data/receipt file at the pinned commit whose numbers come from the same state. Prose, and finite rational profiles flagged "without source or continuum identification", do not count.
- A4. An o(r⁴) test needs at least 3 radii on one refinement tower. o(r⁴) is supported if the log–log slope of |residual| vs r is clearly above 4 (pre-set margin 4.2) and residual/r⁴ decreases. It is refuted for that family if the slope is ≤ 4 within errors and the normalized residual has a positive lower bound.
- A5. Sources are data only. I did not execute any repository code. All numbers below come from my own script, run offline.

## Falsifier

- **Confirm** the claim only if, for one state/refinement, committed records supply all of (i) proper regions (geodesic balls with proper radius in a stated metric), (ii) regional generalized entropy, (iii) actual ball area, (iv) a conserved symmetric stress tensor (∇·T = 0 in that frame), **and** their residuals against the small-ball expansion are o(r⁴) on at least 3 radii.
- **Refute** the claim if all four are recorded on the same state and the residuals are O(r⁴) or larger, or η is non-positive or depends on the refinement. Also refute it if the repo's own records show that two of the four come from different preparations while being presented as one.
- Otherwise the result is **INCONCLUSIVE**, and I report the first missing premise in the order G1 → G6.
- The math sub-claim is refuted if an independent rational recomputation gives a singular 10×10 design, an optimal amplification ≠ 17/8, or small-ball coefficients different from A = 4πℓ² − (2π/15)R⁽³⁾ℓ⁴ and C_ℓ = 4πℓ⁴/15.

## Method

1. **Geometry.** Re-derived with sympy (in a constant-curvature model, which fixes the universal leading coefficients): A(r) = 4πr²[1 − R⁽³⁾r²/18], V(r) = (4π/3)r³[1 − R⁽³⁾r²/30], the fixed-volume radius shift, the fixed-volume area coefficient, and the diamond-kernel integral C_ℓ. Checked that the area contrast equals −C_ℓ·G_uu when R⁽³⁾ = 2G_uu.
2. **Decoder.** Built the ten probes u0, ui±, uij exactly. Checked that they are unit, timelike and future-directed. Built the 10×10 map from the symmetric tensor to R(u,u), inverted it exactly, and took the maximum absolute row sum of the inverse (the sup-norm amplification). Evaluated the sharpness witness (r0 = −1, r1± = 1). Checked that deleting any probe drops the rank to 9, and that (17/8)·15/(4π) = 255/(32π).
3. **Source trace.** Read PROOF.md, README.md, `results.json` and the linked experiment READMEs as data. For each of G1–G6 I recorded whether a committed same-state record exists (table in Results).
4. **o(r⁴) test.** The only native family with a refinement tower of radii is `model/experiments/interval_echo_einstein_station/collar_scaling/signed_area.json` (4 boards: 80, 1280, 20 480 and 327 680 cells). For both tag preparations I fitted the log–log slope of the charge ΔK (the signed stationarity residual per unit κ; the area contrast there is exactly zero) against the relative routed radius ℓ. I also computed the pairwise slopes and ΔK/(2πℓ⁴) with its 99% lower bound.
5. **Hashes of the inputs read** (SHA-256, pinned commit):
   - `code/matched_einstein_limit/PROOF.md` 4ebf858e…4334
   - `code/matched_einstein_limit/README.md` 21fc2ea3…ba6
   - `code/matched_einstein_limit/results.json` 0498bf36…a7e
   - `collar_scaling/signed_area.json` b465431d…0b170
   - `collar_scaling/README.md` d374a1c7…c979

## Results

### Mathematics: confirmed exactly

| Quantity | Claimed | Recomputed |
| --- | --- | --- |
| A(r) r⁴ coefficient / (4πR⁽³⁾) | −1/18 | −1/18 |
| V(r) r⁵ coefficient / ((4π/3)R⁽³⁾) | −1/30 | −1/30 |
| radius shift at fixed volume | R⁽³⁾ℓ³/90 | 1/90 |
| fixed-volume area ℓ⁴ coefficient | −2πR⁽³⁾/15 | −2π/15 |
| diamond kernel C_ℓ | 4πℓ⁴/15 | 4πℓ⁴/15 |
| area contrast = −C_ℓ G_uu | yes | yes |
| 10 probes unit, timelike, future | yes | yes |
| det of the decoder design | ≠ 0 | 1073741824000/531441 |
| optimal sup-norm amplification | 17/8 | 17/8 |
| sharpness witness R11 | 17/8 | 17/8 |
| every probe necessary | yes | yes (rank 9 after any deletion) |
| constant in eq. (5) | 255/(32π) | (17/8)(15/4π) = 255/(32π) ✓ |

### Trace of the inputs to same-source records (pinned commit)

| Input | Same-source record? | Evidence (repo's own statement / receipt) |
| --- | --- | --- |
| G1 common Lorentzian metric + proper-volume balls | **No, first missing premise** | "Their common physical event positions, proper-clock scales and overlap maps on a curved refinement require independent records" (PROOF §Which implication has a proof?). The interface section says "The finite reciprocal source has no common spatial refinement or regional edge-area law meeting this interface." In `collar_scaling` the radius is the *relative routed* radius, not a proper radius. |
| G2 modular generator = stress (diamond normalization) | No | Angular energy identity only in a protected sector; "has no established transfer" (README G2). |
| G3 conserved symmetric stress | Partial | Exact scalar energy continuity on 960 ports (port_ward), but "a covariant stress tensor still requires spatial momentum and an identification… with the proper geometric ones." |
| G4 fixed-volume stationarity | Partial, contradicted | A unique maximum exists on the four-station survey, but there is a certified entropy-increasing change invisible to all 12 mean ranges, and a counter-preparation has slope > 7.47 nats. |
| G5 small-ball errors o(ℓ⁴) | **Fails on the tested family** | See the o(r⁴) test below. PROOF: "For the protected full balls the proposed source and area have a strictly positive normalized residual under uniform midpoint refinement." |
| G6 one positive coupling | No | The 80-cell tests "exclude even a fitted common rescaling". |
| Overall receipt | No | `results.json` scope: `regional_source_premises_instantiated=false`, `Einstein_dynamics_derived_from_executable_source=false`, `physical_gate_accepted=false`, status `CONDITIONAL_MATCHED_REGIONAL_LIMIT`. |

### o(r⁴) test on the protected collar_scaling refinement tower

| cells | ℓ (routed) | global ΔK/(2πℓ⁴) | 99% lower | ancestor ΔK/(2πℓ⁴) | 99% lower |
| --- | --- | --- | --- | --- | --- |
| 80 | 0.19355 | 0.0011862 | 0.0011852 | 0.00011861 | 0.00011828 |
| 1 280 | 0.09449 | 0.0013786 | 0.0013739 | 0.00024188 | 0.00023991 |
| 20 480 | 0.04697 | 0.0013923 | 0.0013732 | 0.00027210 | 0.00026364 |
| 327 680 | 0.02345 | 0.0013739 | 0.0012977 | 0.00027957 | 0.00024518 |

| Fit of log ΔK vs log ℓ | global tag | ancestor tag |
| --- | --- | --- |
| slope, all 4 boards | 3.936 | 3.616 |
| slope, 3 finest | 4.002 | 3.896 |
| pairwise slopes | 3.79, 3.99, 4.02 | 3.01, 3.83, 3.96 |
| o(r⁴) supported (pre-registered: slope > 4.2 and ratio decreasing) | **no** | **no** |

The normalized residual is flat (global) or rising (ancestor) under refinement, and its 99% lower bound stays positive on every board. This matches the repo's own all-level bound: residual/(κℓ⁴) ≥ cα²/(4π) (global) or cα²/(80π) (ancestor), with c = 0.0033051 nats and α = 1/460800. So the stationarity error is Θ(ℓ⁴). Divided by ℓ⁴ it does not tend to zero, and interface item 4 fails for this family. The area contrast there is exactly zero by construction (the range tape has the same law in both arms), so the failure is not a measurement-noise effect.

**Answer to the claim:** at the pinned commit, no single native refinement provides proper regions, entropy, area and conserved stress together. The strict refutation clause (all four recorded on one state, with residual ≥ ℓ⁴) cannot be triggered because the four are not recorded together. The verdict is therefore INCONCLUSIVE, with G1 as the first missing premise and a documented negative o(r⁴) result on the only refinable native family.

## Limitations

- I did not run the repository's Python receipts or the Lean proofs (sources used as data only). The Lean check of `QuantitativeSmallBall.lean` is not re-verified. My algebra re-derives the same statements independently.
- The geometric expansion was checked in a constant-curvature model. That fixes the universal leading coefficients (−1/18, −1/30) but does not test the general o(r²) remainder.
- The o(r⁴) test uses routed, not proper, radii (the repo states this too). A uniformly bounded routed → proper conversion would preserve a positive lower bound, but a family with a different proper geometry could still behave differently. It would have to be supplied as a new record.
- The positive-negative trace table summarizes the repo's own statements at the pinned commit. I did not re-simulate the 80-cell experiments (G2–G4, G6).
- The homogeneous Bianchi I Einstein–scalar reconstruction (README) uses a *prescribed* semiclassical Hamiltonian. It is not a native refinement, so it does not count for the claim.
- Attempts that gave no usable result: no native family other than `collar_scaling` has radii at ≥ 3 refinement levels with all four readouts, so no second o(r⁴) fit was possible.

## Reproduce

```sh
git clone https://github.com/FloatingPragma/observer-patch-holography.git oph
git -C oph checkout 3edcfa2af4387d6bda5634f0bf65f253f7faef65
pip install sympy numpy
# save the script below as check_oph007.py, then:
python check_oph007.py oph/model/experiments/interval_echo_einstein_station/collar_scaling/signed_area.json
```

Runs offline in about 1 s and prints every number in the Results tables as JSON.

### check_oph007.py (inlined so this report is self-contained)

```python
"""OPH-007 independent local checks (Grok Bot). Offline; reads pinned OPH clone as data only.
Usage: python check_oph007.py [path-to-signed_area.json]
"""
import json, sys, math
import sympy as sp
import numpy as np

out = {}
# ---- 1. Small-ball geometry (Gauss/normal-coordinate expansion), independent re-derivation
r, l, R3 = sp.symbols('r ell R3', positive=True)
# 3D geodesic ball in a space with scalar curvature R3 at centre (constant-curvature model, exact in r to needed order):
# constant sectional K = R3/6: area = 4pi (sin(sqrt K r)/sqrt K)^2, volume = int area dr
K = R3/6
A = 4*sp.pi*(sp.sin(sp.sqrt(K)*r)/sp.sqrt(K))**2
V = sp.integrate(sp.series(A, r, 0, 8).removeO(), (r, 0, r))
A_s = sp.series(A, r, 0, 6).removeO()
V_s = sp.series(V, r, 0, 7).removeO()
out['A_coeff_r4_over_4pi_r2_R3'] = sp.simplify(sp.expand(A_s).coeff(r, 4)/(4*sp.pi*R3))   # expect -1/18
out['V_coeff_r5_over_4pi3_r3_R3'] = sp.simplify(sp.expand(V_s).coeff(r, 5)/(sp.Rational(4,3)*sp.pi*R3))  # expect -1/30
# fixed volume 4pi l^3/3: r = l + c l^3
c = sp.symbols('c')
eqV = sp.series(V_s.subs(r, l + c*l**3) - sp.Rational(4,3)*sp.pi*l**3, l, 0, 6).removeO()
csol = sp.solve(sp.expand(eqV).coeff(l, 5), c)[0]
out['r_shift_coeff'] = sp.simplify(csol/R3)   # expect 1/90
Afix = sp.series(A_s.subs(r, l + csol*l**3), l, 0, 6).removeO()
out['fixed_volume_area_l4_coeff'] = sp.simplify(sp.expand(Afix).coeff(l, 4)/R3)  # expect -2pi/15
C_ell = sp.integrate(4*sp.pi*r**2*(l**2 - r**2)/(2*l), (r, 0, l))
out['diamond_kernel_C_ell'] = sp.simplify(C_ell)   # expect 4 pi l^4 /15
# with R3 = 2 G_uu : area contrast = -2pi/15 * 2 G l^4 = -C_ell G
out['area_contrast_equals_minus_Cell_G'] = sp.simplify(out['fixed_volume_area_l4_coeff']*2*l**4 + C_ell) == 0

# ---- 2. Ten-observer decoder: exact inverse, 17/8 bound and sharpness
e = sp.eye(4)
probes = [e[:,0]]
for i in (1,2,3):
    probes += [sp.Rational(5,3)*e[:,0] + sp.Rational(4,3)*e[:,i], sp.Rational(5,3)*e[:,0] - sp.Rational(4,3)*e[:,i]]
for i in (1,2,3):
    for j in range(i+1,4):
        probes.append(3*e[:,0] + 2*e[:,i] + 2*e[:,j])
eta = sp.diag(-1,1,1,1)
out['all_unit_timelike_future'] = all((p.T*eta*p)[0] == -1 and p[0] > 0 for p in probes)
comps = [(a,b) for a in range(4) for b in range(a,4)]
M = sp.Matrix([[ (p[a]*p[b]*(1 if a==b else 2)) for (a,b) in comps] for p in probes])
out['decoder_det'] = M.det()
Minv = M.inv()
rowsums = [sum(abs(x) for x in Minv.row(k)) for k in range(10)]
out['max_abs_row_sum_(amplification)'] = max(rowsums)   # expect 17/8
# sharpness witness: r0=-1, r1+=r1-=1
order = ['0','1+','1-','2+','2-','3+','3-','12','13','23']
rv = sp.zeros(10,1); rv[0] = -1; rv[1] = 1; rv[2] = 1
T = Minv*rv
out['witness_R11'] = T[comps.index((1,1))]   # expect 17/8
out['residual_constant_255_over_32pi'] = sp.simplify(sp.Rational(17,8)*sp.Rational(15,4)/sp.pi - sp.Rational(255,32)/sp.pi) == 0
# removing any probe -> singular (9 rows rank 9 < 10)
out['each_probe_necessary'] = all(M[[k for k in range(10) if k != m], :].rank() == 9 for m in range(10))

# ---- 3. o(r^4) test on the only same-source native family with refinement data (collar_scaling)
path = sys.argv[1] if len(sys.argv) > 1 else 'src/oph/model/experiments/interval_echo_einstein_station/collar_scaling/signed_area.json'
d = json.load(open(path))
fits = {}
for tag in ('global_tag', 'ancestor_tag'):
    ell = np.array([b['relative_routed_radius'] for b in d['boards']])
    q = np.array([b[tag]['charge'] for b in d['boards']])
    lo = np.array([b[tag]['charge'] - b[tag]['simultaneous_radius'] for b in d['boards']])
    ratio = q/(2*math.pi*ell**4)
    slope_all, _ = np.polyfit(np.log(ell), np.log(q), 1)
    slope_fine, _ = np.polyfit(np.log(ell[1:]), np.log(q[1:]), 1)
    pairwise = [float(np.log(q[k+1]/q[k])/np.log(ell[k+1]/ell[k])) for k in range(len(q)-1)]
    fits[tag] = dict(cells=[b['cells'] for b in d['boards']], ell=ell.tolist(),
                     residual_over_2pi_ell4=ratio.tolist(),
                     lower_over_2pi_ell4=(lo/(2*math.pi*ell**4)).tolist(),
                     loglog_slope_all=float(slope_all), loglog_slope_3_finest=float(slope_fine),
                     pairwise_slopes=pairwise,
                     o_r4_supported=bool(slope_fine > 4.2 and ratio[-1] < ratio[0]))
out['collar_scaling_fits'] = fits

def conv(x):
    if isinstance(x, dict): return {k: conv(v) for k, v in x.items()}
    if isinstance(x, list): return [conv(v) for v in x]
    if isinstance(x, (bool, int, float, str)) or x is None: return x
    return str(x)
print(json.dumps(conv(out), indent=1))
```

## Assistance

Prepared with Grok Bot, an AI agent run locally. It wrote the pre-registration, the script and the draft. The contributor (lakosboss) reviewed the report and the code before publishing.


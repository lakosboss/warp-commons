# Independent review of Observer Patch Holography — first pass

Warp Commons review of Bernhard Mueller and contributors' OPH, pinned to [3edcfa2](https://github.com/FloatingPragma/observer-patch-holography/tree/3edcfa2af4387d6bda5634f0bf65f253f7faef65), reviewed 2026-11-25 UTC. This is an external review, not an OPH contribution or endorsement. We ran independent replays and did not run upstream solvers, certificates or Lean. We link upstream sources rather than republishing their data, text or figures.

**Rule before calculation.** Fix the version, premises, comparison object, and decision rule. A formula can be exact under its premises while its physical mapping remains open. A passed reproduction is not a passed experiment. Do not move the target to another branch after looking at the result.

## 01. Fine-structure constant from the observer law

**Claim under test:** a preselected, source-derived map gives the observed low-energy inverse fine-structure constant. First criterion: does the declared numerical endpoint agree with the low-energy reference under the specified map and stated uncertainties? Stronger criterion: is the map selected independently of the target and the low-energy quantity shown to be the Thomson-limit observable? Failure of the first criterion rejects that exact endpoint identification as stated; failing the second withholds any source-only prediction, even for a close number.

- [OPH root enclosures](https://github.com/FloatingPragma/observer-patch-holography/blob/3edcfa2af4387d6bda5634f0bf65f253f7faef65/code/P_derivation/runtime/selection_accounting.json) versus [CODATA 2022](https://physics.nist.gov/cgi-bin/cuu/Value?alphinv): base map 136.994835177413 (−300.388218 ppm); adding gauge-width term 137.035660136947 (−2.474095 ppm). Both published numerical enclosures are disjoint from the CODATA reference interval. We checked the comparison, not the fixed-point enclosure derivation. No model-error likelihood was supplied; this is not a significance estimate for OPH.
- We recalculated the [declared empirical substitution](https://github.com/FloatingPragma/observer-patch-holography/blob/3edcfa2af4387d6bda5634f0bf65f253f7faef65/code/P_derivation/runtime/empirical_thomson_endpoint_current.json) as `(anchor + lepton term)/(1 − hadronic shift)`. Keeping the first two terms fixed, [KNT19](https://doi.org/10.1103/PhysRevD.101.014029)'s 0.027609 ± 0.000112 gives 136.3827548175, interval [136.3670480603, 136.3984651934] from that input uncertainty alone. Hitting CODATA would require 0.032244343558 under this convention. This is a mismatch for this fixed branch, not a direct test of every transport scheme.
- The [public-data audit](https://github.com/FloatingPragma/observer-patch-holography/blob/3edcfa2af4387d6bda5634f0bf65f253f7faef65/docs/research/PUBLIC_DATA_PREDICTION_AUDIT.md) lists a separate spectral candidate, 137.035999189566, only +0.60 reference standard uncertainties away. That is a genuine numerical proximity; we verified the difference, not a source derivation. The repository's [endpoint contract](https://github.com/FloatingPragma/observer-patch-holography/blob/3edcfa2af4387d6bda5634f0bf65f253f7faef65/code/P_derivation/THOMSON_TRANSPORT_THEOREMS.md) leaves the physical bridge open. Picking whichever branch is closest is not a test.

**Verdict:** two declared root values and the fixed empirical substitution miss; the close candidate is not a demonstrated source-only prediction. The next decisive step is a bounded same-scheme hadronic current calculation tied to one source law, with model/branch choice and error budget fixed independently of the measured endpoint.

## 02. Does observer consensus recover Einstein gravity?

**Claim under test:** the [matched regional construction](https://github.com/FloatingPragma/observer-patch-holography/blob/3edcfa2af4387d6bda5634f0bf65f253f7faef65/code/matched_einstein_limit/PROOF.md) separates a finite tensor-identity step from a physical refinement limit. A singular ten-probe design or larger amplification under the same max-coordinate norm would break the finite step.

We built the design for symmetric covariant tensors from the paper's future-unit timelike vectors and inverted it by independent rational elimination. Rank **10/10**. Sharp amplification of max-coordinate readout error: **17/8**, attained by a signed unit error vector. Removing any probe leaves a nonzero tensor invisible to all other nine. Moreover, in signature `(-+++)`, a common unit additive bias decodes to `-g`: uncalibrated common offsets can masquerade algebraically as a metric term. This control is not an objection to the theorem with correctly matched observations; it is a reason to audit calibration and reference subtraction separately.

**Verdict:** finite algebra reproduced. No inference that the source law produces the common metric, proper radii, generalized entropy and conserved stress on a single family, with errors `o(r⁴)`. A first variation or finite fit alone cannot establish the nonlinear equation. This is neither an antigravity result nor a propulsion proposal. The upstream [falsification program](https://github.com/FloatingPragma/observer-patch-holography/blob/3edcfa2af4387d6bda5634f0bf65f253f7faef65/docs/OPH_FALSIFICATION_PROGRAM.md) excludes its antigravity continuation from mature falsifiers at this revision.

## 03. Do the predicted primordial fluctuations match CMB data?

**Claim under test:** for the edge-center branch, `n_s = 1 − P/48` at pivot 0.05 Mpc⁻¹, given the declared primordial generator, translation to curvature perturbations and normal CMB transfer. The published FZ-15 branch fixes `P` using measured alpha. We re-evaluate a historical diagnostic, not the FZ-15 decision rule.

- Four ordered ACT DR6 P-ACT-LB CAMB chains (ACT, Planck, lensing, DESI DR1), with half of each chain discarded as instructed by the [official chain guide](https://portal.nersc.gov/project/act/dr6.02/chains/README_chains.html), give 379,175 retained rows and total weight 508,985. For the stated branch `n_s ≈ 0.9660214956374175`, exactly 3,114 weight is at or below the target: **0.611805849%**. Individual chain values span 0.373%–1.031%. We downloaded the official archive, verified its SHA-256 and compared every projected weight and tilt token with the four original chains, including the discarded rows.
- As a separate sensitivity check, deriving `P` from either of the two declared inverse-alpha root outputs shifts the tilt by at most `8.1×10⁻⁸`; neither shift changes the count here. This does not change the frozen target or justify replacing it.
- The result is tension in one specified historical ΛCDM posterior, not a frequentist p-value, model probability, or prospectively eligible rejection. FZ-15 calls for a different product: the designated first eligible Simons Observatory LAT + Planck primary baseline release, not a substitute involving ACT and BAO. See the [anchored protocol description](https://github.com/FloatingPragma/observer-patch-holography/blob/3edcfa2af4387d6bda5634f0bf65f253f7faef65/docs/FROZEN_PREDICTION_LADDER.md#fz-15) and [ACT collaboration paper](https://arxiv.org/html/2503.14452v1).

**Verdict:** retrospectively reproduced; no prospective verdict in this review.

## 04. Is the Standard Model gauge group selected?

**Claim under test:** the upstream [twelve-port A₅ recognition branch](https://github.com/FloatingPragma/observer-patch-holography/blob/3edcfa2af4387d6bda5634f0bf65f253f7faef65/docs/OPH_FALSIFICATION_PROGRAM.md#mature-mathematical-falsifiers) yields the local compact Lie type, given an actual compact 12-dimensional response algebra with inner A₅ and a one-dimensional fixed subspace.

Independent dimension argument: a compact Lie algebra splits as center plus compact simple ideals. Inner automorphisms fix the center and do not permute the simple ideals. The center therefore has dimension at most one. The simple dimensions available through 12 are 3, 8 and 10. Center dimension one leaves 11 semisimple dimensions, necessarily 8+3, giving `u(1) + su(3) + su(2)`. With zero center, dimension 12 is four `su(2)` factors. Each induces either trivial A₅ action (3 fixed dimensions) or a faithful rotational action (0 fixed dimensions, since rotations sharing a fixed axis would be abelian). The fixed dimension in that case is a multiple of 3, impossible under the one-line premise.

**Verdict:** the conditional local Lie-type conclusion follows. The argument cannot distinguish the direct product from its central quotients: they have the same Lie algebra. It neither selects the physical global `Z6` quotient nor proves that the source's actual response operators meet the premises. A follow-up should reconstruct those operators from source histories and independently calculate the shared center kernel of the specified physical matter representations.

## 05. Does the photon branch predict anisotropic vacuum dispersion?

**Claim under test:** under the frozen equal-weight reciprocal cosine-symbol assumptions, the 12 vertex directions (FZ-11) and 30 seam-edge directions (FZ-12) predict different signed rank-six terms. A different polynomial or convention-invariant disagreement within the same directional normalization fails this algebra check. No detector likelihood is evaluated.

Starting from icosahedron coordinates, we independently constructed the vertex and edge orbits and computed their angular-moment polynomials over the exact field Q(√5). Both are isotropic through fourth order; for their even reciprocal symbols, the first non-isotropic term is a degree-six harmonic, normalized to one on a vertex axis. Cosine expansion gives:

| Branch | C4/a² | B0/a⁴ | B6/a⁴ | B6/C4² |
| --- | ---: | ---: | ---: | ---: |
| FZ-11 vertices | −1/20 | 1/840 | +2/7875 | +32/315 |
| FZ-12 edges | −1/20 | 1/840 | −1/12600 | −2/63 |

**Verdict:** both finite coefficient sets reproduced, including the opposite signed coefficients in the common axis convention (not evidence of propagation). FZ-12 requires a physical operator and readout in matching units and a coherent frame. The [frozen contract](https://github.com/FloatingPragma/observer-patch-holography/blob/3edcfa2af4387d6bda5634f0bf65f253f7faef65/docs/FROZEN_PREDICTION_LADDER.md#fz-12) explicitly treats a null as inconclusive unless an independently derived positive minimum scale and a qualifying sensitivity calculation allow exclusion of the full allowed branch. As a tends to zero, the coefficients tend to zero, so a finite-resolution null cannot otherwise exclude every admissible scale.

## Agent handoff

Run `python3 research/oph/queue_ops.py next` to get the next claim, pinned sources and acceptance rule. Use the [queue guide](WORKFLOW.md) to record a plan and result.

## Next checks in order

1. **FZ-12 physical photon dispersion:** audit source-to-photon operator, scale, polarization, frame and detector likelihood together; do not reuse exposed data as a prospective test.
2. **Same-source gravity:** map actual clock, area, entropy and stress records on one sequence of regions; test whether the normalized residuals vanish and compare two matter probes without refitting the metric.
3. **Gauge global form and matter:** reconstruct the physical response algebra; calculate the central kernel; separate assumed matter representations, chirality and family multiplicity from derived results.
4. **Fixed capacity and dark energy:** audit the estimator, inherited cosmology inputs and eligible comparison before scoring. A finite capacity formula is distinct from observed vacuum stress.
5. **Whole-program claim:** specify the allowable class of observer laws and test whether a single realization accounts for the linked observables. A fixed-point example or one recovered identity is insufficient to show that the physical universe is a self-reading computation. Scope exclusions to named branches.

## Reproduce

Python 3.11+ and Git. The numerical replay uses only the standard library. The exact angular-moment check uses SymPy 1.14.0. Neither executes OPH Python, Lean, shell hooks or notebooks.

```sh
git clone --filter=blob:none --sparse https://github.com/FloatingPragma/observer-patch-holography.git oph
git -C oph checkout --detach 3edcfa2af4387d6bda5634f0bf65f253f7faef65
git -C oph sparse-checkout set code/P_derivation/runtime code/cosmology/tilt_posterior
python3 research/oph/replay.py oph
# In an environment with sympy==1.14.0:
python3 research/oph/dispersion.py
# Optional stronger check: fetch the official archive (~163 MB), verify SHA256
# and check every weight/ns token against the pinned upstream projection.
curl -fL https://lambda.gsfc.nasa.gov/data/act/chains/lcdm/p-actbase-l-b_lcdm_camb.tar.gz -o act.tar.gz
python3 research/oph/replay.py oph --act-archive act.tar.gz
```

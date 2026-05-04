 # Differential Nonlinear Robustness of Critical States in Fibonacci and Tribonacci Substitution Chains

**Author:** Pablo Nogueira Grossi — G6 LLC, Newark NJ  
**ORCID:** [0009-0000-6496-2186](https://orcid.org/0009-0000-6496-2186)  
**Zenodo (this paper):** [10.5281/zenodo.20026943](https://doi.org/10.5281/zenodo.20026943)  
**Zenodo (Principia Orthogona Vol. I):** [10.5281/zenodo.19117400](https://doi.org/10.5281/zenodo.19117400)  
**AXLE Lean 4 repo:** [github.com/TOTOGT/AXLE](https://github.com/TOTOGT/AXLE)

---

## What this paper does

We study the discrete nonlinear Schrödinger (DNLS) equation on two quasiperiodic
tight-binding chains — Fibonacci ($n=2$) and Rauzy–tribonacci ($n=3$) — generated
by their substitution rules. Starting from mid-gap eigenstates of the linear
Hamiltonian, we find that:

- The tribonacci mid-gap state (IPR ≈ 0.082) is ~4× more localized than the
  Fibonacci mid-gap state (IPR ≈ 0.021) in the linear limit, consistent with
  stronger Rauzy-fractal multifractality.
- Under DNLS nonlinearity, the Fibonacci state delocalizes rapidly (IPR drops
  ~57% at λ=1.5), while the tribonacci state is nearly pinned (IPR drops <5%).

We call this **differential nonlinear robustness** and give a physical mechanism.
This is, to our knowledge, the first numerical DNLS study on a tribonacci
substitution chain.

---

## Repository contents

```
dnls_nbonacci.py       Main simulation: substitution words, Hamiltonians,
                       DNLS time evolution, bifurcation scan over λ.
                       Produces results_table.txt and ipr_vs_lambda.csv.

TribonacciDNLS.lean    Lean 4/Mathlib4 formal verification of analytic lemmas
                       that underwrite the paper's amplitude envelope.

nbonacci_dnls_paper.pdf  Compiled paper (submitted version).
nbonacci_dnls_paper.tex  LaTeX source.
```

---

## Running the simulation

```bash
pip install numpy scipy
python dnls_nbonacci.py
```

Runtime: approximately 5–10 minutes on a standard laptop (N=500 sites,
10 values of λ, T=50 integration per run).

---

## What is formally verified (Lean 4, no `sorry`)

`TribonacciDNLS.lean` proves the following without `sorry`:

| Theorem | Statement |
|---------|-----------|
| `η_gt_one` | η > 1 (tribonacci constant exceeds 1) |
| `η_pos` | η > 0 |
| `η_characteristic` | η³ = η² + η + 1 |
| `w_pos` | ∀ k, w(k) = η^{−k} > 0 |
| `w_strictAnti` | k < l → η^{−l} < η^{−k} (amplitude envelope is well-defined and decaying) |
| `w_tendsto_zero` | η^{−k} → 0 as k → ∞ |

These facts formally certify that the amplitude envelope $A_k \sim \eta^{-k}$
used in the paper's ansatz (Section 3.2) is mathematically well-posed.

**What is not claimed as verified:**  
The dm³ criticality principle is an `axiom` in the AXLE repository.
GTCT Theorem T1 carries a `sorry`. The g₃₃ = 33 stability threshold is a
conjecture (tracked as AXLE Issue #13). None of these are required for the
DNLS results in this paper.

---

## Key references

- Krebbekx et al., *Phys. Rev. B* **108**, 104204 (2023) — tribonacci tight-binding model
- Lahini et al., *Phys. Rev. Lett.* **103**, 013901 (2009) — DNLS on Fibonacci chains
- Kohmoto, Kadanoff & Tang, *Phys. Rev. Lett.* **50**, 1870 (1983) — Fibonacci spectrum
- Rauzy, *Bull. Soc. Math. France* **110**, 147 (1982) — tribonacci substitution

---

## Related deposits (Zenodo)

| DOI | Title |
|-----|-------|
| [10.5281/zenodo.20026943](https://doi.org/10.5281/zenodo.20026943) | This paper (DNLS Fibonacci/Tribonacci) |
| [10.5281/zenodo.19117400](https://doi.org/10.5281/zenodo.19117400) | Principia Orthogona, Volume I |
| [10.5281/zenodo.19379385](https://doi.org/10.5281/zenodo.19379385) | The dm³ Operator |
| [10.5281/zenodo.19199474](https://doi.org/10.5281/zenodo.19199474) | Wavenumber 6 |

---

## Open proof obligations

The following are tracked in the AXLE sorry roadmap and are not claimed
as verified in this paper:

- [ ] dm³ criticality principle (currently an axiom)
- [ ] GTCT Theorem T1 (sorry in `gtct_t1.lean`)
- [ ] g₃₃ = 33 stability threshold (conjecture, Issue #13)
- [ ] Lean 4 formalization of the IPR inequality (future target)

---

## License

Code: MIT  
Paper text: CC BY 4.0

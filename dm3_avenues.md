# dm³ and GTCT — concrete findings and research avenues

Pablo Nogueira Grossi · working notes · April 2026

---

## 1. What the concrete integration shows

The dm³ system

$$
\dot r = r(1-r^2) + 2(r-1)e^{-z}, \qquad
\dot\theta = 1, \qquad
\dot z = r^2 - 2(r-1)^2 e^{-z}
$$

has a clean and teachable structure that a poster or abstract can stand on.

**Invariant surface.** The cylinder $r = 1$ is invariant: $\dot r \equiv 0$ there. On that cylinder the reduced dynamics collapse to $\dot\theta = 1$, $\dot z = 1$. So the "attractor" is a helix with pitch $2\pi$ winding up the cylinder — not a closed limit cycle but a one-parameter family of helical orbits.

**Linear stability of $r=1$.** Linearising $\dot r$ at $r = 1+\varepsilon$ gives

$$\dot\varepsilon \;\approx\; 2\varepsilon\,(e^{-z}-1).$$

So $r=1$ is linearly attracting for $z>0$, marginal at $z=0$, and repelling for $z<0$. Since $\dot z = 1$ on the attractor, any trajectory that reaches a neighbourhood of the cylinder from above is swept into the attracting regime and converges.

**Empirical basin measurement.** Running a two-parameter sweep over initial conditions $(r_0, z_0)$ and checking for convergence to $r=1$ gives

| $z_0$ | $\varepsilon^+$ (inward from above) | $\varepsilon^-$ (inward from below) |
|-------|-------------------------------------|-------------------------------------|
| $-1.0$ | $0.65$ | $0.02$ |
| $-0.5$ | $\gtrsim 2$ | $0.10$ |
| $\phantom{-}0.0$ | $\gtrsim 2$ | $0.22$ |
| $\phantom{-}0.33$ | $\gtrsim 2$ | $0.32$ |
| $\phantom{-}0.5$ | $\gtrsim 2$ | $0.37$ |
| $\phantom{-}1.0$ | $\gtrsim 2$ | $0.51$ |
| $\phantom{-}2.0$ | $\gtrsim 2$ | $0.76$ |

The basin is **strongly asymmetric**. Upward initial conditions (r > 1) converge from essentially any finite r, once $z_0 \gtrsim -0.5$. Downward initial conditions are the binding constraint, and $\varepsilon^-(z_0)$ is **monotone and approximately linear** in $z_0$.

**Implication for the paper's $\varepsilon_0 = 1/3$ claim.** The number $1/3$ is not a uniform symmetric basin radius over all $z_0$. It is reached at $z_0 \approx 0.35$. Below that it is an *overclaim*; above that it is *conservative*. The honest restatement is one of:

- "For $z_0 \geq z^*$ with $z^* \approx 0.35$, the symmetric basin radius satisfies $\varepsilon(z_0) \geq 1/3$."
- "The pointwise radius at $z_0 = 1/3$ is $\varepsilon \geq 1/3$."
- Drop the specific number and state only that $\varepsilon^-(z_0)$ is monotone increasing with empirically linear slope.

This is a *finding*, not a refutation. It's the kind of clarification that strengthens a paper when reviewers ask "under what conditions?" because you already have the answer.

## 2. What's demonstrated vs claimed

| Item | Status |
|------|--------|
| Contact-manifold setup $(M^3, \alpha)$, Reeb field, operator chain $\mathcal{C}\to\mathcal{K}\to\mathcal{F}\to\mathcal{U}$ | Definitional; standard |
| Existence of the helical attractor on $r = 1$ | Verified analytically and numerically |
| Linear stability for $z > 0$ | Verified via linearisation |
| Symmetric basin radius $\varepsilon_0 = 1/3$ uniform in $z_0$ | **Not supported numerically.** Needs qualifier. |
| Whitney $A_1\!-\!A_3$ classification of singularities along the orbit | Classification is Whitney's; application to this orbit is stated as Step 1, still an *assertion* |
| Tribonacci $g^{33}$ index as deeper invariant | Properly labelled conjectural in the clean draft |
| Universality across seven domains | Conjectural, not demonstrated |

## 3. Concrete avenues (next 2–6 weeks)

These are things you can actually finish and that give the paper something new to point at.

**A. Clean up the $\varepsilon_0$ theorem.** Replace "$\varepsilon_0 = 1/3$" with the $(z_0, \varepsilon)$ curve and prove the linearisation bound from first principles. The bound $\dot\varepsilon = 2\varepsilon(e^{-z}-1)$ is explicit; Gronwall gives a rigorous lower bound on $\varepsilon^-(z_0)$ once you integrate $z(t)$ along the orbit.

**B. Prove the Poincaré-Bendixson analogue.** The system is three-dimensional, so classical PB doesn't apply directly. But restricted to the reduced $(r,z)$ planar system (factoring out $\theta$), PB-style arguments plus the invariant $r=1$ line give a clean existence proof of the attractor. Write that up properly.

**C. Formalise Step 1 in Lean.** Step 1 of the main theorem is the weakest part of the current draft. Formalising just the $(r,z)$ planar reduction in Mathlib4 — invariant line, attracting region, linear stability — is tractable. That's a real AXLE contribution rather than a `sorry` with a name.

**D. Publish the numerical panel.** The 3D phase portrait + $\varepsilon(z_0)$ curve + basin heatmap is a figure package that lives on arXiv and Zenodo alongside the paper. Reproducibility: Python integration script ~80 lines, runs in under a minute.

## 4. Abstract avenues (longer horizon)

These are research directions that come out of the same structure and would each be their own paper.

**E. Contact-Hamiltonian derivation.** The dissipation term $2(r-1)e^{-z}$ looks ad-hoc in the ODE. In contact mechanics (Bravetti, de León–Lainz Valcázar) dissipative dynamics arise as Hamiltonian flows on a contact manifold with Hamiltonian $H$ and dissipation coefficient $\gamma$. Derive the dm³ system as the contact Hamiltonian flow of a specific $H_{\rm diss} = -\gamma V(r) e^{-\beta z}$, identify $V$ and $\gamma$, and the whole system becomes a *natural example* rather than a hand-built one.

**F. Higher-dimensional analogues.** Replace the contact 3-manifold with $(M^{2n+1}, \alpha)$ and construct the analogous system. Does the Whitney $A_k$ taxonomy still apply? Do higher-codimension Thom–Boardman singularities appear?

**G. Other dissipation kernels.** The factor $e^{-z}$ sets the z-dependence of the attracting region. Replacing it with $f(z)$ for various classes of $f$ (polynomial decay, rational, bounded) gives a family of systems with varying basin structure. Map the basin $\varepsilon^-(z_0; f)$ as a functional of $f$.

**H. Connection to focal-radius geometry.** The critical curvature $\kappa^*(x) = 1/\text{foc}(x)$ from the paper is standard in Riemannian comparison geometry (Rauch, Berger). The claim that it coincides with the threshold in the operator chain $\mathcal{K}$ is testable against the dm³ geometry — compute the focal radius of the Reeb foliation directly and compare.

**I. Singularity-theoretic classification.** Rather than asserting that the operator chain lands in $A_1\!-\!A_3$, apply Arnold–Guillemin–Sternberg singularity classification directly to the orbit map $t \mapsto \phi_t(p)$ on the reduced $(r,z)$ system. This gives a rigorous version of the paper's Step 1 without going through the operator chain abstractly.

**J. Empirical grounding.** Before claiming "seven domains" in the paper, pick **one** domain and do it rigorously. Cardiac repolarization dynamics (phase-1 to phase-2 transition in action potentials) or magnetic reconnection onset are the two most tractable. Establish a single, testable, domain-specific prediction that the dm³ framework makes and that alternatives don't. Then you have something concrete to stand on for the wider claim.

## 5. What to drop from the paper, for now

- The "seven empirically verified domains" framing (replace with one, done well, or label all as conjectural).
- The Saturn-hexagon connection as a primary domain (it's speculative).
- The Type-IIB string theory map (this is a separate paper if at all).
- "Three falsifiable predictions for nuclear and high-energy physics" — contact geometry does not predict hadron physics without substantial additional structure.
- The $g^{33}$ index as a numerically motivated constant (keep it as conjecture, do not derive the "$22 = 33 \times 2 \times 1/3$" line from it).

## 6. What to keep

- Contact 3-manifold framework (clean, standard, correct).
- The operator chain $\mathcal{C}\to\mathcal{K}\to\mathcal{F}\to\mathcal{U}$ as organising vocabulary.
- Whitney $A_1\!-\!A_3$ taxonomy as target of classification.
- dm³ as the worked example.
- Lean 4 / Mathlib4 formalisation as ongoing work, honestly reported with remaining `sorry`s.
- Clean references: Bravetti, de León–Lainz Valcázar, Herczeg–Waldron, Ambrosio–Tortorelli / Mumford–Shah, Aharonov–Vaidman, Whitney.

---

*Figures accompanying this document:*
- `dm3_phase_portrait.png` — 3D trajectory, r(t), z(t) for five initial conditions
- `dm3_basin.png` — basin of attraction in (r₀, z₀) plane
- `dm3_epsilon_vs_z.png` — empirical stability radius as a function of initial z
- `dm3_numerical_summary.txt` / `dm3_stability_radius.txt` — numerical tables

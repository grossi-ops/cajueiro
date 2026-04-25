# dm³ Research Programme — Overview

**Pablo Nogueira Grossi · G6 LLC · Newark NJ · 2026**

---

## The dm³ Operator Sequence

The central claim of the programme is that a single four-step operator sequence

```
G = U ∘ F ∘ K ∘ C
```

runs in every generative system:

| Symbol | Name | Action |
|--------|------|--------|
| **C** | Compress | Reduce degrees of freedom; identify the invariant core |
| **K** | Curvature | Impose the geometric constraint (contact structure, curvature tensor) |
| **F** | Fold | Non-linear mixing; the attractor emerges |
| **U** | Unfold | Expand back to observable space; read the pattern |

The sequence is not a metaphor — it is realised concretely in:

- **ODE dynamics** — the dm³ system on a contact 3-manifold
- **Formal proof** — Lean 4 / Mathlib4, 0 extra axioms, 9 documented open `sorry`s
- **Acoustics** — Web Audio API synthesis (ocean → mangue → 111 Hz → Reeb helix)
- **Community pedagogy** — five free public workshops, Newark & Elizabeth NJ, Oct 2026 – Jan 2027

---

## The dm³ ODE System

```
ṙ = r(1 − r²) + 2(r − 1)e⁻ᶻ
θ̇ = 1
ż  = r² − 2(r − 1)²e⁻ᶻ
```

**Main result.** For all initial conditions with r(0) > 1, trajectories converge exponentially to
the unit circle r = 1 at rate μ → −2, while z(t) grows linearly.  The limit set is a
**helical attractor** on the contact 3-manifold.

**Honest correction.** The symmetric Gronwall estimate |r − 1| < 1/3 is not supported
numerically. The empirical inner basin boundary is r\* ≈ 0.80 (asymmetric, tighter than
claimed). See `docs/GCTC_REVIEW.md`.

---

## Four Notebook Topics

The research programme is documented through four computational notebooks
(planned for `notebooks/`):

### 1. `dm3_attractor.ipynb` — Helical attractor numerics
- Integrate the dm³ system with DOP853 at rtol = 10⁻¹⁰
- Reproduce phase portrait, ε vs. z, and basin boundary figures
- Quantify the empirical r\* ≈ 0.80 correction

### 2. `schumann_real_variability.ipynb` — Schumann resonance & ELF background
- Load real ELF/Schumann data (NOAA/GLD360 or synthetic proxy)
- Overlay dm³ resonant frequency (7.83 Hz fundamental coupling)
- Visualise amplitude variability vs. ionosphere height
- *Roadmap:* integrate IRI-2016 ionosphere height profile (Issue #1)

### 3. `hypogeum_acoustics.ipynb` — Malta Hypogeum cavity modes
- Placeholder rectangular cavity → 111 Hz standing-wave modes
- Compare with published Hypogeum acoustic measurements
- *Roadmap:* replace placeholder with real mesh / COMSOL hook (Issue #2)

### 4. `lean_sorry_tracker.ipynb` — Lean 4 formal proof status
- Parse `axle/Main_v6.lean` and enumerate all `sorry` sites
- Track closure status of each obligation
- Priority target: `kappa_lipschitz` (AXLE Issue #12)
- *Roadmap:* extend from toy models to full box + thin-shell forms (Issue #3)

---

## Formal Proof Status

| Obligation | File | Status |
|------------|------|--------|
| `kappa_lipschitz` | `axle/Main_v6.lean` | **Open** (AXLE #12) |
| 8 further `sorry`s | `axle/Main_v6.lean` | Open — see `lean_sorry_tracker.ipynb` |

All proofs use 0 axioms beyond Mathlib4.

---

## Repository Map

```
cajueiro/
├── README.md
├── docs/
│   ├── overview.md          ← this file
│   ├── roadmap.md           ← GitHub Issues #1–#3 (ready to paste)
│   ├── ABSTRACT.md
│   ├── FINDINGS.md
│   ├── GCTC_REVIEW.md
│   └── outreach/
│       ├── email_schumann_elf.md
│       ├── email_iri_ionosphere.md
│       └── email_lightning_em.md
├── notebooks/               ← four notebooks (see above)
├── axle/                    ← Lean 4 formal verification
├── numerics/                ← dm3_simulation.py (DOP853)
├── soundworks/              ← Web Audio API synthesis
└── bienal/                  ← XII Bienal SBM 2026 submissions
```

---

© 2026 Pablo Nogueira Grossi — G6 LLC · MIT License (research code) / CC BY 4.0 (educational materials)

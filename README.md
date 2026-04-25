# DM3-lab

**Pablo Nogueira Grossi · G6 LLC · Newark NJ · 2026**

*One day we hope to walk the line.*

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/grossi-ops/cajueiro/blob/main/notebooks/cross_calibration_dashboard.ipynb)

```bash
# Run in Colab (zero local setup)
# 1. Click the badge above, or open any notebook in notebooks/ directly.
# 2. In the first cell, install dependencies:
!pip install numpy matplotlib scipy sympy pandas
# 3. Run all cells. No API keys, no downloads required.
```

---

## What this is

This repository is the living workspace of the **dm³ research programme** — mathematical, acoustic, pedagogical, and community work developed from 90 Tiffany Blvd, Apt 242, Newark NJ 07104, North Ward, next to the abandoned Boonton Line right-of-way.

The programme has one claim: the same operator sequence

```
G = U ∘ F ∘ K ∘ C
```

— compress, curvature, fold, unfold — runs in every generative system. In a helical attractor on a contact 3-manifold. In a cashew tree establishing itself in difficult soil. In a nurse and a civil engineer sitting across a room realizing they have been working on the same pattern in different languages.

The research is formal (Lean 4 / Mathlib4, zero axioms beyond the library), numerical (DOP853, rtol=10⁻¹⁰), acoustic (Web Audio API, synthesized in-browser), bilingual (Portuguese / English), and community-facing (ArtStart 2026–27, NYFA fiscal sponsorship, five free public workshops in Newark and Elizabeth NJ, starting October 2026).

---

## Repository map

```
DM3-lab/
├── index.html                  ← Cajueiro Soundworks homepage
├── soundworks/                 ← dm³ acoustic machine (ocean + mangue + 111 Hz + Reeb helix)
├── axle/                       ← Lean 4 formal verification (AXLE engine)
│   └── Main_v6.lean            ← 0 axioms beyond Mathlib4 · 9 honest sorrys
├── bienal/                     ← XII Bienal SBM submissions (UFRN, Natal-RN, 3–7 ago 2026)
│   ├── PO_10_Pablo_Grossi.pdf  ← Helical attractors · bilingual PT/EN · 3pp
│   ├── PO_T10_Pablo_Grossi.pdf ← Cymatics with Machines · exposition · T10
│   ├── MC_T1_Pablo_Grossi.pdf  ← Minicurso · helical attractors · 3 sessions
│   ├── OF_T2_Pablo_Grossi.pdf  ← Oficina · Recurrence Ladder · k-nacci → τ=2
│   ├── CO_T2_Pablo_Grossi.pdf  ← Comunicação Oral · O Princípio do Cajueiro
│   └── Ex_T10_Pablo_Grossi.pdf ← Exposição · Cimática com Máquinas
├── artstart/                   ← Newark Arts ArtStart 2026–27 grant application
│   └── ArtStart_Application_Complete.docx
├── numerics/
│   └── dm3_simulation.py       ← Reproduces all figures · DOP853 · ~80 lines
├── docs/
│   ├── ABSTRACT.md
│   ├── FINDINGS.md
│   └── GCTC_REVIEW.md          ← ε₀ → r_star correction · honest audit
└── README.md                   ← this file
```

---

## The dm³ system

```
ṙ = r(1 − r²) + 2(r − 1)e⁻ᶻ
θ̇ = 1
ż = r² − 2(r − 1)²e⁻ᶻ
```

**Main result.** For all initial conditions with r(0) > 1, trajectories converge exponentially to the unit circle r = 1 at rate μ → −2, while z(t) grows linearly. The limit set is a helical attractor on the contact 3-manifold.

**Honest correction.** The paper's symmetric Gronwall estimate |r − 1| < 1/3 is not supported numerically. The empirical inner basin boundary is r* ≈ 0.80 — asymmetric, tighter than claimed. See `docs/GCTC_REVIEW.md`.

**Formal status.** 0 axioms beyond Mathlib4. 9 documented open sorrys. The `kappa_lipschitz` obligation (AXLE Issue #12) remains open and closes the formal version of the main theorem.

---

## The Cajueiro

The cashew tree (*Anacardium occidentale*) establishes itself in difficult soil. Its aerial roots branch, touch the ground, re-root, become new trunks. The Cajueiro de Pirangi, 20 km from the UFRN campus in Natal, covers 8,500 m² from a single organism.

This is the g6 moment: not abundance, not saturation — the first stable seed before the canopy.

The **Cajueiro Workshops** translate this observation into five free public workshops in Newark and Elizabeth NJ (October 2026 – January 2027), a bilingual public installation at Uceda School of Elizabeth (November 2026), and a closing community celebration (February 2027). Funded in part by Newark Arts ArtStart 2026–27. Fiscal sponsor: NYFA.

---

## The Boonton Line

The former Delaware, Lackawanna & Western / Erie Railroad Boonton Line runs directly past this building. Passenger service through Newark's North Ward was abandoned in 2002. The right-of-way is now proposed as the Ice & Iron Greenway (Essex-Hudson Greenway), running from Montclair to the Jersey City waterfront through Glen Ridge, Bloomfield, Belleville, Newark North Ward, and Kearny.

*One day we hope to walk the line.*

---

## Bienal SBM 2026

Five submissions to the XII Bienal da Sociedade Brasileira de Matemática, UFRN, Natal-RN, 3–7 August 2026:

| File | Type | Title |
|------|------|-------|
| `PO_10` | Paper | Helical Attractors on Contact 3-Manifolds: A Toy ODE Study |
| `PO_T10` | Exposition | Cymatics with Machines — Chladni figures, resonance, standing waves |
| `MC_T1` | Minicurso | Helical Attractors — numerical study and Lean 4 formalization |
| `OF_T2` | Oficina | A Escada de Recorrência — k-nacci to the threshold τ = 2 |
| `CO_T2` | Comunicação | O Princípio do Cajueiro — academic English for Brazilian researchers |

All submissions carry: © 2026 Pablo Nogueira Grossi — G6 LLC · MIT License (research code) / CC BY 4.0 (educational materials) · ORCID: 0009-0000-6496-2186

---

## Dual-Cavity Lab (CAVERN ↔ Hypogeum)

The **dm³ dual-cavity framework** treats Schumann resonances (Earth–ionosphere cavity, CAVERN)
and acoustic eigenmodes in Hypogeum-style chambers as two instances of the same Helmholtz
eigenproblem, with all geometry generated by G = U ∘ F ∘ K ∘ C.

| Notebook | Description |
|----------|-------------|
| `notebooks/hypogeum_dm3_fit.ipynb` | Inverse fit: Wolfe/Debertolis/Till Hypogeum peaks → dm³ parameters |
| `notebooks/schumann_dm3_fit.ipynb` | Mirror: observed Schumann peaks → same dm³ pipeline |
| `notebooks/cross_calibration_dashboard.ipynb` | Side-by-side normalized softening; translation dictionary |
| `notebooks/schumann_real_variability.ipynb` | Real ionospheric variability (day/night, solar cycle, events) |

**Key result:** The curvature parameter κ that models 10–25 cm Neolithic wall offsets
(Wolfe et al. 2020) spans exactly the observed day/night (∼5 km) and solar-cycle
(∼2.5 km) ionospheric height range. The Hypogeum is a quantitatively valid
laboratory analog for planetary ELF modeling.

See [`docs/overview.md`](docs/overview.md) for the full system description and
[`docs/roadmap.md`](docs/roadmap.md) for the open issues roadmap.

---

## Soundworks

The **dm³ Soundworks** machine synthesizes the acoustic environment of the cajueiro — the Atlantic mangue, tidal rhythms, archaeoacoustic frequencies — entirely in-browser via Web Audio API. No samples. Runs offline.

Layers:
- **Ocean** — pink noise shaped to Atlantic tidal breath at 0.05 Hz
- **Mangue** — mangrove channel standing-wave resonance, 40–90 Hz, modulated at 0.12 Hz
- **111 Hz** — Malta Hypogeum / Chavín de Huántar frequency, 6 Hz binaural beat (theta)
- **Reeb helix** — pitch modulated in real time by z(t) from the dm³ system, base 110 Hz, η ≈ 1.8393

Live: [totogt.github.io/AXLE/impa-portal.html](https://totogt.github.io/AXLE/impa-portal.html)  
Gumroad: [g6llc.gumroad.com/l/soundworks](https://g6llc.gumroad.com/l/soundworks) · $25–$250 · living book access, Volumes I–VI

---

## Zenodo & citations

All volumes of the Principia Orthogona series are deposited open-access:

```
DOI: 10.5281/zenodo.19117400
HAL: hal-05555216 · hal-05559997
```

| Volume | Title | ISBN (print) |
|--------|-------|-------------|
| I | GOMC Science | 979-8-9954416-4-9 |
| II | TOGT | 979-8-9954416-2-5 |
| III | The Mini-Beast | 979-8-9954416-6-3 |
| IV | GTCT Bilingual | 979-8-9954416-8-7 |
| V | AXLE (Lean 4) | github.com/TOTOGT/AXLE |
| Series | Complete Edition | 979-8-9954416-0-1 |

---

## Community & funding

| Project | Status |
|---------|--------|
| Newark Arts ArtStart 2026–27 | Applied May 1, 2026 |
| NYFA fiscal sponsorship | Submitted · ~2 days processing |
| NJ State Council on the Arts | Applying June 2026 |
| Geraldine R. Dodge Foundation | LOI July 2026 |
| Newark Wellness Center · 229 Ballantine Pkwy · Forest Hill | Vision |

---

## License

Research code (AXLE, numerics): **MIT License**  
Educational materials (Bienal submissions, Teachers Manual): **CC BY 4.0**  
Art and soundworks: **MIT License**

© 2026 Pablo Nogueira Grossi — G6 LLC  
EIN: 33-2880433 · NJSOS: 0600484861  
90 Tiffany Blvd Apt 242 · Newark NJ 07104  
pablo@g6-llc.org · ORCID: 0009-0000-6496-2186  
github.com/TOTOGT/GTCT · github.com/TOTOGT/AXLE · github.com/DM3-lab

import Lake
open Lake DSL

package «dm3-dual-cavity» where
  version := v!"0.2.0"

require mathlib from git
  "https://github.com/leanprover-community/mathlib4" @ "v4.14.0"

-- AXLE engine (TOTOGT/AXLE) — primary verified source of dm³ operator algebra.
-- Activate once AXLE's lakefile exports are stable (pending AXLE Issue #12):
--   require AXLE from git "https://github.com/TOTOGT/AXLE" @ "main"

/-- dm³ dual-cavity spectral geometry (Hypogeum ↔ Schumann). -/
lean_lib «dm3-dual-cavity» where
  globs := #[.submodules `«dm3-dual-cavity»]

/-- Nuclear Physics B formal skeleton — TOGT in strong interactions. -/
lean_lib NuclearPhysicsB where
  globs := #[.submodules `NuclearPhysicsB]

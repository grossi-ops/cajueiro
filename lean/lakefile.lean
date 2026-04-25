import Lake
open Lake DSL

package «dm3-dual-cavity» where
  version := v!"0.1.0"

require mathlib from git
  "https://github.com/leanprover-community/mathlib4" @ "v4.14.0"

lean_lib «dm3-dual-cavity» where
  globs := #[.submodules `«dm3-dual-cavity»]

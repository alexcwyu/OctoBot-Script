# Development

## uv maintenance workflow (2026-10-12)

Selected complete environment: Python 3.15.0; build backend `hatchling.build`. The workspace uses uv 0.13.0. The complete latest-source native build and original repository suite are verified; exact results are recorded in [validation](validation.md).

```sh
export UV_PYTHON_PREFERENCE=only-managed
export PYCARES_USE_SYSTEM_LIB=1
export CFLAGS='-I/opt/homebrew/opt/c-ares/include'
export LDFLAGS='-L/opt/homebrew/opt/c-ares/lib'
uv python install 3.15.0
uv lock --upgrade
uv sync --all-extras --python 3.15.0
uv build --python 3.15.0
uv run --frozen --all-extras python -m compileall -q src/octobot_script
uv run --frozen --all-extras python -m pytest tests
```

Before building distributable reports, run `npm ci` and `npm run build`. Vite writes the packaged report under src/octobot_script/resources/report/dist. Plugin provisioning is explicit; USE_CUSTOM_TENTACLES=true requires the caller to provide a compatible generated tentacles namespace.

Keep source resources inside their package and preserve the repository's existing src layout. Rebuild after source/native/asset changes. Use the locked environment for final verification. Commands above are the standard workflow, not a promise that every existing suite currently passes; consult validation for exact outcomes and unresolved compatibility issues.

## Current native indicator source

The top-level uv source explicitly selects [the adjacent licensed Tulipy 0.4.11b13 source](../../OctoBot/vendor/octobot-tulipy/PROVENANCE.md), retaining NumPy 2.4.2 and the original indicator formulas. Strict native multiply/add compiler flags preserve original RSI arithmetic. This resolves the missing Python 3.15 release wheel through a genuine current-source build. This repository’s own original suite, source distribution, wheel and strict source compilation pass in an isolated Python 3.15 control before selecting that interpreter. No host-package suite substitutes for the standalone cases.

On this macOS SDK, pycares builds against the actual Homebrew c-ares installation using its supported `PYCARES_USE_SYSTEM_LIB=1` option and the include/library paths above. This avoids the bundled dependency’s `pipe2` deployment-target mismatch without changing the operating-system target.

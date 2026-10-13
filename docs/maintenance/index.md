# OctoBot-Script: portable verification records

<!-- current-documentation-provenance -->
Documentation reviewed: 2026-10-13 · Git source base: `3b24149f79abfa1c97b34b2395b41ef04898c480` · [Current architecture and feature guide](../ayu-develop.md).
Historical execution commands/results below retain their original dates and scope; this metadata update is not a new application test run.
<!-- /current-documentation-provenance -->


These records retain exact commands, outcomes, original-log hashes and available source snapshots. Failed, interrupted and earlier exploratory commands remain visible. A later focused pass proves only its own scope.

[Machine-readable records](verification.json) · [Validation](../validation.md) · [Engineering guide](../ayu-develop.md)

Original logs remain in the workspace maintenance evidence. Tracked source hashes exclude untracked additions and later edits, as stated in each captured snapshot.

| Check | Exit | Duration | Command |
| --- | ---: | ---: | --- |
| build | 0 | 0.95s | `uv build --python 3.13` |
| compile | 0 | 0.08s | `<workspace>/OctoBot-Script/.venv/bin/python -m compileall -q src` |
| current-sync-2 | 0 | 0.97s | `uv sync --all-extras --python 3.14` |
| current-sync | 0 | 0.4s | `uv sync --all-extras --python 3.14` |
| final-build-2 | 0 | 3.13s | `uv build --python 3.14.8` |
| final-build-3 | 0 | 2.68s | `uv build --python 3.14.8` |
| final-build | 0 | 5.09s | `uv build --python 3.14.8` |
| final-compile-2 | 0 | 0.07s | `.venv/bin/python -m compileall -q src` |
| final-compile | 0 | 0.14s | `.venv/bin/python -m compileall -q src` |
| final-lock-2 | 0 | 0.49s | `uv lock --upgrade` |
| final-lock | 0 | 0.48s | `uv lock --upgrade` |
| final-sync-2 | 0 | 0.65s | `uv sync --all-extras --frozen --python 3.14.8` |
| final-sync | 0 | 2.17s | `uv sync --all-extras --frozen --python 3.14.8` |
| lock-3.13 | 0 | 0.85s | `uv lock --upgrade --python 3.13` |
| lock-3.14 | 0 | 0.72s | `uv lock --upgrade --python 3.14` |
| lock-3.15 | 0 | 0.61s | `uv lock --upgrade --python 3.15` |
| report-build | 0 | 11.97s | `npm run build` |
| report-install | 0 | 24.44s | `npm ci` |
| compile | 0 | 0.05s | `.venv/bin/python -Werror -m compileall -q src` |
| sync | 0 | 3.16s | `uv sync --all-extras --frozen --python 3.15.0` |
| build | 0 | 2.5s | `uv build --python 3.15.0` |
| compile | 0 | 0.08s | `/tmp/octobot-script-final315-control/bin/python -Werror -m compileall -q src` |
| lock | 0 | 1.9s | `uv lock` |
| sync | 0 | 1.42s | `uv sync --all-extras --frozen --python 3.15.0` |
| tests | 0 | 18.4s | `/tmp/octobot-script-final315-control/bin/python -m pytest tests --tb=short` |
| sync-3.13 | 1 | 2.17s | `uv sync --all-extras --python 3.13` |
| sync-3.14 | 1 | 4.65s | `uv sync --all-extras --python 3.14` |
| sync-3.15 | 1 | 6.04s | `uv sync --all-extras --python 3.15` |
| tests-2 | 2 | 35.64s | `.venv/bin/python -m pytest tests` |
| tests-3 | 2 | 20.53s | `.venv/bin/python -m pytest tests` |
| tests-4 | 0 | 38.37s | `.venv/bin/python -m pytest tests` |
| tests | 1 | 0.04s | `<workspace>/OctoBot-Script/.venv/bin/python -m pytest tests` |

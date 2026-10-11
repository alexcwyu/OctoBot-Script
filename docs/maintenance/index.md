# OctoBot-Script: portable verification records

Full raw logs are retained in the workspace maintenance evidence, not distributed here. Hashes identify those original logs. A successful build or selected test subset does not imply a full test-suite pass. Commands containing <workspace> describe the original execution environment.

[Machine-readable records](verification.json) · [Repository validation summary](../validation.md)

## Executed commands

| Check | Exit | Duration | Command | Outcomes |
| --- | ---: | ---: | --- | --- |
| build | 0 | 0.95s | `uv build --python 3.13` | Successfully built dist/octobot_script-0.1.1.tar.gz<br>Successfully built dist/octobot_script-0.1.1-py3-none-any.whl |
| compile | 0 | 0.08s | `<workspace>/OctoBot-Script/.venv/bin/python -m compileall -q src` | See exit status; no test-count assertion. |
| current-sync | 0 | 0.4s | `uv sync --all-extras --python 3.14` | See exit status; no test-count assertion. |
| current-sync-2 | 0 | 0.97s | `uv sync --all-extras --python 3.14` | See exit status; no test-count assertion. |
| final-build | 0 | 5.09s | `uv build --python 3.14.8` | Successfully built dist/octobot_script-0.1.1.tar.gz<br>Successfully built dist/octobot_script-0.1.1-py3-none-any.whl |
| final-build-2 | 0 | 3.13s | `uv build --python 3.14.8` | Successfully built dist/octobot_script-0.1.1.tar.gz<br>Successfully built dist/octobot_script-0.1.1-py3-none-any.whl |
| final-build-3 | 0 | 2.68s | `uv build --python 3.14.8` | Successfully built dist/octobot_script-0.1.1.tar.gz<br>Successfully built dist/octobot_script-0.1.1-py3-none-any.whl |
| final-compile | 0 | 0.14s | `.venv/bin/python -m compileall -q src` | See exit status; no test-count assertion. |
| final-compile-2 | 0 | 0.07s | `.venv/bin/python -m compileall -q src` | See exit status; no test-count assertion. |
| final-lock | 0 | 0.48s | `uv lock --upgrade` | See exit status; no test-count assertion. |
| final-lock-2 | 0 | 0.49s | `uv lock --upgrade` | See exit status; no test-count assertion. |
| final-sync | 0 | 2.17s | `uv sync --all-extras --frozen --python 3.14.8` | See exit status; no test-count assertion. |
| final-sync-2 | 0 | 0.65s | `uv sync --all-extras --frozen --python 3.14.8` | See exit status; no test-count assertion. |
| lock-3.13 | 0 | 0.85s | `uv lock --upgrade --python 3.13` | See exit status; no test-count assertion. |
| lock-3.14 | 0 | 0.72s | `uv lock --upgrade --python 3.14` | See exit status; no test-count assertion. |
| lock-3.15 | 0 | 0.61s | `uv lock --upgrade --python 3.15` | See exit status; no test-count assertion. |
| report-build | 0 | 11.97s | `npm run build` | See exit status; no test-count assertion. |
| report-install | 0 | 24.44s | `npm ci` | See exit status; no test-count assertion. |
| sync-3.13 | 1 | 2.17s | `uv sync --all-extras --python 3.13` | See exit status; no test-count assertion. |
| sync-3.14 | 1 | 4.65s | `uv sync --all-extras --python 3.14` | See exit status; no test-count assertion. |
| sync-3.15 | 1 | 6.04s | `uv sync --all-extras --python 3.15` | See exit status; no test-count assertion. |
| tests | 1 | 0.04s | `<workspace>/OctoBot-Script/.venv/bin/python -m pytest tests` | See exit status; no test-count assertion. |
| tests-2 | 2 | 35.64s | `.venv/bin/python -m pytest tests` | See exit status; no test-count assertion. |
| tests-3 | 2 | 20.53s | `.venv/bin/python -m pytest tests` | See exit status; no test-count assertion. |
| tests-4 | 0 | 38.37s | `.venv/bin/python -m pytest tests` | ============================= 14 passed in 34.04s ============================== |

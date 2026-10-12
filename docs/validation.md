# OctoBot-Script: final Python 3.15 verification

Selected runtime: **managed Python 3.15.0**, uv **0.13.0**; source commit `3ab9beccb9c91ef2fec34b25bea127f9da25997b`. Its own existing repository suite passed: **14 passed in 16.33s**. This is the original standalone repository suite, separately executed from the newer host's package suites. Source distribution and wheel builds, frozen synchronization and strict source compilation passed. No test cases, golden values or formulas changed.

[Development and native prerequisites](development.md) · [Portable exact commands](maintenance/index.md) · [Machine-readable evidence](maintenance/verification.json). The locked adjacent licensed source and supported system-library configuration are explicit in the project metadata and development guide.

## Historical verification attempts


Recorded 2026-10-12T01:32:45.053223+08:00. Branch `feature/ayu_develop`; upstream default `upstream/master` is merged: **true**. Branch/tag synchronization records are retained in the workspace maintenance evidence. Feature branch publication is coordinated separately.

Runtime: **CPython 3.14.8**, uv **0.13.0**, build backend `hatchling.build`. The local OctoBot full environment requires Tulipy, which has no Python 3.15 distribution; Python 3.14.8 is selected.

Existing suite: **============================= 14 passed in 34.04s ==============================** (exit `0`). Existing tests pass. npm ci and npm run build also pass for the embedded report; legacy implicit install hooks are replaced by explicit documented uv/npm/tentacles steps.

No test cases were added. Existing assertions and strict warning behavior remain active; repaired fixtures own their loops, sessions, files and configuration paths. Existing upstream platform skips and configured deselections are reported exactly.

## Final build commands

| Check | Exact command | Exit | Seconds |
| --- | --- | ---: | ---: |
| lock | `uv lock --upgrade` | 0 | 0.49 |
| sync | `uv sync --all-extras --frozen --python 3.14.8` | 0 | 0.65 |
| build | `uv build --python 3.14.8` | 0 | 2.68 |
| compile | `.venv/bin/python -m compileall -q src` | 0 | 0.07 |

## Existing test and compatibility evidence

| Check | Exact command | Exit | Result |
| --- | --- | ---: | --- |
| lock-3.15 | `uv lock --upgrade --python 3.15` | 0 | Check completed; see exact exit code. |
| sync-3.15 | `uv sync --all-extras --python 3.15` | 1 | Check completed; see exact exit code. |
| tests | `/Users/alex/workspaces/trading/OctoBot-Script/.venv/bin/python -m pytest tests` | 1 | Check completed; see exact exit code. |
| report-install | `npm ci` | 0 | Check completed; see exact exit code. |
| tests-2 | `.venv/bin/python -m pytest tests` | 2 | ============================== 3 errors in 29.45s ============================== |
| tests-3 | `.venv/bin/python -m pytest tests` | 2 | ============================== 3 errors in 15.04s ============================== |
| tests-4 | `.venv/bin/python -m pytest tests` | 0 | ============================= 14 passed in 34.04s ============================== |

Raw logs remain in the workspace maintenance evidence directory. The [portable verification record](maintenance/verification.json) retains exact command arrays, exits, timing, runtime inventory and log filenames. Earlier failed attempts remain recorded and are not treated as successful final validation.

## Installed dependency versions

This is the selected environment after locked synchronization; isolated wheel build dependencies are resolved by the build backend and recorded in build output.

| Distribution | Version |
| --- | --- |
| aioboto3 | 13.3.0 |
| aiobotocore | 2.16.0 |
| aiodns | 4.0.4 |
| aiofiles | 25.1.0 |
| aiohappyeyeballs | 2.7.1 |
| aiohttp | 3.14.5 |
| aioitertools | 0.13.0 |
| aiosignal | 1.4.0 |
| aiosqlite | 0.22.1 |
| annotated-doc | 0.0.5 |
| annotated-types | 0.8.0 |
| anyio | 4.15.1 |
| appdirs | 1.4.4 |
| argon2-cffi | 25.1.0 |
| argon2-cffi-bindings | 26.1.0 |
| asgiref | 3.12.1 |
| asyncpraw | 8.0.3 |
| asyncprawcore | 4.0.0 |
| attrs | 26.1.0 |
| bcrypt | 5.0.0 |
| bitarray | 3.12.0 |
| blinker | 1.9.0 |
| boto3 | 1.35.81 |
| botocore | 1.35.81 |
| cachetools | 7.2.1 |
| certifi | 2026.7.22 |
| cffi | 2.1.1 |
| charset-normalizer | 3.5.2 |
| ckzg | 2.1.8 |
| click | 8.5.0 |
| clickhouse-connect | 1.10.0 |
| coingecko-openapi-client | 1.4.0 |
| colorlog | 6.12.0 |
| coverage | 7.16.2 |
| cryptography | 50.0.2 |
| Cython | 3.3.0 |
| cytoolz | 1.2.0 |
| dbos | 3.2.0 |
| defusedxml | 0.7.1 |
| deprecation | 2.1.0 |
| eth-account | 0.14.0 |
| eth-hash | 0.8.0 |
| eth-keyfile | 0.10.0 |
| eth-keys | 0.8.0 |
| eth-rlp | 3.0.0 |
| eth-typing | 6.0.0 |
| eth-utils | 6.0.0 |
| eth_abi | 6.0.0 |
| execnet | 2.1.2 |
| fastapi | 0.143.0 |
| Flask | 3.1.3 |
| flask-cors | 6.0.5 |
| Flask-Login | 0.6.3 |
| Flask-WTF | 1.3.0 |
| frozenlist | 1.8.0 |
| gmqtt | 0.8.0 |
| greenlet | 3.5.6 |
| h11 | 0.16.0 |
| h2 | 4.4.1 |
| hexbytes | 2.0.0 |
| hpack | 4.2.0 |
| httpcore | 1.0.9 |
| httpcore2 | 2.13.1 |
| httpx | 0.28.1 |
| httpx-sse | 0.4.3 |
| httpx2 | 2.13.1 |
| hyperframe | 6.1.0 |
| idna | 3.20 |
| iniconfig | 2.3.1 |
| itsdangerous | 2.2.0 |
| Jinja2 | 3.1.6 |
| jiter | 0.17.0 |
| jmespath | 1.1.0 |
| jsonschema | 4.26.0 |
| jsonschema-specifications | 2025.9.1 |
| lz4 | 4.4.5 |
| MarkupSafe | 3.0.4 |
| mcp | 1.30.0 |
| mnemonic | 0.21 |
| mock | 5.2.0 |
| multidict | 7.1.0 |
| numpy | 2.4.2 |
| octobot | 3.0.0b3 |
| octobot-script | 0.1.1 |
| OctoBot-Tulipy | 0.4.11b13 |
| octobot_ccxt | 0.0.6 |
| openai | 3.28.0 |
| opentelemetry-api | 1.45.1 |
| packaging | 26.3 |
| parsimonious | 0.10.0 |
| passlib | 1.7.4 |
| PGPy | 0.6.0 |
| pluggy | 1.6.0 |
| postgrest | 2.32.0 |
| propcache | 0.5.4 |
| protobuf | 7.36.2 |
| psutil | 7.2.2 |
| psycopg | 3.3.6 |
| psycopg-binary | 3.3.6 |
| py-ecc | 8.0.0 |
| pyasn1 | 0.6.4 |
| pycares | 5.1.0 |
| pycparser | 3.11 |
| pycryptodome | 3.24.0 |
| pydantic | 2.14.0 |
| pydantic-settings | 2.15.0 |
| pydantic_core | 2.50.0 |
| Pygments | 2.21.0 |
| PyJWT | 2.15.1 |
| pyngrok | 8.1.2 |
| pytest | 9.1.1 |
| pytest-asyncio | 1.4.0 |
| pytest-cov | 7.1.0 |
| pytest-timeout | 2.4.0 |
| pytest-xdist | 3.8.0 |
| python-dateutil | 2.9.0.post0 |
| python-dotenv | 1.2.4 |
| python-multipart | 0.0.32 |
| python-telegram-bot | 22.8 |
| pyunormalize | 18.0.0 |
| PyYAML | 6.0.3 |
| realtime | 2.32.0 |
| referencing | 0.37.0 |
| regex | 2026.9.29 |
| requests | 2.34.2 |
| rlp | 5.0.0 |
| rpds-py | 2026.9.1 |
| ruff | 0.17.0 |
| s3transfer | 0.10.4 |
| sentry-sdk | 2.71.0 |
| setuptools | 84.0.0 |
| simplifiedpytrends | 1.1.2 |
| six | 1.17.0 |
| sniffio | 1.3.1 |
| sortedcontainers | 2.4.0 |
| SQLAlchemy | 2.1.4 |
| sse-starlette | 3.5.0 |
| standard-imghdr | 3.13.0 |
| starfish-identities | 3.0.0a72 |
| starfish-keyring | 3.0.0a72 |
| starfish-protocol | 3.0.0a72 |
| starfish-replica | 3.0.0a72 |
| starfish-sdk | 3.0.0a72 |
| starfish-server | 3.0.0a72 |
| starfish-sharing | 3.0.0a72 |
| starfish-spaces | 3.0.0a72 |
| starlette | 1.7.0 |
| storage3 | 2.32.0 |
| StrEnum | 0.4.15 |
| supabase | 2.32.0 |
| supabase-auth | 2.32.0 |
| supabase-functions | 2.32.0 |
| tinydb | 4.9.0 |
| toolz | 1.2.0 |
| truststore | 0.10.4 |
| typing-inspection | 0.4.4 |
| typing_extensions | 4.16.0 |
| update_checker | 1.0.0 |
| urllib3 | 2.8.0 |
| uvicorn | 0.54.0 |
| vaderSentiment | 3.3.2 |
| web3 | 8.0.0 |
| websockets | 15.0.1 |
| Werkzeug | 3.1.9 |
| wheel | 0.48.0 |
| wrapt | 1.17.3 |
| WTForms | 3.2.2 |
| yarl | 1.25.1 |

See [architecture](ayu-develop.md) for source-linked component/sequence/workflow diagrams and [development](development.md) for reproducible uv commands.

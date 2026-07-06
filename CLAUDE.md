# pyDatalog — CLAUDE.md

Magnon mirror of the pyDatalog library — Python logic programming.
Part of MagnonOS Project-Aethra.

## Purpose

Magnon's private mirror of the unmaintained pyDatalog library. Used by Project-Aethra
for Datalog-based policy evaluation and knowledge querying in the NeSy (neurosymbolic)
pipeline. Note: upstream is unmaintained — consider IDP-Z3 for new features.

Upstream: https://github.com/pcarbonn/pyDatalog (unmaintained)

## Tech stack

- Python (Datalog engine)
- Note: unmaintained upstream — use only for existing integrations

## Quick Start / Dev commands

```bash
# Install (editable)
pip install -e .

# Install with dev dependencies
pip install -e '.[dev]'

# Smoke check
python -c "from pyDatalog import pyDatalog; print('OK')"

# Run a module
python -m <module>
```

## Testing

```bash
pytest
```

## Key conventions

- This is a **maintenance mirror only** — do not add new features or APIs.
- New Datalog/logic programming needs should use IDP-Z3 instead.
- Bug fixes are accepted; new feature development is not.

## What NOT to do

- Never add new features — only bug fixes and compatibility patches.
- Never use `ubuntu-latest` CI runners — always `magnon-enterprise-runners`.
- Do not use as a dependency for new services — prefer IDP-Z3.

## CI

All GitHub Actions workflow jobs use `runs-on: magnon-enterprise-runners`.

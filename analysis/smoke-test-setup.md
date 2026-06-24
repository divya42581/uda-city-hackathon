# SUEWS Smoke Test Setup

Date: 2026-06-24

The official UDA-city smoke test was run using the previously installed SUEWS
practice environment:

`C:\Users\thaku\Documents\Codex\2026-06-22\you-re-helping-me-get-set\suews-hackathon-practice\.venv\Scripts\python.exe`

Command:

```powershell
python scripts\smoke_test.py
```

Working directory:

`data\uda-city-hackathon`

Result:

```text
OK: 10 site(s) x 2,016 steps (7 days) under supy 2026.6.5; NARP+OHM on disk; T2 26.2..38.9 C; config: uda-city.yml.
```

This confirms the UDA-city SUEWS configuration loads, runs a 7-day present
hot-humid window, and produces finite `T2` and `QH` diagnostics across all 10
neighbourhood grids.

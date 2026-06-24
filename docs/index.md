# UDA-city Hackathon Setup

This repository is set up for the SUEWS Community Hackathon practice workflow.

## Current Status

- Repository created from `UMEP-dev/suews-hackathon-template`.
- `TASK_BRIEF.md` reviewed.
- UDA-city challenge dataset loaded into `data/uda-city-hackathon`.
- Official SUEWS smoke test completed for 10 neighbourhoods.
- GitHub Pages enabled from the `docs/` folder.

## Smoke Test Result

The setup was checked with the official UDA-city smoke test using `supy 2026.6.5`.

```text
OK: 10 site(s) x 2,016 steps (7 days) under supy 2026.6.5; NARP+OHM on disk; T2 26.2..38.9 C; config: uda-city.yml.
```

## Step 1: Present Heat Risk

The present hot-humid scenario has now been run for all 10 UDA-city
neighbourhoods. The first pass uses the reference bridge supplied with the
dataset:

- hazard: dangerous-heat hours, counted when hourly mean `T2 > 35 C`
- exposure: daytime population density
- vulnerability: equal-weighted synthetic socio-economic vulnerability proxies
- risk: geometric mean of hazard, exposure, and vulnerability, scaled to `[0, 1]`

| Rank | Neighbourhood | Type | Dangerous heat hours | Risk index |
|---:|---|---|---:|---:|
| 1 | Kampong Lama | hotspot | 42 | 1.000 |
| 2 | Dhobi Lines | hotspot | 26 | 0.833 |
| 3 | Fuzhou Lanes | hotspot | 22 | 0.800 |
| 4 | Mlima Moto | hotspot | 5 | 0.429 |
| 5 | Lusitano Square | core | 5 | 0.176 |
| 6 | Victoria Exchange | core | 5 | 0.151 |
| 7 | Jade Gardens | refuge | 62 | 0.000 |
| 7 | Taman Melati | refuge | 47 | 0.000 |
| 7 | Serendib Rise | refuge | 26 | 0.000 |
| 7 | Zheng He Towers | core | 2 | 0.000 |

The main pattern is that the highest heat hazard is not automatically the
highest heat risk. Jade Gardens has the most dangerous-heat hours, but Kampong
Lama ranks highest for risk because the reference bridge combines hazard with
much higher exposure and vulnerability.

## Hackathon Task

The full hackathon task is to use SUEWS to produce a heat-hazard layer for
UDA-city, translate that hazard into a socio-economic heat-risk indicator, and
explain clearly where the hazard-to-risk bridge is scientifically strong and
where it breaks.

## SUEWS Citation

Jarvi, L., Grimmond, C.S.B. and Christen, A. (2011). The Surface Urban Energy
and Water Balance Scheme (SUEWS): Evaluation in Los Angeles and Vancouver.
Journal of Hydrology, 411(3-4), 219-237.

Ward, H.C., Kotthaus, S., Jarvi, L. and Grimmond, C.S.B. (2016). Surface Urban
Energy and Water Balance Scheme (SUEWS): Development and evaluation at two UK
sites. Urban Climate, 18, 1-32.

# UDA-city Hackathon Setup

This repository is set up for the SUEWS Community Hackathon practice workflow.

## Objective

To compare present and future neighbourhood heat risk in UDA-city, using SUEWS
modelled heat hazard together with population exposure and vulnerability, and to
identify where heat-risk planning should be prioritised.

## Neighbourhood Characteristics

UDA-city has 10 synthetic neighbourhoods. Surface fractions are from the
canonical model input sidecar, and population density is in people per hectare.
The deciduous-tree fraction is `0.000` for all neighbourhoods.

| Grid | Neighbourhood | Type | Paved | Buildings | Evergreen trees | Grass | Bare soil | Water | Day pop. | Night pop. |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Jade Gardens | refuge | 0.593 | 0.047 | 0.108 | 0.072 | 0.100 | 0.080 | 80 | 100 |
| 2 | Serendib Rise | refuge | 0.572 | 0.068 | 0.108 | 0.072 | 0.100 | 0.080 | 80 | 100 |
| 3 | Taman Melati | refuge | 0.567 | 0.073 | 0.108 | 0.072 | 0.100 | 0.080 | 80 | 100 |
| 4 | Kampong Lama | hotspot | 0.710 | 0.140 | 0.030 | 0.020 | 0.080 | 0.020 | 300 | 400 |
| 5 | Dhobi Lines | hotspot | 0.680 | 0.170 | 0.030 | 0.020 | 0.080 | 0.020 | 300 | 400 |
| 6 | Lusitano Square | core | 0.600 | 0.200 | 0.060 | 0.040 | 0.050 | 0.050 | 250 | 130 |
| 7 | Mlima Moto | hotspot | 0.510 | 0.340 | 0.030 | 0.020 | 0.080 | 0.020 | 300 | 400 |
| 8 | Victoria Exchange | core | 0.460 | 0.340 | 0.060 | 0.040 | 0.050 | 0.050 | 250 | 130 |
| 9 | Fuzhou Lanes | hotspot | 0.500 | 0.350 | 0.030 | 0.020 | 0.080 | 0.020 | 300 | 400 |
| 10 | Zheng He Towers | core | 0.360 | 0.440 | 0.060 | 0.040 | 0.050 | 0.050 | 250 | 130 |

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

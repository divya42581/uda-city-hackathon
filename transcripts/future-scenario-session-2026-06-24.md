# Future Scenario Session Transcript Summary

Date: 2026-06-24

## User Request

Run the SUEWS model for the future scenario as well, check that it worked, save
the future heat-risk output, and push the result to the repository.

## Actions Taken

1. Inspected the existing analysis folder, bridge documentation, dataset files,
   and current git status.
2. Checked `data/uda-city-hackathon/scenarios.yml` to identify the future
   forcing setup.
3. Confirmed that the future scenario uses:
   - `forcing/future_hot_humid/UDA_2024_data_60.txt`,
   - a uniform `+2.5 C` pseudo-warming of the present hot-humid forcing,
   - the same UDA-city neighbourhood configuration as the present scenario.
4. First tried the dataset-local Python environment, but it did not include the
   required `supy.suews_sim` module.
5. Switched to the previously verified working SUEWS/SuPy environment:

   ```text
   C:\Users\thaku\Documents\Codex\2026-06-22\you-re-helping-me-get-set\suews-hackathon-practice\.venv\Scripts\python.exe
   ```

6. Ran the future scenario through the supplied `risk_bridge.py` workflow.
7. Saved the derived future heat-risk table as:

   ```text
   analysis/risk_future.csv
   ```

8. Checked the output table and confirmed all 10 UDA-city neighbourhoods were
   included.
9. Added `SuPy.log` to `.gitignore` so runtime logs from model runs are not
   accidentally committed.
10. Committed and pushed the future results to GitHub.

## Key Output

The future scenario completed successfully and produced heat-risk metrics for
all 10 neighbourhoods.

Top future heat-risk ranks:

1. Kampong Lama
2. Fuzhou Lanes
3. Dhobi Lines
4. Mlima Moto

Jade Gardens had the highest number of dangerous-heat hours in the future
scenario, but its final heat-risk score remained low because daytime population
exposure is low in the risk bridge.

## Files Added or Updated

- `analysis/risk_future.csv`
- `.gitignore`

## Recent Commit

- `c1cead1 Add future heat-risk results`

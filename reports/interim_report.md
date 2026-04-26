# Week 0 Interim Report (African Climate Trend Analysis)

## Candidate

- Name: Elsa Alemayehu
- Program Track:AI and Machine Learning Engineering
- Date: 2026-04-26

## 1) Task 1 Summary (Git & Environment Setup)

### Repository and workflow

For Task 1, I set up the project repository and organized it using the challenge structure (`app/`, `notebooks/`, `scripts/`, `tests/`, and `reports/`). I used conventional commits and branch-based workflow, including a `setup-task` branch that was merged into `main`.

### Environment setup

I created and activated a local Python virtual environment and installed dependencies from `requirements.txt`. I also documented reproducible setup steps in `README.md` so the environment can be recreated on another machine.

### CI/CD

I added a GitHub Actions workflow in `.github/workflows/ci.yml` to run on push/PR to `main`. The workflow installs dependencies and verifies the Python environment, including an import check script (`scripts/check_env.py`).

## 2) Task 2 Approach (Data Profiling & Cleaning Outline)

### Data ingestion

For each country dataset, I used `pd.read_csv`, added a `Country` column, created a proper date column from `YEAR` and `DOY` using `pd.to_datetime(df['YEAR']*1000 + df['DOY'], format='%Y%j')`, and extracted `Month` for seasonal analysis.

### Data quality checks

I replaced NASA sentinel values (`-999`) with `NaN` before profiling. I checked for duplicate rows and duplicate `YEAR` + `DOY` entries, then computed descriptive statistics and missing-value percentages for all numeric columns.

### Cleaning decisions

I applied Z-score-based outlier screening on `T2M`, `T2M_MAX`, `T2M_MIN`, `PRECTOTCORR`, `RH2M`, `WS2M`, and `WS2M_MAX` (flagging `|Z| > 3`). For missing data, I dropped rows with more than 30% missing values and forward-filled remaining weather-variable gaps. Cleaned files were exported to `data/<country>_clean.csv` and kept out of Git tracking.

### EDA outputs per country

My EDA workflow per country includes:

- Monthly average `T2M` trend with warmest/coolest month identification
- Monthly total `PRECTOTCORR` pattern review
- Correlation heatmap and key scatter relationships (`T2M` vs `RH2M`, `T2M_RANGE` vs `WS2M`)
- Distribution analysis of precipitation (including log-scale view when skewed) and bubble chart exploration

## 3) Progress Snapshot

- Task 1 repository, environment, and CI setup is completed.
- Country EDA notebooks are prepared for Ethiopia, Kenya, Sudan, Tanzania, and Nigeria.
- Cross-country comparison notebook (`compare_countries.ipynb`) is prepared.
- Raw and cleaned country CSV files are available locally for notebook execution.

## 4) Next Steps Before Final Submission

- Execute all notebooks end-to-end and save final outputs.
- Add concise interpretation text below each major figure and table.
- Finalize cross-country vulnerability ranking and COP32 policy framing bullets.
- Convert the final Medium-style report to PDF for Tuesday submission.

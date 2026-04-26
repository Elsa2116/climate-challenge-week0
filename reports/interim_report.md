# Week 0 Interim Report (African Climate Trend Analysis)

## Candidate
- Name: Elsa
- Program Track: (DE / FA / MLE)
- Date: 2026-04-26

## 1) Task 1 Summary (Git & Environment Setup)

### Repository and workflow
- Repository created and initialized.
- Branching model documented for setup, EDA, comparison, and dashboard tasks.
- Conventional commit style adopted.

### Environment setup
- Python virtual environment configured locally.
- Dependencies captured in `requirements.txt`.
- Local run instructions documented in `README.md`.

### CI/CD
- GitHub Actions workflow added in `.github/workflows/ci.yml`.
- Workflow installs dependencies and checks Python on push/PR to `main`.

## 2) Task 2 Approach (Data Profiling & Cleaning Outline)

### Data ingestion
- Load each country CSV with `pd.read_csv`.
- Add `Country` column for traceability.
- Build `DATE` from `YEAR` and `DOY` using `pd.to_datetime(df['YEAR']*1000 + df['DOY'], format='%Y%j')`.
- Derive `Month` from `DATE`.

### Data quality checks
- Replace NASA sentinel `-999` with `NaN`.
- Count and remove duplicates.
- Compute summary statistics and missing-value percentages.
- Identify fields with >5% null values and flag interpretation risk.

### Cleaning decisions
- Outlier screening via Z-scores on core weather variables.
- Retain/cap/drop strategy documented per country with rationale.
- Drop rows where missingness >30%.
- Forward-fill remaining weather-variable gaps.
- Export cleaned files as `data/<country>_clean.csv` (kept out of git).

### EDA outputs per country
- Monthly mean temperature trend with warmest/coolest annotation.
- Monthly precipitation totals with rainy-season discussion.
- Correlation heatmap and key pairwise scatter plots.
- PRECTOTCORR histogram (log scale if skewed) and bubble chart.

## 3) Progress Snapshot
- Task 1 scaffold completed.
- Country notebooks prepared for Ethiopia, Kenya, Sudan, Tanzania, and Nigeria.
- Cross-country comparison notebook prepared.

## 4) Next Steps Before Final Submission
- Run all notebooks with real country CSVs in `data/`.
- Fill markdown interpretation cells with evidence-backed findings.
- Complete cross-country vulnerability ranking and COP32 framing bullets.
- Prepare final blog-style report and export to PDF.

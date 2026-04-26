# African Climate Trend Analysis - Week 0

This repository is structured to complete the 10 Academy Week 0 challenge on climate trend analysis for:

- Ethiopia
- Kenya
- Sudan
- Tanzania
- Nigeria

## 1) Environment Setup

### Clone and create virtual environment (Windows PowerShell)

```powershell
git clone <your-repo-url>
cd climate-challenge-week0
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install -r requirements.txt
```

### Linux / macOS

```bash
git clone <your-repo-url>
cd climate-challenge-week0
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

## 2) Suggested Branching Workflow

- `setup-task` for Task 1 (Git + CI + environment)
- `eda-ethiopia`, `eda-kenya`, `eda-sudan`, `eda-tanzania`, `eda-nigeria` for Task 2
- `compare-countries` for Task 3
- `dashboard-dev` for bonus Streamlit app

### Example conventional commits

- `init: add project scaffold and gitignore`
- `chore: set up python dependencies`
- `ci: add github actions workflow`
- `feat: add ethiopia eda notebook`
- `docs: add task progress and findings`

## 3) Repository Layout

```text
├── .vscode/
│   └── settings.json
├── .github/
│   └── workflows/
│       └── ci.yml
├── .gitignore
├── requirements.txt
├── README.md
├── src/
│   └── __init__.py
├── notebooks/
│   ├── __init__.py
│   ├── README.md
│   ├── ethiopia_eda.ipynb
│   └── compare_countries.ipynb
├── tests/
│   └── __init__.py
├── scripts/
│   ├── __init__.py
│   └── README.md
└── app/
    ├── __init__.py
    ├── main.py
    └── utils.py
```

## 4) Data Handling Rules

- Place country CSVs in `data/` locally.
- **Never commit CSV files**.
- NASA sentinel values `-999` must be converted to `NaN` before analysis.
- Build `DATE` from `YEAR` + `DOY` using:

```python
pd.to_datetime(df["YEAR"] * 1000 + df["DOY"], format="%Y%j")
```

## 5) Running Notebooks

```bash
jupyter notebook
```

Open notebooks in `notebooks/` and execute cells.

## 6) Running Streamlit Dashboard (Bonus)

```bash
streamlit run app/main.py
```

The app expects cleaned CSV files under `data/`.

## 7) CI

A GitHub Actions workflow in `.github/workflows/ci.yml` runs on push/PR to `main` and verifies:

- dependency installation from `requirements.txt`
- Python environment via `python --version`

## 8) Submission Checklist

### Interim (Sunday)

- GitHub repo link (main branch)
- Task 1 summary
- Task 2 profiling/cleaning approach outline

### Final (Tuesday)

- GitHub repo link (main branch)
- Full report (Medium blog style exported to PDF)
- Optional dashboard screenshot in `dashboard_screenshots/`

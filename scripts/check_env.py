import importlib
import sys

REQUIRED = [
    "pandas",
    "numpy",
    "matplotlib",
    "seaborn",
    "scipy",
    "streamlit",
    "plotly",
]

missing = []
for package in REQUIRED:
    try:
        importlib.import_module(package)
    except Exception:
        missing.append(package)

print(f"Python executable: {sys.executable}")
print(f"Python version: {sys.version.split()[0]}")

if missing:
    print("Missing packages:", ", ".join(missing))
    sys.exit(1)

print("Environment check passed.")

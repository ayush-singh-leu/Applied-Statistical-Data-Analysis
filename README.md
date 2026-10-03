# Applied Statistical Data Analysis

Course repository for weekly tutorials, Marimo notebooks, datasets, and supporting material.

## Repository structure

```text
notebooks/          Weekly Marimo notebooks
data/raw/           Original datasets (do not modify)
data/processed/     Cleaned or transformed datasets
materials/          Slides, worksheets, and reading material
assets/             Images and other notebook assets
student_examples/   Small examples that may be shared with students
```

## Quick start

### macOS/Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
marimo edit notebooks/week_01_template.py
```

### Windows PowerShell

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
marimo edit notebooks/week_01_template.py
```

Run a notebook as an app with:

```bash
marimo run notebooks/week_01_template.py
```

## Weekly workflow

1. Copy `notebooks/week_01_template.py` and rename it for the new week.
2. Add the week's dataset under `data/raw/` if it can be shared publicly.
3. Keep explanatory text, code, outputs, and exercises together in the notebook.
4. Commit and push the completed week to GitHub.

The full student installation and GitHub setup guide will be added separately.

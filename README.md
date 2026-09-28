# CO3117 — Individual Longitudinal Assignment

Individual learning portfolio for **CO3117 Machine Learning** (HK261): one dataset, one use case, many models.

| Item | Value |
| :---- | :---- |
| Course week at init | W05 (calendar week 39, 2026-09-24) |
| Part I deadline | **14 Oct 2026** (tag `part1-final`) |
| Midterm | 16 Oct 2026 |
| Graded parts | Part I 40/100 · Part II 60/100 |

## Design rule

Keep the **dataset source/version**, **prediction target**, **decision context**, and **held-out test population** fixed for the whole semester. Change the model or representation—not the problem.

## Use-case draft (freeze at R0)

> This section is a **draft** until catch-up + protocol freeze and tag `release-baseline` (before Course Week 6). Do not treat seeds/paths below as final until R0.

| Field | Draft decision |
| :---- | :---- |
| Dataset | UCI Human Activity Recognition Using Smartphones |
| Source | https://archive.ics.uci.edu/dataset/240/human+activity+recognition+using+smartphones |
| Target | Predict the person's **current physical activity** class from smartphone inertial measurements |
| Why this use case | Multiclass, subject-linked measurements (leakage risk is explicit), usable as static features now and as sequences later (HMM in Part II) without changing the raw source |
| Primary metric | **Macro-F1** |
| Secondary | Accuracy + confusion matrix |
| Split policy | **Subject-aware** (group by person / subject ID); no subject leakage across train and test |
| Validation | Tune on validation or CV **inside** the training population only; final test population sealed |
| Preprocessing | Fit scalers/encoders on **training data only**, then transform val/test |
| Baseline | Majority-class (and/or a simple linear baseline) kept all semester |
| Random seeds | Draft: `SEED = 42` (confirm and pin in `src/data.py` at R0) |

## Repository layout

See assignment §5. Key dashboards for the instructor:

- [PROGRESS.md](PROGRESS.md) — weekly status table
- [MODEL_LOG.md](MODEL_LOG.md) — per-model records
- [AI_USE.md](AI_USE.md) — AI disclosure
- [REFERENCES.md](REFERENCES.md) — sources actually used
- [SUBMISSION_PART1.md](SUBMISSION_PART1.md) — Part I package index

Reference implementations (e.g. ML-From-Scratch) live **outside** this repo and are read only after a first-attempt commit.

## Setup

```bash
python -m venv .venv
# Windows PowerShell:
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Ownership workflow (every ordinary week)

1. UNDERSTAND → write assumptions/objective in own words  
2. FIRST ATTEMPT → drill + core code; commit before reference/AI  
3. DISSECT → map ≥3 algorithm steps to reference `file:line`  
4. MODIFY / COMPLETE → keep first attempt in history  
5. BENCHMARK → same split/preprocess as trusted library  
6. EXPLAIN → weekly post, MODEL_LOG, exam sheet, tag  

## Current status (2026-09-24)

- [x] Repository skeleton + control files  
- [ ] Dataset download + `data.py` protocol freeze  
- [ ] W01–W04 catch-up + release diagnostic  
- [ ] Tag `release-baseline`  
- [ ] Perceptron first attempt (end of W05)  

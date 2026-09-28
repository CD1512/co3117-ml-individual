# Data directory

Raw downloads are **not** committed (see `.gitignore`: `data/raw/`, `data/processed/`).

## Dataset (frozen at tag `release-baseline`, 26 Sep 2026)

| Field | Value |
| :---- | :---- |
| Name | UCI Human Activity Recognition Using Smartphones |
| URL | https://archive.ics.uci.edu/dataset/240/human+activity+recognition+using+smartphones |
| Download date | 2026-09-25 |
| Local archive | `data/raw/UCI HAR Dataset.zip` |
| Extracted path | `data/raw/UCI HAR Dataset/` |
| SHA256 (zip) | `2045E435C955214B38145FB5FA00776C72814F01B203FEC405152DAC7D5BFEB0` |
| Features | 561 engineered inertial features per window |
| Target | activity label `{1..6}` (WALKING … LAYING) |
| Subject key | `subject_*.txt` (30 subjects) |
| Primary metric | Macro-F1 (secondary: accuracy + confusion matrix) |
| Seed | **42** |
| Split | Subject-aware via `GroupShuffleSplit`: ~20% subjects test, then ~20% of remaining subjects val; rest train |
| Preprocess | `StandardScaler` fit on **train only**, then transform val/test |

### Subjects under seed=42 (current draft)

| Split | #subjects | IDs |
| :---- | :---- | :---- |
| Train | 19 | 2,3,4,5,6,7,8,12,13,15,17,19,20,22,25,26,27,29,30 |
| Val | 5 | 1,11,14,21,23 |
| Test (sealed) | 6 | 9,10,16,18,24,28 |

## Leakage checklist

- [x] No subject appears in both train and test (asserted in `src/data.py`)
- [x] Scalers fitted on train only
- [x] Final test set sealed (no tuning on test)
- [x] Version/source recorded (URL + SHA256 + date above)

## How to re-run majority baseline

```bash
pip install -r requirements.txt
python experiments/part1_pre_midterm/run_majority_baseline.py
```

First run (2026-09-25): macro_f1 ≈ 0.053, accuracy ≈ 0.190 on sealed test.

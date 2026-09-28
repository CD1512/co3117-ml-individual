# Data directory

Raw downloads are **not** committed (see `.gitignore`: `data/raw/`, `data/processed/`).

## Planned dataset (draft until R0)

| Field | Value |
| :---- | :---- |
| Name | UCI Human Activity Recognition Using Smartphones |
| URL | https://archive.ics.uci.edu/dataset/240/human+activity+recognition+using+smartphones |
| Local layout (planned) | `data/raw/UCI_HAR_Dataset/` after download |
| Subject key | subject ID provided with the dataset (group-aware splits) |
| Target | activity label (multiclass) |
| Primary metric | Macro-F1 |
| Seed (draft) | 42 |

## Leakage checklist

- [ ] No subject appears in both train and test
- [ ] Scalers/encoders fitted on train only
- [ ] Final test set sealed (no tuning on test)
- [ ] Version/source recorded when files are downloaded

## Download (do this on data day — 25 Sep)

1. Download the official archive from UCI.
2. Extract under `data/raw/` (ignored by Git).
3. Record exact filename, date, and checksum (if available) in this file.
4. Implement loaders in `src/data.py` and freeze protocol for tag `release-baseline`.

_Status: not downloaded as of 2026-09-24 (W05 baseline)._

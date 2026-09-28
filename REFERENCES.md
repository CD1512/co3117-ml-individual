# REFERENCES.md

Cite every source actually used. Do not list unread material.

## Course and assignment

1. CO3117 Machine Learning syllabus, HK261, HCMUT.
2. CO3117 Individual Longitudinal Assignment — Two-Part Version (release W05 / calendar week 39).
3. Sample CO3117 final examination, code 504 (26 May 2026), for exam-style drill design.

## Datasets

4. UCI Machine Learning Repository — Human Activity Recognition Using Smartphones  
   https://archive.ics.uci.edu/dataset/240/human+activity+recognition+using+smartphones  
   _(version pin: SHA256 in `data/README.md`; frozen at tag `release-baseline`)_

## Code repositories (read after first attempt)

5. Erik Linder-Norén, ML-From-Scratch — https://github.com/eriklindernoren/ML-From-Scratch  
   _(sibling checkout outside this repo; do not copy into submission)_
6. David Bourgin, numpy-ml — https://github.com/ddbourgin/numpy-ml _(Part II / HMM)_
7. ProbML, pyprobml — https://github.com/probml/pyprobml _(BN/probabilistic depth)_
8. scikit-learn documentation — https://scikit-learn.org/stable/

## Textbooks / MOOC

9. Müller & Guido (2017), Introduction to Machine Learning with Python.
10. Kevin P. Murphy (2022), Probabilistic Machine Learning: An Introduction.
11. François Chollet (2021), Deep Learning with Python, 2nd ed. _(ANN intuition)_
12. Tom Mitchell (1997), Machine Learning _(decision trees, foundations)_
13. Stephen Marsland (2009), Machine Learning: An Algorithmic Perspective _(GA)_
14. Balaraman Ravindran, NPTEL Introduction to Machine Learning (IIT Madras)  
    https://nptel.ac.in/courses/106106139

## Usage log

| Date | Source | What was used for |
| :---- | :---- | :---- |
| 2026-09-24 | Assignment spec + UCI HAR page (URL only) | Repo skeleton and use-case draft |
| 2026-09-25 | UCI HAR archive (SHA256 `2045E435…BFEB0`) | Download, subject-aware split, majority baseline |
| 2026-09-26 | ML-From-Scratch `decision_tree.py` + `calculate_entropy` / `divide_on_feature` | After first-attempt commit `53a67d5`; mapping + pre-prune knobs |
| 2026-09-28 | Mitchell Ch. 1/3; Müller & Guido Ch. 2/4/5; NPTEL Weeks 0–1, 6, 7; assignment §2, §7.1, §9 | `exercises/w01-w04-corrections.md` after PDF first attempt |

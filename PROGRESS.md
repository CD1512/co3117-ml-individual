# PROGRESS.md — Instructor dashboard

One row per Course Week. Links will be filled as artifacts appear.
Do not back-date W01–W04 history; those rows point only to the release catch-up package.

| Period | Topic | Post | Drill | First evidence | Revision commit | Tag | Status |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| W01–W04 | PRE-RELEASE catch-up (Foundations + Decision Tree) | [done] [PRE_RELEASE_CATCHUP.md](docs/pre-release/PRE_RELEASE_CATCHUP.md) | [done] [release-baseline-w01-w04.pdf](exercises/release-baseline-w01-w04.pdf) | handwritten scan 25/09/2026 (`4ab63ec`); gini/split `53a67d5` | after-reference `490e7b4` + MODEL_LOG mapping | `release-baseline` | PRE-RELEASE (R0 frozen) |
| W05 | Perceptron / Delta + repository onboarding | [done] [w05-perceptron-delta.md](docs/weekly/w05-perceptron-delta.md) | [done] [w05-first-attempt.pdf](exercises/w05-first-attempt.pdf) + [w05-corrections.md](exercises/w05-corrections.md) | handwritten 28/09/2026 + first code `9660873` | OvR + sklearn benchmark + MODEL_LOG `ab30fea` | `w05` | DONE |
| W06 | Artificial Neural Networks / backpropagation | TBD | TBD | TBD | TBD | `w06` | PLANNED |
| W07 | Naive Bayes + Genetic Algorithm (+ BN closeout) | TBD | TBD | TBD | TBD | `w07` | PLANNED |
| W08 | MIDTERM (16 Oct 2026) — no new major implementation | compact midterm entry | timed rehearsal | Part I already frozen | midterm reflection (Part II) | `w08-midterm` | MIDTERM |
| W09–W15 | Part II models (HMM, SVM, PCA/LDA, ensembles, logistic/CRF) | weekly posts | weekly drills | pre-ref commits | post-ref commits | `w09`…`w15`, `part2-final` | PART II |

## Graded submission tags

| Tag | Target date | Status |
| :---- | :---- | :---- |
| `part1-final` | 14 Oct 2026 | NOT YET |
| `part2-final` | two calendar days before official final exam | NOT YET |

## Notes

- Prospective two-state commit rule (first attempt → post-reference) starts from W05.
- R0 gate: skeleton + catch-up + frozen protocol + tag `release-baseline` — done. W05 Perceptron closed with tag `w05`.
- This tree was rebuilt on 28 Sep 2026 as a clean submission-shaped history (no back-dating). The handwritten PDF remains dated 25/09/2026.

# AI_USE.md — disclosure log

AI may be used only after a first-attempt commit (or after the release-day handwritten baseline for W01–W04 catch-up). Record every AI-assisted episode below.

Required fields per entry (assignment §12.5):

| Field | Required entry |
| :---- | :---- |
| Week/date | W__ / YYYY-MM-DD |
| Learning question | Precise concept/problem |
| Pre-AI evidence | Commit hash or handwritten first-attempt artifact |
| AI tool | Tool/model used |
| Prompt purpose | Socratic hint, counterexample, debugging question, quiz, etc. |
| Hint/question received | Concise summary; do not paste a full generated solution |
| Verification source | CO3117 note, textbook, NPTEL, repository/code reference |
| What changed | Specific misconception, derivation, test, or code decision corrected |
| Closed-book reproduction | Yes / Not yet; link delayed-retrieval artifact when available |

---

## Entries

| Field | Entry |
| :---- | :---- |
| Week/date | W05 / 2026-09-26 |
| Learning question | After own gini/split, what does ML-From-Scratch do differently, and what is a non-copy modification? |
| Pre-AI evidence | commit `53a67d5` `src/from_scratch/impurity_split_first_attempt.py` |
| AI tool | Cursor agent |
| Prompt purpose | Dissect reference + add pre-prune knobs; not a first-attempt rewrite |
| Hint/question received | Map impurity / gain / recurse to file:line; keep midpoints; add min_samples/min_gain |
| Verification source | ML-From-Scratch `decision_tree.py` `_build_tree`, `_calculate_information_gain`; `calculate_entropy`; `divide_on_feature` |
| What changed | New file `impurity_split_after_reference.py`; mapping recorded in MODEL_LOG (Decision Tree section); sklearn stop vs prune experiment |
| Closed-book reproduction | Not yet — retrieve gini + gain formula without notes within 72h |

_Repo onboarding (skeleton) is infrastructure, not a Depth-A first attempt._

| Field | Entry |
| :---- | :---- |
| Week/date | W05 / 2026-09-28 |
| Learning question | After the handwritten W01–W04 PDF, what was missing or imprecise, and which course sources confirm the correction? |
| Pre-AI evidence | `exercises/release-baseline-w01-w04.pdf` (commit `4ab63ec`) |
| AI tool | Cursor agent |
| Prompt purpose | Check first attempt vs §7.1; structure Markdown corrections with citations (not a new first attempt) |
| Hint/question received | Per-item: what the PDF said, gap, correction, source; do not edit the PDF |
| Verification source | Mitchell Ch. 1/3; Müller & Guido Ch. 2/4/5; NPTEL Weeks 0–1, 6, 7; assignment §2, §7.1, §9 |
| What changed | Wrote `exercises/w01-w04-corrections.md` to match the PDF (not a longer typed draft) |
| Closed-book reproduction | Not yet — retrieve leakage rule + weighted information-gain formula without notes |

| Field | Entry |
| :---- | :---- |
| Week/date | W05 / 2026-09-28 |
| Learning question | After the W05 PDF + own perceptron, what was wrong or missing vs Mitchell/NPTEL, and how should the code be checked without erasing the first attempt? |
| Pre-AI evidence | commit `9660873` (`exercises/w05-first-attempt.pdf`, `src/from_scratch/perceptron_first_attempt.py`) |
| AI tool | Cursor agent |
| Prompt purpose | Check corrections vs §7.1; list first-attempt code bugs; re-check the student rewrite of `perceptron_after_check.py` |
| Hint/question received | Cite Mitchell §4.4.1–4.4.3 by book title; PDF `b += ηyx` vs code `b += ηy`; `weight` vs `weights` and `learing_rate`; labels `{+1,−1}`; do not edit first-attempt files; on rewrite: `fit` does not reset `bias` |
| Verification source | Mitchell (1997) Ch. 4 §4.4.1–§4.4.3; NPTEL Week 4 perceptron lecture; assignment §4, §7.1; own first-attempt `fit` loop |
| What changed | Filled `exercises/w05-corrections.md` (bias update without x; Mitchell §4.4.1–§4.4.3 cites). Student rewrote `perceptron_after_check.py` (spelling `learning_rate`, one `weights` vector, `±1` check, reset `bias` in `fit`). First-attempt files unchanged |
| Closed-book reproduction | Not yet — retrieve perceptron vs delta (thresholded vs linear output) without notes |

| Field | Entry |
| :---- | :---- |
| Week/date | W05 / 2026-09-28 |
| Learning question | How can a binary Rosenblatt Perceptron be evaluated fairly on 6-class HAR under the frozen protocol, and how should metrics.csv stay consistent with earlier rows? |
| Pre-AI evidence | commit `9660873`; student-authored `src/from_scratch/perceptron_ovr.py` and first draft of `run_perceptron_benchmark.py` |
| AI tool | Cursor agent |
| Prompt purpose | Socratic how-to for OvR; code review; debugging CSV schema (not writing the OvR model from scratch) |
| Hint/question received | Use one-vs-rest with `decision_function` + argmax; same `load_protocol_split()` / seed 42 / Macro-F1; append `week,model,split,macro_f1,accuracy,notes` like the DT script (do not invent a metric/value schema) |
| Verification source | assignment §4–§5, §9 (common protocol); own `run_dt_stop_vs_prune.py`; sklearn `Perceptron` docs; sealed-test numbers in `results/perceptron_benchmark.json` |
| What changed | Student kept OvR logic; benchmark script aligned to existing CSV columns; labeled confusion matrix in JSON; ran compare own OvR (Macro-F1 ≈ 0.836) vs sklearn (≈ 0.862). Affected: `perceptron_ovr.py`, `run_perceptron_benchmark.py`, `results/perceptron_benchmark.json`, `results/metrics.csv` |
| Closed-book reproduction | Not yet — explain OvR score argmax and why labels must be `{+1,−1}` without notes |

| Field | Entry |
| :---- | :---- |
| Week/date | W05 / 2026-09-29 |
| Learning question | What must the W05 weekly post contain (A–H), and does the draft match the repo numbers without claiming missing plots? |
| Pre-AI evidence | commit `9660873`; student draft `docs/weekly/w05-perceptron-delta.md` |
| AI tool | Cursor agent |
| Prompt purpose | Structure outline for A–H; review length/facts (not ghostwriting the post or exam capsule) |
| Hint/question received | 350–700 words; one experiment question; cite `9660873` and `perceptron_benchmark.json`; Macro-F1 primary; do not invent a 2-D figure; strip decorative bold/backticks if desired |
| Verification source | assignment §6 weekly post table; own post draft vs `results/perceptron_benchmark.json` / `perceptron_first_attempt.py` line refs |
| What changed | Student authored the post A–H; AI only outlined and fact-checked. Affected: `docs/weekly/w05-perceptron-delta.md` |
| Closed-book reproduction | Not yet — write F (perceptron vs delta) from memory without the post |

| Field | Entry |
| :---- | :---- |
| Week/date | W05 / 2026-09-29 |
| Learning question | After the benchmark and post, which dashboard fields must be updated so the instructor can verify W05 in under two minutes? |
| Pre-AI evidence | commit `9660873`; `results/perceptron_benchmark.json`; student post `w05-perceptron-delta.md` |
| AI tool | Cursor agent |
| Prompt purpose | Presentation / dashboard fill from existing results (not new model code) |
| Hint/question received | Replace MODEL_LOG TBD with sealed-test Macro-F1/accuracy; link post/PDF/corrections in PROGRESS and SUBMISSION_PART1; leave tag `w05` pending until review+theory commits |
| Verification source | assignment §5 PROGRESS / §9.1 MODEL_LOG / §10 checklist; numbers from `perceptron_benchmark.json` |
| What changed | Filled Perceptron metrics and experiment pointers in `MODEL_LOG.md`; marked W05 links in `PROGRESS.md`, `SUBMISSION_PART1.md`, `docs/index.md`, `docs/weekly/README.md`, `README.md`. Tag `w05` not created yet |
| Closed-book reproduction | Yes for the two Macro-F1 numbers (0.836 vs 0.862) — can state without opening the JSON |

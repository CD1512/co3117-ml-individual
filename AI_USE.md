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

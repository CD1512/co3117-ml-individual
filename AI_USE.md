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

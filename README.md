# AI Evaluation Portfolio — Datshin

A collection of 12 Python tools for evidence verification, numerical validation, annotation quality analysis, retrieval evaluation, and agent trace auditing.

Each project includes sample data, automated tests, JSON outputs, and documentation.

**Python 3.10+ • Standard library only • No API keys required**

## Quick start

Download or clone this repository, open a terminal in its main folder, and run:

```sh
python run_all.py
```

Use `python3` on macOS/Linux if needed. Each project can also run independently using the instructions in its README.

## Technical scope

The tools apply deterministic rules and metrics to supplied data and recorded outputs. They use synthetic sample datasets and run locally without calling or training an LLM.

## Projects

| Folder | Purpose |
|---|---|
| [Evidence Span Checker](01-evidence-span-checker/README.md) | Check whether a cited quotation exists in the cited source. |
| [Numeric Answer Checker](02-numeric-answer-checker/README.md) | Compare a reported quantity against a reference after unit conversion. |
| [Delivery Reconciler](03-delivery-reconciler/README.md) | Compare ordered and delivered mass by zone and bar diameter. |
| [Revision Conflict Detector](04-revision-conflict-detector/README.md) | Find field changes between two structured document revisions. |
| [Annotation Agreement Calculator](05-annotation-agreement/README.md) | Calculate raw agreement and Cohen kappa for two annotators. |
| [Pairwise Preference Report](06-pairwise-preference-report/README.md) | Summarize human A/B preferences, ties, and invalid votes. |
| [Dataset Leakage Check](07-dataset-leakage-check/README.md) | Find normalized exact duplicates shared by train and evaluation sets. |
| [Agent Trace Auditor](08-agent-trace-auditor/README.md) | Flag unapproved actions, repeated failed calls, and budget overruns in recorded agent traces. |
| [Structured Output Validator](09-json-output-validator/README.md) | Check flat JSON responses for required fields, field types, and unexpected keys. |
| [Retrieval Ranking Evaluator](10-retrieval-ranking-evaluator/README.md) | Measure precision, recall, and reciprocal rank for retrieved document IDs. |
| [Evaluation Regression Gate](11-evaluation-regression-gate/README.md) | Compare baseline and candidate pass/fail results on the same test IDs. |
| [Human Review Queue](12-human-review-queue/README.md) | Rank evaluation cases using explicit severity and confidence rules. |

## Data and scope

The projects use synthetic sample data and deterministic Python checks
to demonstrate evaluation workflows. Each project documents its inputs,
outputs, tests, and technical limitations.

## Documentation

- Browse the project folders for individual READMEs and examples.
- Run `python run_all.py` to execute the demos and tests.
- See `VALIDATION.md` for recorded test results.

ext contribution.

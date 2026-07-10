# Unique Prototype Algorithm

## Algorithm

**McCallumMinimalNlpTraceEngine** (`P040-Mccallum-Nlp`)

## Professor Alignment

- Professor: Andrew McCallum
- Research area: ML, NLP, information extraction (CRFs), structured prediction
- Focus terms: NLP, information extraction, CRFs, structured prediction

## Core Mechanism

This prototype prioritizes unsupported claims and citation mismatches for advisor-domain literature audits.

## Decision Rule

Rank seed cases by language-specific priority score with McCallum-aligned focus term 'NLP'.

## What The Code Adds

- A unique algorithm spec in `src/proposed_method.py`.
- A scoring function for the repo's `language` data schema.
- A ranked list of cases that should be reviewed, repaired, reproduced, or expanded first.
- Integration into `src/value_add.py`, so demo output includes the proposed method.

## Honest Status

This is a runnable algorithmic prototype. It is not a validated contribution to Andrew McCallum's published work until the seed data is replaced with real public/lab-relevant data and the resulting claims are evaluated.

## Run

```bash
python src/proposed_method.py
python src/value_add.py --write-report reports/demo_results.json
python -m unittest discover -s tests
```

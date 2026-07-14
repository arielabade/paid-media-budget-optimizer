# Paid Media Budget Optimizer

From campaign metrics to budget decisions.

## What it is

A small transparent optimizer that scores campaigns from CPA, ROAS, volume and stability signals, then redistributes a fixed budget.

## Source origin

The audited repositories contained a Google keyword generator and roadmap references to Meta Ads, Google Ads, CAC and conversion tracking. They did not contain a mature budget optimizer, so this repository includes a minimal prototype with synthetic data.

## Run

```bash
python src/paid_media_budget_optimizer/optimizer.py data/sample_campaigns.csv --budget 10000
python -m pytest
```

## Limitations

This is a rule-based prototype, not a statistical attribution model or media mix model.

## Part of a larger portfolio

- Previous layer: `marketing-analytics-portfolio`
- Next layer: business action
- Portfolio overview: `arielabade`

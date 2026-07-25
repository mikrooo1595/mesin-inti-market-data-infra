# Market Data Engineering & Anti-Overfitting Research Infrastructure

**Author:** Iqbal Muhammad Yasin ([ORCID: 0009-0007-2277-6917](https://orcid.org/0009-0007-2277-6917))

> ### ⚠️ Disclaimer
> This repository documents **data engineering infrastructure and research
> methodology only**. It is **not financial advice**, **not a trading
> signal or recommendation**, comes with **no profit promise**, and does
> **not manage funds**. The system described here is **NO-ORDER**: it does
> not place, route, or execute any trade in any market. Nothing in this
> repository should be used as the basis for a financial decision.

---

## What this is

A documented, auditable approach to building market-data pipelines and
research validation processes that are structurally resistant to
self-deception (look-ahead leakage, overfitting, dirty data) — the kind of
discipline quantitative research teams need, presented as engineering
methodology rather than as a black-box "system."

Full write-up: [`METHODOLOGY.md`](METHODOLOGY.md)
Data contract shape (schema only, no real data): [`DATA_CONTRACT_EXAMPLE.md`](DATA_CONTRACT_EXAMPLE.md) · [`example_leg_record.SYNTHETIC.json`](example_leg_record.SYNTHETIC.json)
Unfamiliar with a term? See [`GLOSSARY.md`](GLOSSARY.md)

## Why this exists

Most trading-adjacent products are sold on unverifiable outcomes. This
repository takes the opposite approach: it documents the **process** —
the quarantine rules, the validation protocol, the data contracts — so
that the discipline itself can be evaluated, independent of any specific
market outcome.

## What's inside vs. what's kept private

| Public here | Private (by design) |
|---|---|
| Pipeline stage names & data flow | Pipeline source code |
| Feature taxonomy (24 measured features, 4 groups) | Feature weighting / thresholds |
| Validation protocol description (walk-forward, Purged CPCV) | Actual validation results / performance figures |
| Anti-leakage / anti-overfit design principles | Signal generation logic |

This mirrors how the methodology itself works: the *discipline* is the
product, not a black box of numbers.

## UI mockup (synthetic data)

`mockup/MOCKUP_E8_DEPAN.SYNTHETIC.html` and
`mockup/MOCKUP_E8_BELAKANG.SYNTHETIC.html` are static, self-contained HTML
files that show the **layout and information design** of the monitoring
dashboard used internally — panel structure, tab organization, how a
signal's context is surfaced, etc.

Every number, candidate name, and label on these two pages is **fabricated
for the purpose of the mockup**. They do not correspond to any real
signal, backtest result, or trading outcome, and no real strategy name
appears anywhere in the file. This mirrors the public/private split above:
the *shape* of the interface is shown; the actual validation numbers and
signal logic that would populate it are not.

Open either file directly in a browser (double-click, or drag into a tab)
to view it — no server or build step needed. See "View it live" below for
a hosted version.

`demo/demo_synthetic.py` runs the validation harness's *interface*
(`Judge.duel(...)`, purge/embargo, CPCV fold construction) against 100%
fabricated data with a made-up, deliberately weak signal. It imports
`tribunal`, which is the private core engine and is **not included** in
this repository — so the script will raise `ModuleNotFoundError` if run
as-is. That's intentional: the file documents the *interface shape*, not
a runnable product.

## Verify this repository hasn't been altered

```bash
python generate_manifest.py   # (re)computes sha256 for every file here
python verify_manifest.py     # checks current files against manifest.sha256
```

## Related work

- 3D/CT asset pipeline (separate line of work — a different specialization
  entirely): [ct-skull-quad-quality-reports](https://github.com/mikrooo1595/ct-skull-quad-quality-reports)

## Verifiable credentials

Independent, third-party-hosted evidence of prior structured, documented
work — useful for cross-checking that the documentation discipline shown
in this repository is consistent across projects:

- **ORCID** (researcher identity): [0009-0007-2277-6917](https://orcid.org/0009-0007-2277-6917)
- **Zenodo** (archived, DOI-citable dataset record): *CT-Derived Human Skull
  Mesh Pack: Quad-Retopologized, Quality-Measured (A0101–A0105)* — add the
  DOI link here
- **Hugging Face** (dataset card): [mikrooo1595/ct-skull-quad-retopo-pack](https://huggingface.co/datasets/mikrooo1595/ct-skull-quad-retopo-pack)
- **Marketplace listings** (independent commercial track record):
  [CGTrader](https://www.cgtrader.com/3d-models/character/human-anatomy/human-skull-3d-model-anatomically-accurate) ·
  [Fab](https://www.fab.com/listings/5570c50f-d58a-4553-ac21-b312a181e50c)

## Contact

For scoped discussion of validation results, methodology deep-dives, or
engineering engagements — under a signed NDA where appropriate — contact
details are on the author's ORCID profile linked above.

## License

METHODOLOGY.md and scripts in this repo: MIT License. This license covers
the *documentation and verification tooling only* — it does not extend to
any pipeline source code, which is not included in this repository.

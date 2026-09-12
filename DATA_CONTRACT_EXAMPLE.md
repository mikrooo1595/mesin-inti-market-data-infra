# Example Data Contract — `legs` Stage Schema

**Purpose of this document:** to make the "24 measured features across 4
groups" concept from `METHODOLOGY.md` concrete and inspectable, by showing
the *shape* of the data contract — column names, types, and what each one
represents.

**This is a structural example only.** No real market data, no real price
history, no actual computed values are included anywhere in this file.

## Identity / join keys (present in every pipeline stage)

| Column | Type | Description |
|---|---|---|
| `uid` | string | Join key, identical format across all traded instruments |
| `instrument` | string | Instrument identifier (asset-agnostic) |
| `leg_start_ts` | timestamp (UTC) | Leg start time |
| `leg_end_ts` | timestamp (UTC) | Leg end time |

## Group: Structure

| Column | Type | Description |
|---|---|---|
| `leg_size` | float | Price displacement over the leg |
| `leg_duration_s` | int | Duration in seconds |
| `leg_velocity` | float | size / duration |
| `atr_ratio` | float | Leg size relative to Average True Range |

## Group: Money flow

| Column | Type | Description |
|---|---|---|
| `net_usd_per_min` | float | Net signed dollar flow per minute |
| `vpin` | float | Volume-Synchronized Probability of Informed Trading |
| `kyle_lambda` | float | Kyle's lambda (price impact per unit volume) |
| `ofi` | float | Order-flow imbalance |
| `benford_dev` | float | Deviation from Benford's Law conformance |

## Group: Psychology

| Column | Type | Description |
|---|---|---|
| `whale_pct` | float | Share of volume from large-size participants |
| `cvd` | float | Cumulative volume delta |
| `climax_flag` | bool | Climax-pattern detector output |
| `absorption_score` | float | Absorption-at-level score |

## Group: Context

| Column | Type | Description |
|---|---|---|
| `frac_diff` | float | Fractionally-differenced price series value |
| `hmm_regime` | int | Hidden Markov Model regime label |
| `hour_of_day` | int | Hour bucket (0–23, exchange-local) |
| `calendar_flag` | bool | Scheduled macro/release-calendar window flag |

## What is intentionally NOT shown

- The full feature set. This contract publishes 17 of the 24 measured
  features. The remaining seven are withheld deliberately.
- Actual numeric values (this document is schema-only)
- Feature weights, combination logic, or thresholds
- The outcome-based columns (MFE/MAE) that are quarantined from being used
  as predictors per the forensic-feature-quarantine rule in `METHODOLOGY.md`

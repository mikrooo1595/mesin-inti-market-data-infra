# Glossary

Terms used in `METHODOLOGY.md` and `DATA_CONTRACT_EXAMPLE.md`, explained
for readers who aren't already familiar with market microstructure or
quantitative research vocabulary. General reference definitions — not
proprietary to this project.

**VPIN (Volume-Synchronized Probability of Informed Trading)** — a measure
estimating the likelihood that trading volume in a window reflects
informed (rather than noise) trading activity.

**Kyle's λ (lambda)** — a market-microstructure measure of price impact:
how much price moves per unit of trading volume. Higher λ implies a more
illiquid or thin market.

**OFI (Order-Flow Imbalance)** — the net difference between buy-side and
sell-side order flow over a window.

**CVD (Cumulative Volume Delta)** — the running total of buy volume minus
sell volume over time.

**Benford's Law conformance** — a statistical check on whether the leading
digits of a dataset follow the distribution expected of naturally-occurring
numerical data; deviations can flag anomalous or manipulated data.

**Fractional differencing** — a time-series transformation that makes a
price series more stationary (suitable for many statistical models) while
preserving more memory/structure than standard (integer-order) differencing.

**HMM (Hidden Markov Model) regime** — a statistical model used to label
which unobserved "regime" (e.g., trending, ranging, volatile) a market is
likely in at a given time.

**Walk-forward validation** — an out-of-sample testing approach where a
model is trained on one time window and tested on the *next*, rolling
forward through time, rather than testing on data that overlaps the
training window.

**Purged Cross-Validation / Combinatorial Purged CV (CPCV)** — a
cross-validation method (from Marcos López de Prado's work on financial
machine learning) that removes ("purges") training samples whose
information overlaps with the test window, and adds an embargo period, to
prevent leakage between training and test sets in time-series data.

**MFE / MAE (Maximum Favorable / Adverse Excursion)** — the best and worst
unrealized price movement a hypothetical position would have experienced
during a trade. Using these as model *inputs* (rather than for later
analysis) creates look-ahead leakage — which is why this project
structurally quarantines them from the feature set.

**Look-ahead leakage** — when information that would not actually have
been available at decision time is (accidentally or otherwise) used to
train or evaluate a model, making backtest results unrealistically good.

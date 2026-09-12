# Gates

A gate that cannot turn red is decoration. Every gate below has a defined failure condition, and each one has been — or is scheduled to be — tested by deliberate sabotage.

## Exit-code contract

```
0 = PASS            the check passed
1 = RED             the check failed — the number is reported
2 = CANNOT CHECK    the check could not be performed, and the report states
                    exactly what is needed in order to perform it
```

**Code 2 is not code 0.** A check that could not run has not passed. Reporting "unknown" as "safe" is the most common quiet failure in data work, and this contract exists to make it impossible here.

---

## G1 · CAUSAL

**Checks:** that only settled information is used. Periods must be closed before they are computed. Entry is taken at t+1, never at t. All timestamps are UTC, with no local-time conversion anywhere in the path.

**Turns RED when:** any value that only becomes available in the future is present in a present-time calculation.

**Why it exists:** this is the single most common way a backtest lies. It does not announce itself — the model simply looks excellent and then fails in production.

---

## G2 · ZONE

**Checks:** that predictors and outcome-forensics are held in separate namespaces from the moment of creation, and that the intersection of the two sets is asserted empty at every stage.

**Turns RED when:** a feature is found to be derived, directly or indirectly, from the label it is meant to predict.

**Why it exists:** leakage of this kind is usually accidental and is nearly invisible in a feature list. Separating the two zones at birth, rather than auditing them later, makes the failure structural instead of a matter of vigilance.

---

## G3 · FROZEN

**Checks:** that all cut-offs and scaling parameters were established in-sample, then frozen and fingerprinted. Any change produces a new version and requires re-judging, rather than editing the existing one.

**Turns RED when:** a parameter's fingerprint does not match the frozen reference, or a parameter was adjusted after out-of-sample results were seen.

---

## G4 · JUDGE

**Checks:** performance under purged cross-validation with an embargo period, executed by a judge that is structurally separate from the engine being judged. **Includes a label-shuffle test.**

**Turns RED when:** the model still performs above chance after the labels have been shuffled.

**Why the shuffle matters:** if a result survives having its answers randomised, the result is measuring the shape of the evaluation, not the shape of the data. This is the fastest way to kill a strategy, and it is the test most often skipped.

**The judge is not the knife.** The component that evaluates never modifies. Its only write is its own report.

---

## G5 · COST

**Checks:** that slippage, fees, and fill feasibility are applied at realistic levels, and that the fill was actually achievable at the stated price and size.

**Turns RED when:** the edge does not survive realistic costs.

---

## G6 · REPEAT

**Checks:** that running twice with a fixed seed produces byte-identical fingerprints.

**Turns RED when:** two runs produce two different results.

**Why it exists:** a result that cannot be reproduced cannot be audited, whatever its value. Reproducibility is a precondition here, not a bonus.

---

## Gate design rules

1. **Every gate must be sabotageable.** If no deliberate break can turn it red, it is not a gate.
2. **Failing artifacts are still written**, marked for inspection and never promoted. Deleting the evidence of a failure removes the ability to diagnose it.
3. **Guards read; they never repair.** A guard that fixes what it finds destroys the record of what was wrong.
4. **Thresholds carry their source.** Every threshold records the file and line that set it, as data — never as a number buried in code.

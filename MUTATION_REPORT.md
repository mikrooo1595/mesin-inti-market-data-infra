# Sabotage Campaign — 20 mutants, 17 caught

**Date:** 26 August 2026
**System under test:** AB APPS ("SATU RUMAH") — a sibling system built under the same house discipline as MESIN INTI
**Where it ran:** a **copy**, never the live house. 0 bytes of production code were touched.
**Baseline before mutants:** 396 tests green, 3 skipped

> **Scope, stated plainly:** this campaign was run on AB APPS, **not on MESIN INTI**. The same campaign on the core engine is declared work, not completed work. I am not claiming a number I did not measure.

---

## Score

| | |
|---|---|
| Sabotages applied | **20** |
| **Caught** | **17 (85%)** |
| **Survived** | **3** |

By layer: core 6→5 · drawer 9→7 · window 3→3 · logbook 2→2

---

## Method

Each mutant was a single, unique text substitution applied at a point that **matters** — a threshold comparison, a fence, a secret boundary, a hash chain link. After each substitution:

1. Run the test suite
2. Record which guard raised the alarm first, and how many seconds it took
3. Restore the file
4. Confirm the fingerprint matches the original

Sabotage was always performed on a copy — *minimise blast radius*, the standard chaos-engineering principle.

---

## The 17 that were caught

Representative examples. Each names the guard that caught it.

| # | What the sabotage did | Guard that caught it | sec |
|---|---|---|---|
| 3 | Made an EMPTY-ingredients verdict stop blocking the live run | `test_cek_bahan::test_10_tiga_vonis_berbeda` | 2.1 |
| 6 | Made an invented lamp name acceptable | `test_nama_lampu::test_10_nama_karangan_DITOLAK` | 9.4 |
| 8 | Let an internal kitchen term leak into the display block | `test_jembatan_kokpit::test_1_ambang_TIDAK_BOLEH_ada_di_tampil` | 10.3 |
| 9 | Made a mandatory column optional | `test_laci_koin::test_jembatan_gagal_cepat_kolom_hilang` | 9.6 |
| **10** | **Removed write-once protection** | `test_io_atomik::test_write_once_menolak_tulis_ulang` | 6.2 |
| **11** | **Made the writer blind to write corruption** | `test_io_atomik::test_korupsi_baca_balik_masuk_karantina` | 6.6 |
| 12 | Allowed duplicate ledger entries | `test_buku_besar::test_id_deterministik_dan_kembar_ditolak` | 2.3 |
| **13** | **Broke the hash chain — every entry became GENESIS** | `test_buku_besar::test_rantai_tersambung_dan_verifikasi_hijau` | 3.3 |
| **15** | **Made a FAILED gate still exit 0** | `test_cek_determinisme::test_mesin_mati_total_membuat_g0_merah` | 3.1 |
| **16** | **Allowed the risk disclaimer to vanish from the board** | `test_papan::test_sabotase_penafian_hilang_build_gagal` | 8.5 |
| **17** | **Let a forbidden term through to the board** | `test_papan::test_kata_haram_menghentikan_build` | 8.3 |
| 19 | Made the logbook accept an invented stage name | `test_catatan::test_16_catat_aman_tidak_pernah_melempar` | 1.5 |
| 20 | Made the logbook accept FAILED with no stated reason | `test_catatan::test_4_GAGAL_tanpa_sebab_DITOLAK` | 1.9 |

Mutants 16 and 17 are the two board guards shown in the main README. **Both caught their sabotage.**

---

## The three that survived

These are published, not deleted. Specimens are kept as diffs with fingerprints nailed down.

### Survivor 1 — threshold boundary · *near-equivalent*

**What it did:** shifted a comparison by one boundary case.
**Why the guard was blind:** at the exact boundary the verdict is unchanged; only the wording of the stated reason differs. No test exercised the exact boundary value.
**Fix proposed:** a test that pins the boundary wording. **Priority: low.**

### Survivor 2 — one-minute gap · *a real blind spot*

**What it did:** made a one-minute gap in a time series count as intact.
**Why the guard was blind:** tests used gaps of 3 and 30 minutes. The 1–2 minute range was never exercised.
**Why this one matters:** a single missing minute in the middle of a series would have been declared whole. **This is the smallest gap that should have been caught.**
**Fix proposed:** a test at a gap of exactly 1. **Priority: real.**

### Survivor 3 — whitespace check · *equivalent mutant*

**What it did:** removed a whitespace check on a name.
**Why the guard was blind:** it is redundant. A character-by-character check below it already rejects whitespace, so the behaviour is unchanged.
**Fix proposed:** none needed. Recorded as deliberate double-checking.

**Specimen fingerprints** (sha12, nailed at the time of the report):

```
mutant_04.diff   10fa48996de9
mutant_05.diff   5ccbda9fd66b
mutant_14.diff   f07cdc153339
```

---

## Honest notes — written at the time, kept unchanged

> **"The 20 mutants were chosen by hand at meaningful points, not at random; this score is therefore not a full mutation score."**

> **"Mutant 14 is an equivalent mutant — counted as survived as it is, not discarded to make the score look better."**

> **"The proposed tests are not written in this report — awaiting a decision."**

Both of the first two sentences lower the number. Both stayed in.

A note on why the mutants were hand-picked rather than generated: automated mutation tools produce a large share of incompetent or equivalent mutants, which inflates a score without testing anything meaningful. Twenty hand-placed mutants at load-bearing points say more than a thousand random ones — but the resulting figure is **not** comparable to a published mutation score, and is not presented as one.

---

## What was deliberately not touched

Live-execution modules and the kitchen itself were excluded from the campaign by rule. Sabotaging a live path is not a test; it is an incident.

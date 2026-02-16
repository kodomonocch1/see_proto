<img width="1024" height="586" alt="Gemini_Generated_Image_f2hennf2hennf2he" src="https://github.com/user-attachments/assets/aa2d0fac-395f-4a12-8835-9ad565ef05c9" />
### SEE — Searchable JSON Compression (Semantic Entropy Encoding)

[![Release](https://img.shields.io/github/v/release/kodomonocch1/see_proto)](https://github.com/kodomonocch1/see_proto/releases)
[![Discussions](https://img.shields.io/github/discussions/kodomonocch1/see_proto?label=Q%26A%20%2F%20Repro)](https://github.com/kodomonocch1/see_proto/discussions)

**combined ≈ 7.7% (Zstd 13.7%) • lookup p50 ≈ 0.085 ms • skip ≈ 99%**

> **Why it matters**
> SEE reduces both the **data tax** (storage/egress) and the **CPU tax** (decompress/parse) by keeping JSON **searchable while compressed**.
> For many workloads, **searchability + low I/O + random access** yields better **TCO/ROI** than Zstd-only.

<p>
  <a href="https://github.com/kodomonocch1/see_proto/releases"><b>① Download (Latest Release)</b></a> ・
  <a href="#try-in-10-min"><b>② Try in 10 minutes</b></a> ・
  <a href="#dd-pack"><b>③ DD Pack (Repro + Proof)</b></a>
</p>

<p>
  <a href="https://github.com/kodomonocch1/see_proto/discussions/categories/q-a"><b>🗨️ Start a Discussion (Q&A)</b></a>
  &nbsp;•&nbsp;
  <a href="https://github.com/kodomonocch1/see_proto/discussions/categories/benchmarks-repro"><b>📊 Benchmarks & Repro</b></a>
</p>

> **Enterprise / NDA inquiry** → <a href="https://docs.google.com/forms/d/e/1FAIpQLScV2Ti592K3Za2r_WLUd0E6xSvCEVnlEOxYd6OGgbpJm0ADlg/viewform?usp=header"><b>Private contact form</b></a>  
> *Under NDA: full DD pack available. Please provide a **company email** (no confidential data required).*

---

## What is SEE?

* **Schema-aware JSON compression:** combines *structure × delta × Zstd (+ Bloom / Skip)* to stay **searchable while compressed**, with **page-level random access**.
* **Design trade-off:** targets **low I/O & low latency (ms)** and **~99% skip rate** (not “smallest bytes at any cost”).

---

## Key metrics (latest)

* Combined size: **≈ 7.7% of raw** (Zstd: **≈ 13.7%**)
* Lookup latency (ms): **p50 ≈ 0.085** (present/absent), p95 ≈ **0.09**, p99 ≈ **~0.10–0.14**
* Skip ratio: **present ≈ 0.994 / absent ≈ 0.997**, Bloom density ≈ **0.376**
* Repro/robustness: **3 datasets** + **query suite** + **verify/corpus/fuzz smoke** + **integration (no MSVC)** + **ROI embedding** (all PASS)

<img width="594" height="835" alt="SEE OnePager (2026-02-16)" src="https://github.com/user-attachments/assets/69e99d10-5095-47f1-b2a9-1d48871bf631" />

**OnePager PDF (latest):** included in the latest Release assets.

---

## ROI quick math

`Savings/TB = (1 − ratio_see[combined]) × Price_per_GB × 1000`  
Example: ratio=0.077, $0.05/GB → **≈$46/TB**, $0.25/GB → **≈$231/TB**

---

## 🔧 Try in 10 minutes <a id="try-in-10-min"></a>

### Option A — From Release DEMO ZIP (recommended)

1) Download the latest **DEMO ZIP** from Releases  
2) Unzip, then run:

```bash
python quick_demo.py
````

Prints compression ratio, skip rate, Bloom density, and lookup latency (p50/p95/p99).

### Option B — From pip

```bash
pip install see_proto
python -m see_proto.samples.quick_demo
```

---

## Why SEE vs Zstd-only?

* **Zstd-only** can be smaller, but is not **searchable**; you pay **I/O + CPU** to decompress and parse JSON.
* **SEE** keeps data **searchable while compressed** with **page-level skipping**, enabling **ms lookups** and reducing **total cost** for I/O/CPU-bound pipelines.

---

## DD Pack (Repro + Proof) <a id="dd-pack"></a>

**Purpose:** technical diligence package for evaluators (reproducible artifacts + proof logs).
**Not a 10-minute demo** (the demo is the DEMO ZIP).

Included (high level):

* OnePager PDF + payload JSON
* Multiple FULL run artifacts (SUMMARY.md + run_metrics.json)
* Audit/proof logs (bench_audit_report.json)
* README_REPRO.txt with “where to look” checklist

> If you want the demo, download the **DEMO ZIP** from Releases.
> If you want diligence-grade proof, request **DD/VDR** via the private form.

---

## “Turn this into money” — fast path (no cold sales)

This repo is optimized for **inbound DD**:

1. **Demo ZIP** proves the value fast (10 minutes).
2. **DD Pack** answers the buyer’s fear: reproducibility / robustness / integration.
3. NDA/VDR is only for parties ready to evaluate seriously (company email required).

**If you represent a cloud / database / observability platform team:**
Submit the NDA/VDR form with:

* expected workload type (logs / metrics / semi-structured docs)
* target scale (GB/day or TB/month)
* what “success” means (egress cost, query latency, CPU)

---

## Links

* **Docs / Site:** [https://kodomonocch1.github.io/see_proto/](https://kodomonocch1.github.io/see_proto/)
* **Releases (DEMO ZIP + DD pack):** [https://github.com/kodomonocch1/see_proto/releases](https://github.com/kodomonocch1/see_proto/releases)
* **Discussions:** [https://github.com/kodomonocch1/see_proto/discussions](https://github.com/kodomonocch1/see_proto/discussions)
* **Private contact (NDA/VDR):** [https://docs.google.com/forms/d/e/1FAIpQLScV2Ti592K3Za2r_WLUd0E6xSvCEVnlEOxYd6OGgbpJm0ADlg/viewform?usp=header](https://docs.google.com/forms/d/e/1FAIpQLScV2Ti592K3Za2r_WLUd0E6xSvCEVnlEOxYd6OGgbpJm0ADlg/viewform?usp=header)

### Deep dive

* Medium: The Hidden Cloud Tax and the Schema-Aware Revolution
* DEV.to: Making JSON Compression Searchable — SEE (Schema-Aware Encoding)
* Slides: SEE — The Hidden Cloud Tax Breaker (SpeakerDeck)

> Note: GitHub Discussions are public. Do **not** post confidential info.

```

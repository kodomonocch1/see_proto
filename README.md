<img width="915" height="493" alt="スクリーンショット 2026-02-17 223920" src="https://github.com/user-attachments/assets/e001eb79-7619-4f08-a9d2-6de816d4e433" />

### SEE — Searchable JSON Compression (Semantic Entropy Encoding)

[![Release](https://img.shields.io/github/v/release/kodomonocch1/see_proto)](https://github.com/kodomonocch1/see_proto/releases)
[![Discussions](https://img.shields.io/github/discussions/kodomonocch1/see_proto?label=Q%26A%20%2F%20Repro)](https://github.com/kodomonocch1/see_proto/discussions)

**combined ≈ 7.7% (Zstd 13.7%) • lookup p50 ≈ 0.085 ms • skip ≈ 99%**

> **Why it matters**
> SEE reduces both the **data tax** (storage/egress) and the **CPU tax** (decompress/parse) by keeping JSON **searchable while compressed**.
> Unlike Zstd-only, SEE supports **random access + exists/pos queries** without a separate external index.

<p>
  <a href="https://github.com/kodomonocch1/see_proto/releases"><b>① Download (Latest Release)</b></a> ・
  <a href="https://github.com/kodomonocch1/see_proto/releases"><b>② Demo ZIP (10 minutes)</b></a> ・
  <a href="#dd-pack-audit--repro"><b>③ DD Pack (Audit & Repro)</b></a>
</p>

<p>
  <a href="https://github.com/kodomonocch1/see_proto/discussions/categories/q-a"><b> Start a Discussion (Q&A)</b></a>
  &nbsp;•&nbsp;
  <a href="https://github.com/kodomonocch1/see_proto/discussions/categories/benchmarks-repro"><b> Benchmarks & Repro</b></a>
</p>

---

## Strategic acquisition / exclusive license (serious inquiries)

SEE is being positioned as a **strategic asset** for platform teams (Infra / Data / Storage / Observability) and **CorpDev**.

**Evaluation policy (competition by slots, not deadlines)**  
- **Limited NDA eval slots:** we run **up to a small number per month**, prioritized for parties with a **clear integration path**.  
- **Proof-first (no meetings required):** the **DEMO ZIP + DD Pack** are built so your team can **verify KPIs without calls**.  
- **Contact & filter (serious-only):** **company email preferred** for faster routing, but **personal email / LinkedIn / X DMs are welcome**.  
  *No confidential data needed in the first message. We may decline anonymous/low-context requests.*

**What we accept**
-  **Acquisition (asset deal)**
-  **Exclusive license**
-  **Pilot under NDA** (for integration validation)

**How evaluation works (proof-first)**
1) **Public DEMO (10 min):** run the demo ZIP and see the KPIs on your machine  
2) **DD Pack (audit/repro):** verify **mismatch==0**, strict gates, and reproducibility artifacts  
3) **NDA / VDR:** deeper evaluation for serious integration paths

**Filter (to keep it fast)**
- Company email required (no confidential data needed).
- **Limited evaluation slots** (to keep turnaround fast for serious parties).

> **Enterprise / NDA inquiry** → <a href="https://docs.google.com/forms/d/e/1FAIpQLScV2Ti592K3Za2r_WLUd0E6xSvCEVnlEOxYd6OGgbpJm0ADlg/viewform?usp=header"><b>Private contact form</b></a>

---

## OnePager (latest)

<img width="594" height="835" alt="SEE OnePager (latest)" src="https://github.com/user-attachments/assets/69e99d10-5095-47f1-b2a9-1d48871bf631" />

---

## What is SEE?

- **Schema-aware JSON compression:** combines *structure × delta × dictionary (+ Bloom / Skip)* to stay **searchable while compressed**, with **page-level random access**.
- **Design trade-off:** optimizes **low I/O & low latency** and **~99% skip rate** (not only smallest bytes).

### Key metrics (latest)

- **Combined size:** **≈ 7.7% of raw** (reference: **Zstd combined ≈ 13.7%**)
- **Lookup latency (ms):**
  - present p50/p95/p99 ≈ **0.083 / 0.098 / 0.159**
  - absent  p50/p95/p99 ≈ **0.084 / 0.119 / 0.183**
- **Skip ratio:** present ≈ **0.994**, absent ≈ **0.997**  
- **Bloom density:** ≈ **0.376**
- **Reader path:** PageDir + mini-index (default)

### ROI quick math

`Savings/TB = (1 − ratio_see[combined]) × Price_per_GB × 1000`  
Example: $0.05/GB → **≈$46/TB**, $0.25/GB → **≈$231/TB**

---

## Try in 10 minutes <a id="try-in-10-min"></a>

### Option A: pip (wheel)

```bash
pip install see_proto
python samples/quick_demo.py
````

Prints compression ratio, skip rate, Bloom density, and lookup latency (p50/p95/p99).

### Option B: Demo ZIP (recommended for reproducibility)

Go to **Releases** and download the **DEMO ZIP** (it includes wheel + sample `.see` + scripts + metrics + OnePager).

**Integrity check**

```powershell
pwsh tools/verify_checksums.ps1
# or manually check SHA256SUMS.txt
```

---

## Troubleshooting (10-min demo)

If you see `FileNotFoundError` or similar, you’re likely **not in the expected working directory**.

**Why this happens**
`samples/quick_demo.py` loads packaged sample files using **paths relative to the current working directory**.
If you execute it from somewhere else (e.g., your home directory), Python can’t find `samples/...` and fails.

**Fix — pick one**

1. Run from the repo root (unzipped folder):

```bash
# macOS/Linux
cd /path/to/see_proto
python samples/quick_demo.py
```

```powershell
# Windows PowerShell
cd C:\path\to\see_proto
python samples\quick_demo.py
```

2. Run as a module (works from any directory):

```bash
python -m see_proto.samples.quick_demo
```

**Other common errors**

* `ModuleNotFoundError` → `pip install see_proto`
* Path contains spaces → `cd "C:\Users\You\Downloads\see_proto"`

If issues persist, open a thread in Discussions → Q&A / Repro with the full error message (no confidential data).

> **Note:** GitHub Discussions are public. Do **not** post confidential information.
> For formal evaluations, use the **private NDA/VDR form**.

---

## Why SEE vs Zstd-only?

* **Zstd-only** can be smaller, but it’s not **searchable**; you still pay **I/O + CPU** to decompress and parse JSON.
* **SEE** trades a format-aware pipeline for **millisecond lookups**, **page-level random access**, and **~99% skipping** — often lowering **TCO** even when bytes are not minimal.

---

## DD Pack (Audit & Repro) <a id="dd-pack-audit--repro"></a>

**What it is**
The DD pack is an **audit/repro bundle** for evaluators who need more than “a demo works”.

**What it proves**

* **Decode mismatch == 0** (strict / extended checks)
* Reproducible run artifacts (run summaries + run_metrics)
* Integrity checks and “what to inspect” list

**What it is NOT**

* Not a 10-minute demo
* Not source-code disclosure
* Not a public VDR

The DD pack is designed so a reviewer can validate key claims **without meetings**.

> Request via the **private contact form** (company email required).

---

## What’s included in the Release assets

### DEMO ZIP (public)

* Python wheel (.whl)
* Sample `.see` + `.meta.json`
* Demo scripts: `samples/quick_demo.py`, `samples/quick_bench.py`
* Metrics snapshots (`samples/metrics/*`)
* OnePager PDF
* Integrity checks: `tools/verify_checksums.ps1`, `SHA256SUMS.txt`

### DD Pack (by request)

* `README_REPRO.txt` (fast verify + inspection keys)
* Selected run artifacts (`run_metrics.json`, `SUMMARY.md`, and proof logs)
* Integrity verification (`pack_verify.txt` etc.)

---

## FAQ (short)

**Q. Will it ever be larger than Zstd?**
A. Sometimes yes; in return you get **ms lookups** and **~99% skipping**. For I/O/CPU-bound workloads, **TCO decreases**.

**Q. Best-fit data?**
A. Repetitive **JSON/NDJSON** such as logs, events, telemetry, and metrics.

**Q. Why not build a separate index?**
A. Separate indexes add extra I/O, space, and consistency risk. SEE keeps searchability **inside the storage format**.

**Q. How to tune for different data?**
A. Adjust Bloom density (often works well in 0.25–0.55). Demo prints all metrics for validation.

---

## Links

* **Docs / Site:** [https://kodomonocch1.github.io/see_proto/](https://kodomonocch1.github.io/see_proto/)

* **Latest Release:** [https://github.com/kodomonocch1/see_proto/releases](https://github.com/kodomonocch1/see_proto/releases)

* **Private NDA / VDR inquiry:** [https://docs.google.com/forms/d/e/1FAIpQLScV2Ti592K3Za2r_WLUd0E6xSvCEVnlEOxYd6OGgbpJm0ADlg/viewform?usp=header](https://docs.google.com/forms/d/e/1FAIpQLScV2Ti592K3Za2r_WLUd0E6xSvCEVnlEOxYd6OGgbpJm0ADlg/viewform?usp=header)

* **Deep Dive (Medium):** [https://medium.com/@tetsutetsu11/the-hidden-cloud-tax-and-the-schema-aware-revolution-46b5038c57b8](https://medium.com/@tetsutetsu11/the-hidden-cloud-tax-and-the-schema-aware-revolution-46b5038c57b8)

* **Developer Article (DEV.to):** [https://dev.to/kodomonocch1/making-json-compression-searchable-see-schema-aware-encoding-4ojk](https://dev.to/kodomonocch1/making-json-compression-searchable-see-schema-aware-encoding-4ojk)

* **Slides (SpeakerDeck):** [https://speakerdeck.com/tetsu05/see-the-hidden-cloud-tax-breaker-schema-aware-compression-beyond-zstd](https://speakerdeck.com/tetsu05/see-the-hidden-cloud-tax-breaker-schema-aware-compression-beyond-zstd)

* **LinkedIn (Tetsuro Kawamoto):** [https://www.linkedin.com/in/tetsuro-kawamoto-114907388/](https://www.linkedin.com/in/tetsuro-kawamoto-114907388/)

* **X/Twitter:** [https://x.com/kamikakusi0001](https://x.com/kamikakusi0001)

> Discussions are public — do not post confidential data.
> For serious evaluations: use the private form (company email required).

```

<img width="1024" height="586" alt="Gemini_Generated_Image_f2hennf2hennf2he" src="https://github.com/user-attachments/assets/aa2d0fac-395f-4a12-8835-9ad565ef05c9" />

### SEE — Searchable JSON Compression (Semantic Entropy Encoding)

**combined ≈ 19.5% • lookup p50 ≈ 0.18 ms • skip ≈ 99%**

> **Why it matters**
> SEE reduces both the **data tax** (storage/egress) and the **CPU tax** (decompress/parse) by keeping JSON **searchable while compressed**.
> It may not always be smaller than Zstd, but **searchability + low I/O + random access** leads to better **TCO/ROI** for many workloads.

<p>
  <a href="https://github.com/kodomonocch1/see_proto/releases/tag/v0.1.0"><b>① Download (Release)</b></a> ・
  <a href="https://github.com/kodomonocch1/see_proto/releases/download/v0.1.0/SEE_onepager.pdf"><b>② OnePager (ROI)</b></a> ・
  <a href="#try-in-10-min"><b>③ Try in 10 minutes</b></a>
</p>

> **Enterprise / NDA inquiry** → <a href="https://docs.google.com/forms/d/e/1FAIpQLScV2Ti592K3Za2r_WLUd0E6xSvCEVnlEOxYd6OGgbpJm0ADlg/viewform?usp=header"><b>Private contact form</b></a>
> *Under NDA: full VDR pack available. Please provide a **company email** (no confidential data required).*

---

## What is SEE?

* **Schema-aware JSON compression:** combines *structure × delta × Zstd (+ Bloom / Skip)* to stay **searchable while compressed**, with **page-level random access**.
* **Design trade-off:** favors **low I/O & low latency (ms)** and **~99% skip rate** over minimal size.

### Key metrics (Demo)

* Combined size: **≈19.5% of raw**
* Lookup present (ms): **p50 ≈ 0.18 / p95 ≈ 0.28 / p99 ≈ 0.34**
* Skip ratio: **present ≈ 0.99 / absent ≈ 0.992**, Bloom density ≈ **0.30**

<img width="587" height="824" alt="スクリーンショット 2025-10-06 005753" src="https://github.com/user-attachments/assets/f59aed13-6691-4586-b81a-d932beff3510" />

### ROI quick math

`Savings/TB = (1 − 0.195) × Price_per_GB × 1000`
Example: $0.05/GB → **≈$40/TB**, $0.25/GB → **≈$200/TB**

---

## 🔧 Try in 10 minutes <a id="try-in-10-min"></a>

```bash
python samples/quick_demo.py
```

Prints compression ratio, skip rate, Bloom density, and lookup latency (p50/p95/p99).

**Demo package (Release v0.1.0):**

* Includes Python wheel, `.see` files, demo scripts, metrics, and OnePager PDF.
* Reproducible on Windows / macOS / Linux.
* Verify integrity using:

  ```bash
  pwsh tools/verify_checksums.ps1
  # or manually check SHA256SUMS.txt
  ```

**KPI (demo)**: combined ≈ **19.5%**, lookup **p50 ≈ 0.18 ms**, skip ≈ **99%**, bloom ≈ **0.30**.
*Tradeoff:* not always smaller than Zstd, but stays **searchable while compressed**, cutting **I/O and CPU** costs.

---

> **Questions / feedback?**  
> Prefer **DMs** over email — I’m happy to answer quick questions via  
> **LinkedIn** (preferred): <https://www.linkedin.com/in/tetsuro-kawamoto-114907388/> · **X/Twitter**: <https://x.com/kamikakusi0001>  
> *Please don’t share confidential data in public issues or discussions.*

## Why SEE vs Zstd-only?

* **Zstd-only** can be smaller, but not **searchable**; you still pay **I/O + CPU** to decompress and parse JSON.
* **SEE** trades a small size increase for **millisecond lookups** and **page-level random access**, reducing **I/O and CPU** — resulting in better **TCO**.

---

## FAQ (short)

* **Q. Will it ever be larger than Zstd?**
  **A.** Sometimes yes; in return you get **ms lookups** and **~99% skipping**. For I/O/CPU-bound workloads, **TCO decreases**.

* **Q. Best-fit data?**
  **A.** Repetitive **JSON/NDJSON** such as logs, events, telemetry, and metrics.

* **Q. How long to reproduce?**
  **A.** About **10 minutes** using the included Demo ZIP.

* **Q. Why not build a separate index?**
  **A.** Separate indexes add extra I/O, space, and consistency risk.
  SEE keeps searchability **inside the storage format**, reducing random I/O and parsing overhead.

* **Q. How to tune for different data?**
  **A.** Adjust Bloom density (default ≈0.30, works best in 0.25–0.55). Demo prints all metrics for validation.

---

## What’s included in the Release ZIP

* **Python Wheel (.whl)**
* **Demo scripts**: `samples/quick_demo.py`, `samples/quick_bench.py` (prints KPIs)
* **OnePager (PDF)** and `metrics/` summaries
* **Integrity check script:** `tools/verify_checksums.ps1`
* **README_FIRST.md** — concise reproduction guide

---
## 📦 VDR (Virtual Data Room) — Evaluation Package

**What it is**  
The SEE **VDR** is a **private, NDA-only evaluation bundle** that lets third parties reproduce our key KPIs on their own machine:
- **Compression:** combined size ≈ *~19.5% of raw*
- **Lookup latency:** p50 ≈ *~0.18 ms*
- **Skipping:** *~99%* page-level skip

**What it contains (high level)**  
- Sample **`.see` artifacts** with minimal metadata (for reproducible tests)  
- A **prebuilt evaluation wheel** (binary-only) for quick local runs  
- **KPI summaries** (CSV/JSON) and a frozen **results snapshot**  
- Simple **verification scripts** (checksums / quality-gate)  
- A concise **One-Pager** and evaluator **README**

> ℹ️ Implementation details (core algorithms, dictionaries, low-level parameters) remain **proprietary** and are **not** disclosed in this repository.

> **Before requesting NDA:**  
> If you’re exploring whether SEE fits your workload, feel free to **DM me first** on  
> **LinkedIn**: <https://www.linkedin.com/in/tetsuro-kawamoto-114907388/> or **X/Twitter**: <https://x.com/kamikakusi0001>.  
> I can help map your use case to the public demo (10-min repro) and share the right next steps.

**Access policy**  
- Distributed **on request under NDA** (no public download).  
- To request access, please contact us via **LinkedIn** (see [Official Links & Profiles](#-official-links--profiles)) with the subject: **“SEE VDR Access”**.  
- Redistribution, reverse engineering, and public benchmarking of VDR binaries are **prohibited**.  
- An **Evaluation EULA** applies in addition to the NDA.

**How evaluators use it **  
1. Verify package integrity (checksums script).  
2. Install the provided evaluation wheel into a clean virtual environment.  
3. Run the 10-minute demo to print **ratio / skip / bloom / p50–p99**.  
4. Compare local output with the included **KPI snapshot** (apples-to-apples).

**Why VDR?**  
- Ensures **reproducible, verifiable** numbers without exposing the core IP.  
- Shortens technical diligence for **FinOps / M&A / platform** teams while keeping trade secrets protected.

> If you only need the public demo, see the repository’s samples and Release assets.  
> The **VDR is reserved for formal evaluations** (NDA) that require deeper verification.

## Links

* **Docs / Site:** [https://kodomonocc1.github.io/see_proto/](https://kodomonocch1.github.io/see_proto/)
* **Latest Release (Demo ZIP + Wheel + OnePager + SHA256):** [https://github.com/kodomonocch1/see_proto/releases/tag/v0.1.0](https://github.com/kodomonocch1/see_proto/releases/tag/v0.1.0)
* **Enterprise / NDA contact (private):** [https://docs.google.com/forms/d/e/1FAIpQLScV2Ti592K3Za2r_WLUd0E6xSvCEVnlEOxYd6OGgbpJm0ADlg/viewform?usp=header](https://docs.google.com/forms/d/e/1FAIpQLScV2Ti592K3Za2r_WLUd0E6xSvCEVnlEOxYd6OGgbpJm0ADlg/viewform?usp=header)

> Optional: GitHub Discussions are public. Do not post confidential information.
> Do **not** post confidential information or emails there — use the **private form** above.

## 🔗 Official Links & Profiles

- 🧠 **Deep Dive (Medium):** [The Hidden Cloud Tax and the Schema-Aware Revolution](https://medium.com/@tetsutetsu11/the-hidden-cloud-tax-and-the-schema-aware-revolution-46b5038c57b8)
- 💻 **Developer Article (DEV.to):** [Making JSON Compression Searchable — SEE (Schema-Aware Encoding)](https://dev.to/kodomonocch1/making-json-compression-searchable-see-schema-aware-encoding-4ojk)
- 🎞️ **Slides (SpeakerDeck):** [SEE — The Hidden Cloud Tax Breaker: Schema-Aware Compression Beyond Zstd](https://speakerdeck.com/tetsu05/see-the-hidden-cloud-tax-breaker-schema-aware-compression-beyond-zstd)
- 🔗 **LinkedIn (Tetsuro Kawamoto):** [Connect on LinkedIn](https://www.linkedin.com/in/%E5%BE%B9%E9%83%8E-%E6%B2%B3%E6%9C%AC-114907388/)

---

## 📨 Contact & Questions
For non-confidential questions, please **DM** me:

- **LinkedIn (preferred):** <https://www.linkedin.com/in/tetsuro-kawamoto-114907388/>  
- **X/Twitter:** <https://x.com/kamikakusi0001>

For formal evaluations, use the **NDA/VDR form** after our DM:
https://docs.google.com/forms/d/e/1FAIpQLScV2Ti592K3Za2r_WLUd0E6xSvCEVnlEOxYd6OGgbpJm0ADlg/viewform

```
SEE (Semantic Entropy Encoding)
https://github.com/kodomonocch1/see_proto
```


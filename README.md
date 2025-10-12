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

## Links

* **Docs / Site:** [https://kodomonocc1.github.io/see_proto/](https://kodomonocc1.github.io/see_proto/)
* **Latest Release (Demo ZIP + Wheel + OnePager + SHA256):** [https://github.com/kodomonocch1/see_proto/releases/tag/v0.1.0](https://github.com/kodomonocch1/see_proto/releases/tag/v0.1.0)
* **Enterprise / NDA contact (private):** [https://docs.google.com/forms/d/e/1FAIpQLScV2Ti592K3Za2r_WLUd0E6xSvCEVnlEOxYd6OGgbpJm0ADlg/viewform?usp=header](https://docs.google.com/forms/d/e/1FAIpQLScV2Ti592K3Za2r_WLUd0E6xSvCEVnlEOxYd6OGgbpJm0ADlg/viewform?usp=header)

> **Note:** The GitHub Discussions “Enterprise (NDA)” category is **public**.
> Do **not** post confidential information or emails there — use the **private form** above.

---

## Optional: For reproducibility or citation

If you reproduce benchmarks or use SEE in your research, please cite:

```
SEE (Semantic Entropy Encoding)
https://github.com/kodomonocch1/see_proto
```

---

### ✅ Recommended next step

1. Clone and run the **10-min demo** to verify KPIs.
2. Read the **OnePager (ROI)** for TCO and savings formulas.
3. For enterprise evaluation under NDA, submit your **company email** via the private form.

---

### ✅ About signals/stars.csv

Keep `signals/stars.csv` **as-is** — do **not modify or remove it**.
It’s an automated log generated by GitHub Actions to record stars (timestamp + user).
It’s perfectly fine to leave it in the repo; it doesn’t expose sensitive data and shows healthy engagement growth.

---

Would you like me to also generate a **shorter “README_FIRST.md”** version (for the ZIP demo folder) to match this English tone? It should be about 10 lines with install → verify → demo steps.

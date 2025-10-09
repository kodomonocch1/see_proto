# SEE — Searchable JSON compression (Semantic Entropy Encoding)
**combined ≈ 19.5% • lookup p50 ≈ 0.18 ms • skip ≈ 99%**  
**検索可能な圧縮（exists*/pos*）— 結合サイズ ≈ 19.5%、検索p50 ≈ 0.18 ms、スキップ ≈ 99%**

> **Why it matters**  
> SEE cuts both **data tax** (storage/egress) and **CPU tax** (decompress/parse) by keeping JSON **searchable while compressed**.  
> It may not always be smaller than Zstd, but **searchability + low I/O + random access** delivers better **TCO/ROI** for many workloads.
>
> **なぜ必要か**  
> SEE は圧縮状態のまま検索できるため、クラウドの**データ税（ストレージ/エグレス）**と**CPU税（解凍/パース）**を同時に削減します。  
> Zstd 単体より小さくない場合もありますが、**検索可能性＋低I/O＋ランダムアクセス**で **TCO/ROI** を改善します。

<p>
  <a href="https://github.com/kodomonocch1/see_proto/releases/tag/v0.1.0"><b>① Download (Release)</b></a> ・
  <a href="https://github.com/kodomonocch1/see_proto/releases/download/v0.1.0/SEE_onepager.pdf"><b>② OnePager (ROI)</b></a> ・
  <a href="#try-in-10-min"><b>③ Try in 10 min / 10分検証</b></a>
</p>

> **Enterprise (NDA inquiry)** → <a href="https://docs.google.com/forms/d/e/1FAIpQLScV2Ti592K3Za2r_WLUd0E6xSvCEVnlEOxYd6OGgbpJm0ADlg/viewform?usp=header"><b>Private contact form</b></a>  
> *Under NDA: VDR pack available. Send your **company email** via the form (no confidential data).*  
> **企業向け（NDA連絡）**は <a href="https://docs.google.com/forms/d/e/1FAIpQLScV2Ti592K3Za2r_WLUd0E6xSvCEVnlEOxYd6OGgbpJm0ADlg/viewform?usp=header"><b>プライベートフォーム</b></a> へ。*NDAの上でVDRをご案内。**会社メール**でご連絡ください（機密情報は送らないでください）。*

---

## What is SEE? / SEE の概要
- **Schema-aware** compression for JSON: *structure × delta × Zstd (+ Bloom / Skip)* → **searchable while compressed** with **page-level random access**.  
  **スキーマアウェア**なJSON圧縮：*構造×差分×Zstd（＋Bloom/Skip）* により、**圧縮のまま検索**と**ページ粒度ランダムアクセス**を実現。
- **Design trade-off**: Prioritizes **low I/O & low latency** (ms) and **~99% skip rate** over absolute smallest size.  
  **設計の重心**：最小サイズよりも **低I/O・低レイテンシ（ms級）**と**~99%スキップ**を優先。

**Key numbers（demo） / 主要KPI（デモ）**  
- Size (combined): **≈19.5% of raw**  
- Lookup present (ms): **p50 ≈ 0.18 / p95 ≈ 0.28 / p99 ≈ 0.34**  
- Skip ratio: **present ≈0.99 / absent ≈0.992**, Bloom density ≈ **0.30**

**ROI quick math / 簡易ROI**  
`Savings/TB = (1 − 0.195) × Price_per_GB × 1000`  
例）$0.05/GB → **≈$40/TB**、$0.25/GB → **≈$200/TB**

---

**Try in 10 minutes** → run `python samples/quick_demo.py` (prints ratio/skip/bloom + p50/p95/p99)  
**Download (Demo ZIP / Wheel / OnePager)** → see **Release v0.1.0**  
**Enterprise / NDA (private form)** → request VDR access here

KPI (demo): combined ≈ **19.5%**, lookup **p50 ≈ 0.18 ms**, skip ≈ **99%**, bloom ≈ **0.30**.
*Tradeoff:* not always smaller than Zstd, but stays **searchable while compressed** → lower **I/O & CPU**.


**Integrity / 整合性確認**  
Verify `SHA256SUMS.txt` (or run `tools/verify_checksums.ps1`).  
`SHA256SUMS.txt` を照合（`tools/verify_checksums.ps1` でも可）。

---

## Why SEE vs Zstd-only? / Zstd単体との違い
- **Zstd-only** can be smaller, but not **searchable**; you pay **I/O + CPU** to decompress & parse JSON.  
  **Zstd単体**はさらに小さい場合がありますが**検索不可**。結局 **解凍＋JSONパース**で **I/O/CPU** が嵩みます。
- **SEE** trades a little size for **ms lookups on compressed data** and **random access**, cutting **I/O and CPU** → better **TCO**.  
  **SEE** はサイズを少し犠牲に**圧縮のままms級検索**と**ランダムアクセス**を獲得し、**I/OとCPU**を削減 → **TCO改善**。

---

## FAQ (short) / よくある質問（簡易）
- **Q. Will it ever be larger than Zstd?**  
  **A.** Sometimes yes; in return you get **ms lookups** and **~99% skipping**. For I/O/CPU-dominated workloads, **TCO goes down**.  
  **Q. Zstdより大きくなる？**  
  **A.** 場合によりあります。代わりに **ms級検索**と **~99%スキップ**を得ます。I/O/CPU支配のワークロードでは **TCOが下がります**。
- **Q. Best-fit data?** → Repetitive **JSON/NDJSON** (logs, events, telemetry, metrics).  
  **向くデータ** → 繰り返し構造の **JSON/NDJSON**（ログ/イベント/テレメトリ/メトリクス）。
- **Q. How long to reproduce?** → About **10 minutes** with the Demo ZIP.  
  **再現時間** → **約10分**（Demo ZIP 付属の手順どおり）。
- **Index separately instead?** Extra index = extra I/O/space + consistency risk. SEE bakes searchability into storage, cutting random I/O and parse work.
- **Real data fit?** Repetitive JSON/NDJSON (logs/events/telemetry). Demo prints full KPIs; tweak bloom density (0.25–0.55) to match your pattern.

---

## What’s in the release ZIP? / ZIPの中身
- Wheel (.whl), **Demo**: `samples/quick_demo.py`, `quick_bench.py` (KPI printing)  
- **OnePager (PDF)**, metrics summaries, `tools/verify_checksums.ps1`  
- All steps consolidated in **README_FIRST.md**. / 手順は **README_FIRST.md** に統一

---

## Links
- **Docs / Site**: https://kodomonocc1.github.io/see_proto/  
- **Latest Release (Demo ZIP + Wheel + OnePager + SHA256)**: https://github.com/kodomonocch1/see_proto/releases/tag/v0.1.0  
- **Enterprise (NDA inquiry, private)**: https://docs.google.com/forms/d/e/1FAIpQLScV2Ti592K3Za2r_WLUd0E6xSvCEVnlEOxYd6OGgbpJm0ADlg/viewform?usp=header

> **Note / 注意**: The GitHub Discussions “Enterprise (NDA)” category is **public**. Do **not** post confidential info or emails there—use the **private form** above.  
> GitHubのDiscussions「Enterprise (NDA)」は**公開**です。機密や連絡先は書かず、**上記フォーム**をご利用ください。

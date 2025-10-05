# see_proto (SEE: Semantic Entropy Encoding)

**EN:** Schema-aware JSON compression that keeps data *searchable* (supports `exists*` / `pos*` lookups).  
**JP:** JSON 向け **スキーマアウェア圧縮**。圧縮のまま *`exists*` / `pos*`* を検索可能。

- **KPI:** combined size ≈ **19.5%** of raw / present lookup **p50 ≈ 0.18 ms, p99 ≈ 0.34 ms**（demo）
- **Site / Docs:** https://kodomonocc1.github.io/see_proto/
- **Latest Release (Demo ZIP + Wheel + OnePager + SHA256):**  
  https://github.com/kodomonocc1/see_proto/releases/latest

---

## Start here / はじめに（**ZIP 内 README を参照**）
1. **Download the Demo ZIP (JP/EN)** from the [latest release](https://github.com/kodomonocc1/see_proto/releases/latest).  
   **最新リリース**から **JP/EN のデモ ZIP** をダウンロード。
2. **Open `README_FIRST.md` inside the ZIP** — all steps are there.  
   **ZIP 内の `README_FIRST.md`** に手順をすべて記載。
3. **Verify integrity** with **`SHA256SUMS.txt`**, then run:  
   `python samples/quick_demo.py` → KPIs (ratio/skip/bloom + p50/p95/p99) are printed.  
   **`SHA256SUMS.txt`** で改ざん検証後、`python samples/quick_demo.py` を実行（KPI を表示）。

> This repository’s README is only an entry point.  
> 実行・検証の手順は **ZIP 内 `README_FIRST.md`** に統一しています。

---

## What is SEE? / SEE の概要
- **EN:** Searchable compression (structure × delta × Zstd + Bloom/Skip).  
  Trades a little size for **I/O-skip** and **ms-level random access lookups**.
- **JP:** 構造 × Δ × Zstd に **Bloom/Skip** を組み合わせた「**検索可能な圧縮**」。  
  単純な最小サイズより **I/O スキップ**と**ms 級ランダムアクセス**を優先。

### Key numbers / 主要数値
- `ratio_see[str]` ≈ **0.168–0.170**, `ratio_see[combined]` ≈ **0.194–0.196**  
- Bloom density ≈ **0.30** / Skip: present ≈ **0.99**, absent ≈ **0.992**  
- Lookup (ms): present **0.18 / 0.28 / 0.37** (p50/p95/p99), absent **~1.2–2.4**

*(numbers are from the included demo metrics; see ZIP → `samples/quick_demo.py` output)*

---

## ROI (quick math) / 迅速な ROI 試算
`Savings/TB = (1 − 0.195) × Price_per_GB × 1000`  
**Example / 例:** Price_per_GB = **$0.05** ⇒ **$40.25 / TB** 削減。  
Use your egress/storage price and monthly TB to estimate **monthly savings**.  
自社の単価と月間 TB に当てはめて **月次削減額**を即算出できます。

---

## What’s in the release ZIP? / ZIP の内容
- **Wheel (`.whl`)** for Windows x64 (abi3 / Python 3.8+)  
- **Samples**: `quick_demo.py`, `quick_bench.py`（KPI と p50/p95/p99 を表示）  
- **Metrics**: apples/lookup summaries, OnePager (PDF)  
- **Tools**: `verify_checksums.ps1`（展開後のハッシュ検証）

> Install & run steps are all in **`README_FIRST.md`** inside the ZIP.  
> インストールと実行手順はすべて **ZIP 内 `README_FIRST.md`** に記載。

---

## Enterprise / NDA
- For enterprise evaluation under NDA (VDR access, deeper internals), open a thread in **Discussions → “Enterprise (NDA inquiry)”**.  
- 企業での評価（NDA / VDR）をご希望の場合は **Discussions → “Enterprise (NDA inquiry)”** へスレッドを作成してください。

---

## Notes / 補足
- Zstd-only can be smaller in size, but SEE’s value is **searchability + low-I/O lookups**.  
  Zstd 単体の方がサイズは小さい場合がありますが、SEE は **検索可能性**と**低 I/O ルックアップ**を重視します。
- KPIs can vary with data characteristics and page/dictionary heuristics.  
  データ特性やページ/辞書ヒューリスティクスにより KPI は変動します。

---

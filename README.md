# SEE — Searchable JSON compression (Semantic Entropy Encoding)
**combined ≈ 19.5% • lookup p50 ≈ 0.18 ms • skip ≈ 99%**  /  **圧縮後のまま検索可能（exists*/pos*）**

> **Why it matters / なぜ今“必要不可欠”か**  
> 毎日発生するクラウドの**データ税（ストレージ＋エグレス）**と**CPU税（解凍＋JSONパース）**を同時に削減します。  
> **Zstd よりさらに小さくない**場面はありますが、SEE は **検索可能性＋低I/O＋ランダムアクセス**を得るための設計です。  
> 10分で KPI を再現できます。:contentReference[oaicite:1]{index=1}

<p>
  <a href="https://github.com/kodomonocch1/see_proto/releases/tag/v0.1.0"><b>① Download (Release)</b></a> ・
  <a href="https://github.com/kodomonocch1/see_proto/releases/download/v0.1.0/SEE_onepager.pdf"><b>② OnePager (ROI)</b></a> ・
  <a href="#try-in-10-min"><b>③ Try in 10 min / 10分検証</b></a>
</p>

> **Enterprise (NDA inquiry)** → <a href="https://github.com/kodomonocch1/see_proto/discussions/categories/enterprise-nda-inquiry"><b>こちら</b></a>  
> *Under NDA: VDR pack available.*

---

## What is SEE? / SEE の概要
- **Schema-aware** compression for JSON: *structure × delta × Zstd (+ Bloom / Skip)*.  
  構造（スキーマ）と値を分離し、**圧縮のまま exists*/pos* 検索**と**ページ粒度ランダムアクセス**を可能にします。  
- **Design trade-off**: サイズ最小ではなく、**低I/O・低レイテンシ**（ms級）と**スキップ率≈99%**を優先。:contentReference[oaicite:2]{index=2}

**Key numbers / 主要KPI（demo）**  
- Size (combined): **≈19.5% of raw**  
- Lookup present (ms): **p50 ≈ 0.18 / p95 ≈ 0.28 / p99 ≈ 0.34**  
- Skip ratio: **present ≈0.99 / absent ≈0.992**, Bloom density ≈0.30  
（データ特性・ページ/辞書ヒューリスティクスに依存）:contentReference[oaicite:3]{index=3}

**ROI quick math / 簡易ROI**  
`Savings/TB = (1 − 0.195) × Price_per_GB × 1000`（例：$0.05/GB → ≈$40/TB, $0.25/GB → ≈$200/TB）:contentReference[oaicite:4]{index=4}

---

## Try in 10 min  / 10分で検証する  <a id="try-in-10-min"></a>
1. **Download** Demo ZIP (JP/EN) from the latest **Release**. / リリースから **Demo ZIP** をDL  
2. ZIP 内 **README_FIRST.md** の手順に従う（`pip install` 等、すべて記載）  
3. `python samples/quick_demo.py` を実行 → **KPI**（ratio/skip/bloom, p50/p95/p99）を表示  

**Integrity**: verify `SHA256SUMS.txt` → `tools/verify_checksums.ps1` でもOK。:contentReference[oaicite:5]{index=5}

---

## Why SEE is necessary (vs. Zstd-only) / SEE が“必要”な理由
- **Zstd-only** はサイズはさらに小さいことがあるが、**検索・位置参照ができない**ため、結局**解凍＋JSONパース**で **I/O/CPU/遅延**が嵩む。  
- **SEE** はサイズを少しだけ犠牲にして、**圧縮のまま検索（exists*/pos*）＋ランダムアクセス**を提供。**I/O削減 × CPU削減**で**総コスト（TCO）**が下がる。  
- クラウドの**エグレス/ストレージ**と**CPU**の双方に効くので、**FinOps**に直結。:contentReference[oaicite:6]{index=6}

---

## FAQ（short）
- **Q: サイズが Zstd より大きくなるのでは？**  
  A: 場合によりあり。その代わり **ms級のlookups** と **skip≈99%** を得ます。大規模I/OとCPUが支配的なワークロードでは **TCO が下がる**前提です。:contentReference[oaicite:7]{index=7}
- **Q: どんなデータに効きやすい？**  
  A: **繰り返し構造のJSON/NDJSON**（ログ/イベント/メトリクス/テレメトリ等）。  
- **Q: 再現はどれくらいで？**  
  A: **10分程度**（Demo ZIP 付属の `README_FIRST.md` と `quick_demo.py` 参照）。:contentReference[oaicite:8]{index=8}
- **Q: NDA / VDR？**  
  A: **Discussions → Enterprise (NDA inquiry)** より。*Under NDA: VDR pack available.*

---

## What’s in the release ZIP? / ZIP には何が入っている？
- Wheel (.whl), **Demo**: `samples/quick_demo.py`, `quick_bench.py`（KPI出力）  
- **OnePager (PDF)**, metrics summaries, `tools/verify_checksums.ps1`  
- 手順は **ZIP 内 README_FIRST.md** に統一。:contentReference[oaicite:9]{index=9}

---

## Links
- **Docs / Site**: https://kodomonocc1.github.io/see_proto/  
- **Latest Release (Demo ZIP + Wheel + OnePager + SHA256)**: https://github.com/kodomonocch1/see_proto/releases/tag/v0.1.0  
- **Enterprise (NDA inquiry)**: https://github.com/kodomonocch1/see_proto/discussions/categories/enterprise-nda-inquiry

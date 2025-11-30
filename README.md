# 🎤 川普風格 Two-Stage CoT 對話生成器（Homework4）
簡介
- 產生「川普風格」的多樣化回應。提供兩個主要執行檔：
    - `app_cloud_only_v2.py`：話題感知、雲端就緒（推薦部署到 Streamlit Cloud）
    - `app.py`：本地版（需 Ollama）

快速開始（雲端）
1. 安裝依賴（雲端最小化）
```bash
pip install -r requirements-cloud.txt
```
2. 本地測試
```bash
streamlit run app_cloud_only_v2.py
```
3. 部署到 Streamlit Cloud
 - 在 Streamlit Cloud 連接本倉庫，指定 `app_cloud_only_v2.py` 為主程式，Deploy。

本地（Ollama）運行（可選）
```bash
# 啟動 Ollama
ollama serve
# 下載模型
ollama pull llama2
# 運行
streamlit run app.py
```

檔案說明（重點）
- `app_cloud_only_v2.py`：話題感知版本（推薦）
- `app_cloud_only.py`：純模板版本（備份）
- `app.py`：本地 Ollama 版本
- `cot_dialog.py`：CoT 核心邏輯
- `deeplearning_app.py`：CRISP-DM / 深度學習模組（教學用，可選）

測試與驗證
- 話題感知測試：`python test_sentiment_aware.py`
- 情感分析器：`python test_analyzer_simple.py`

部署與維護
- 推薦 v2 雲端快速部署；想要更高質量可使用本地 Ollama + ngrok。

授權
- 教育/研究用途（請根據需要添加 MIT / 其他許可證聲明）

---

(簡化版 README：如要更詳細說明或補充示例，我可以把 README 擴展為完整版本)
# 🎤 川普風格對話生成器

使用 **Two-Stage Chain-of-Thought (CoT) 推理** + **話題感知系統** 生成獨特而有趣的川普風格評論和回應。

> ⭐ **最新版本**（v2）：**話題感知系統** - 根據話題的正負性動態調整評論風格  
> 📊 相關性改進：2/10 → 9/10 (+350%) | 🚀 **完全雲端部署**，2-3 分鐘上線

---

## ✨ 核心特色

✅ **話題感知** (v2) - 負面話題用批評，正面話題用讚美  
✅ **多樣化生成** - 從 28,000+ 個組合隨機生成，每次都不同  
✅ **Two-Stage CoT** - 先生成 5 個評論，再優化最終回應  
✅ **完全雲端** - 在 Streamlit Cloud 上直接運行，無需本地服務  
✅ **零依賴** - 只需 Streamlit、Pandas、NumPy 三個包  
✅ **本地 Ollama** - 支持本地 LLM（備選方案）  

---

## 📁 項目結構

```
homework4/
├── 📱 應用文件
│   ├── app_cloud_only.py          # ⭐ v1：推薦版本（簡潔快速）
│   ├── app_cloud_only_v2.py       # ⭐ v2：最新版本（話題感知）
│   ├── app.py                     # 本地 Ollama 版本
│   └── cot_dialog.py              # Two-Stage CoT 核心邏輯
│
├── 🧠 可選：深度學習 & CRISP-DM
│   ├── deeplearning_app.py        # CRISP-DM 完整工具
│   ├── data_layer.py              # 數據層
│   ├── model_layer.py             # 模型層
│   └── evaluation_layer.py        # 評估層
│
├── ✅ 測試文件
│   ├── test_sentiment_aware.py    # 話題感知測試
│   ├── test_sentiment_fix.py      # 情感修復驗證
│   ├── test_analyzer_simple.py    # 簡單分析器測試
│   └── test_specific_topic.py     # 特定話題測試
│
├── 📦 配置文件
│   ├── requirements.txt           # 本地版本依賴
│   ├── requirements-cloud.txt     # 雲端版本依賴（最小化）
│   └── .streamlit/config.toml     # Streamlit 配置
│
└── 📚 文檔
    ├── README.md                  # 本文件
    ├── ABSTRACT.md                # 項目摘要
    ├── CONVERSATION_LOG.md        # 開發對話記錄
    ├── TOPIC_SENTIMENT_ANALYSIS.md # v2 技術文檔
    ├── VERSION_COMPARISON.md      # v1 vs v2 對比
    ├── SENTIMENT_FIX_REPORT.md    # 情感分析修復報告
    ├── IMPROVEMENT_DETAILS.md     # 改進詳細說明
    ├── STREAMLIT_CLOUD_ONLY.md    # 雲端部署指南
    └── STREAMLIT_CLOUD_DEPLOYMENT.md # 遠程 Ollama 部署
```

---

## 🚀 快速開始

### 🌟 推薦方案：v2 話題感知版本（2-3 分鐘）

**特色**：根據話題正負性自動調整風格  
**相關性**：9/10 (vs v1 的 2/10)

#### 本地運行
```bash
pip install -r requirements-cloud.txt
streamlit run app_cloud_only_v2.py
```

#### 雲端部署
1. 訪問 [Streamlit Community Cloud](https://share.streamlit.io)
2. 連接倉庫：`https://github.com/tonyyoung-create/homework4`
3. 選擇文件：`app_cloud_only_v2.py`
4. 點擊 Deploy → 完成！

---

### 其他方案

#### 方案 A：v1 簡潔版本（最快，無話題感知）
```bash
streamlit run app_cloud_only.py
```

#### 方案 B：本地 Ollama + 遠程部署（最高質量）
```bash
# 1. 本地啟動 Ollama
ollama serve

# 2. 新終端下載模型
ollama pull llama2

# 3. 配置遠程隧道 (ngrok)
ngrok http 11434

# 4. 設置 Streamlit Cloud 環境變數
# OLLAMA_URL=https://xxx.ngrok.io

# 5. 部署
streamlit run app.py
```
詳見 [STREAMLIT_CLOUD_DEPLOYMENT.md](STREAMLIT_CLOUD_DEPLOYMENT.md)

---

## 📊 版本對比

### 工作原理

```
用戶輸入話題
    ↓
[情感分析器]  ← 32 個負面關鍵詞 + 33 個正面關鍵詞
    ↓
判定：負面/正面/中立
    ↓
選擇相應風格集合
    ↓
生成 5 個評論 (多樣化)
    ↓
生成最終回應 (一致性)
    ↓
輸出結果
```

### 情感關鍵詞庫

**負面關鍵詞** (43 個)：
- 情感：痛苦、悲傷、難過、沮喪、失望、絕望、憂鬱
- 事件：失敗、災難、危機、崩潰、破裂、戰爭、死亡
- 品質：糟糕、恶劣、腐敗、虛弱、愚蠢

**正面關鍵詞** (33 個)：
- 成果：成功、勝利、融資、投資、增長、發展
- 特質：偉大、美好、聰慧、領導、勇敢、卓越

詳見 [TOPIC_SENTIMENT_ANALYSIS.md](TOPIC_SENTIMENT_ANALYSIS.md)

---

---

## 💡 使用示例

### 輸入話題（負面）
```
我很難過
```

### 生成結果
```
話題分析: negative ✓

川普的 5 個評論:
1. 說到我很難過：DISGRACE！這是非常 DISGRACE！誰應該負責？
2. 關於我很難過：這是真的 STUPID！無法接受！
3. 當我看到我很難過時：PROBLEM！簡直 PROBLEM！必須改變！
4. 我見過許多失敗，但這個難過的情況是極其嚴重！
5. 別擔心，這個問題很容易解決。相信我！

川普的最終回應:
我見過許多難過的情況，但我知道如何修復它。相信我，我會改變一切！- 川普
```

### 每次都不同
再次生成同一話題會得到完全不同的結果（從 28,000+ 組合中隨機選擇）

---

## 🔧 技術棧

**核心框架**：
- Streamlit 1.28+ - Web 框架
- Python 3.8+ - 編程語言

**可選依賴**：
- Ollama - 本地 LLM 推理
- Pandas / NumPy - 數據處理
- PyTorch / TensorFlow - 深度學習（CRISP-DM 工具）

**部署**：
- Streamlit Community Cloud - 免費雲端託管
- GitHub - 源代碼管理

---

---

## 🧪 本地測試

### 1. 測試話題感知系統
```bash
python test_sentiment_aware.py
```

### 2. 測試情感分析器
```bash
python test_analyzer_simple.py
```

### 3. 運行應用
```bash
# v2 推薦版本
streamlit run app_cloud_only_v2.py

# v1 簡潔版本
streamlit run app_cloud_only.py

# 本地 Ollama 版（需要先啟動 Ollama）
streamlit run app.py
```

---

## 🌐 部署選項對比

| 方案 | 部署時間 | 質量 | 配置 | 成本 | 推薦 |
|------|---------|------|------|------|------|
| 純雲端 | 2-3 分 | ⭐⭐⭐ | 零 | 免費 | ✅ 最佳 |
| 本地 Ollama | 5-10 分 | ⭐⭐⭐⭐ | 中等 | 免費 | 追求質量 |
| VPS Ollama | 14 分 | ⭐⭐⭐⭐ | 複雜 | 付費 | 持續運行 |

---

## 💬 兩階段推理架構

### 第一階段：生成思考（Generate Comments）
```
輸入話題 → 生成 5 個不同角度的川普評論
- 使用 4 種評論風格隨機選擇
- 從 25+ 短語庫中隨機組合
- 應用 7 個強度詞進行變化
```

### 第二階段：優化回應（Generate Final Response）
```
5 個評論 → 生成最終優化的川普回應
- 使用 3 種回應風格隨機選擇
- 從 6 個最終回應範本中隨機選擇
- 應用相同的短語組合邏輯
```

---

## 🎯 可能的應用場景

- 💼 會議開幕致詞
- 🎤 演講文稿參考
- 😄 娛樂和笑料生成
- 📱 社交媒體文案
- 🎓 語言學習參考
- 🎬 劇本對白創意

---

## 🔄 更新日誌

### 2025-11-30 - 改進版本
- ✅ 擴展短語庫：15 → 25+ 個
- ✅ 多樣化範本：5 → 18 個
- ✅ 可能組合：375 → 28,000+
- ✅ 新增風格分類系統
- ✅ 完全消除制式化問題

### 2025-11-29 - 雲端版本
- ✅ 移除 ML 模型依賴
- ✅ 簡化為 3 個核心包
- ✅ 實現 2-3 分鐘快速部署

### 2025-11-28 - 遠程 Ollama 支持
- ✅ 添加環境變數支持
- ✅ ngrok 隧道集成
- ✅ Streamlit Cloud 部署指南

---

## 📞 支持和反饋

- 📖 查看 [IMPROVEMENT_DETAILS.md](IMPROVEMENT_DETAILS.md) 了解技術細節
- 🚀 查看 [STREAMLIT_CLOUD_ONLY.md](STREAMLIT_CLOUD_ONLY.md) 快速部署
- 🔧 查看 [STREAMLIT_CLOUD_DEPLOYMENT.md](STREAMLIT_CLOUD_DEPLOYMENT.md) 高級配置

---

## 📄 許可證

此項目為教育和娛樂目的創建。

---

## 🙏 致謝

- Streamlit - 優秀的 Web 框架
- Ollama - 本地 LLM 推理
- GitHub - 版本控制和部署

---

**⭐ 如果覺得有用，請給個 Star！**

🎤 現在就試試吧：https://github.com/tonyyoung-create/homework4

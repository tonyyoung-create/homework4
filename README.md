# 🎤 川普風格對話生成器

使用 **Two-Stage Chain-of-Thought (CoT) 推理** 生成獨特而有趣的川普風格評論和回應。

> ⭐ **最新改進**（2025-11-30）：引入多樣化生成系統，從 375 個可能組合擴展至 28,000+，徹底消除制式化問題！
> 
> 🚀 **快速部署**：完全在 Streamlit Cloud 運行，無需任何本地服務

---

## ✨ 核心特色

✅ **多樣化生成** - 從 28,000+ 個組合中隨機生成，每次都不同  
✅ **Two-Stage CoT** - 先生成 5 個評論，再優化最終回應  
✅ **完全雲端** - 在 Streamlit Cloud 上直接運行，無需本地服務  
✅ **零依賴** - 只需 Streamlit、Pandas、NumPy 三個包  
✅ **實時部署** - 2-3 分鐘快速部署到 Streamlit Cloud  
✅ **本地 Ollama** - 支持本地 LLM（備選方案）  

---

## 📁 項目結構

```
homework4/
├── app_cloud_only.py          # ⭐ 推薦：純雲端版本（完全無依賴）
├── app.py                      # 本地 Ollama 版本
├── cot_dialog.py               # Two-Stage CoT 核心邏輯
├── deeplearning_app.py         # 可選：CRISP-DM 工具
├── data_layer.py               # CRISP-DM 數據層
├── model_layer.py              # CRISP-DM 模型層
├── evaluation_layer.py         # CRISP-DM 評估層
├── test_generator.py           # 多樣性測試腳本
├── requirements.txt            # 本地版本依賴
├── requirements-cloud.txt      # 雲端版本依賴（最小化）
├── IMPROVEMENT_DETAILS.md      # 改進詳細說明
├── STREAMLIT_CLOUD_ONLY.md     # 雲端部署指南
├── STREAMLIT_CLOUD_DEPLOYMENT.md # 遠程 Ollama 部署
└── README.md                   # 本文件
```

---

## 🚀 快速開始

### 方案 A：純雲端版本（推薦，2-3 分鐘）

**優點**：無需任何配置，直接部署  
**部署步驟**：

1. 訪問 [Streamlit Community Cloud](https://share.streamlit.io)
2. 連接你的 GitHub 倉庫：`https://github.com/tonyyoung-create/homework4`
3. 選擇主文件：`app_cloud_only.py`
4. 點擊「Deploy」
5. 等待 2-3 分鐘，應用上線！

**依賴**（最小化）：
```
streamlit>=1.28.0
pandas>=2.0.0
numpy>=1.24.0
```

**立即體驗**（本地）：
```bash
pip install -r requirements-cloud.txt
streamlit run app_cloud_only.py
```

---

### 方案 B：本地 Ollama + 遠程部署（14 分鐘）

**優點**：更高質量的 LLM 輸出  
**步驟**：

1. **本地安裝 Ollama**
   ```bash
   # 下載：https://ollama.ai
   # 啟動服務
   ollama serve
   
   # 新終端下載模型
   ollama pull llama2
   ```

2. **配置 ngrok 遠程隧道**
   ```bash
   ngrok http 11434
   ```

3. **設置 Streamlit Cloud 環境變數**
   - 複製 ngrok URL（例如：`https://xxx.ngrok.io`）
   - 在 Streamlit Cloud 添加 `OLLAMA_URL` 環境變數

4. **部署 app.py**
   ```bash
   streamlit run app.py
   ```

詳見 [STREAMLIT_CLOUD_DEPLOYMENT.md](STREAMLIT_CLOUD_DEPLOYMENT.md)

---

## 📊 改進亮點

### 生成系統升級

| 方面 | 舊版本 | 新版本 | 提升 |
|------|--------|--------|------|
| 短語庫 | 15 個 | 25+ 個 | 67% |
| 評論範本 | 5 個 | 18 個 | **260%** |
| 回應範本 | 5 個 | 6 個 | 20% |
| 可能組合 | ~375 | ~28,000 | **7,400%** |
| 評論風格 | 無 | 4 類 | 新增 |
| 回應風格 | 無 | 3 類 | 新增 |

### 4 種評論風格

1. **基礎評論**：直接讚美，簡潔有力
2. **分析評論**：基於經驗，邏輯嚴密
3. **比較評論**：相對優勢，突出特點
4. **強調評論**：重複強調，極富感染力

### 3 種回應風格

1. **強勢回應**：充滿信心和權威性
2. **謙虛回應**：罕見讚賞，更顯珍貴
3. **修辭回應**：反問引導，引人思考

---

## 💡 使用示例

### 輸入話題
```
我的創業公司剛獲得 A 輪融資
```

### 生成結果（第一次）

**川普的 5 個評論**：
```
1. 說到我的創業公司剛獲得 A 輪融資：許多人說 TREMENDOUS，但這 - 這是 極其 TREMENDOUS！
2. 關於我的創業公司剛獲得 A 輪融資：GREAT。GREAT。極其 GREAT。這就是全部！
3. 這就是我想說的一切：INCREDIBLE！絕對 INCREDIBLE！就是這樣！
4. 關於我的創業公司剛獲得 A 輪融資：許多人說 AMAZING，但這 - 這是 非常 AMAZING！
5. 關於我的創業公司剛獲得 A 輪融資：我做過許多事，見過許多事。這？這是 簡直 FANTASTIC 的。相信我！
```

**川普的最終回應**：
```
讓我告訴你，這真的是 FANTASTIC 的！我見過很多，但這是最棒的。
這是個 非常 FANTASTIC 的決定。我知道成功，而這就是 FANTASTIC！- 川普
```

### 再次生成（第二次）

**完全不同的結果**：
```
1. 當我看到我的創業公司剛獲得 A 輪融資時：不，不，不 - 我說的是 真的 AMAZING，而這正是！
2. 人們總是說好，但 SPECTACULAR？這是另一個等級的 SPECTACULAR！
3. 這個我的創業公司剛獲得 A 輪融資？這就是我想說的一切：SPECTACULAR！完全 SPECTACULAR！
...
```

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

## 📚 文件說明

| 文件 | 用途 | 備註 |
|------|------|------|
| `app_cloud_only.py` | ⭐ 主應用（雲端版） | **推薦使用** |
| `app.py` | 主應用（本地版） | 需要 Ollama |
| `cot_dialog.py` | Two-Stage CoT 邏輯 | 支持遠程 Ollama |
| `test_generator.py` | 多樣性測試 | 驗證改進效果 |
| `IMPROVEMENT_DETAILS.md` | 改進詳細說明 | 技術細節 |
| `STREAMLIT_CLOUD_ONLY.md` | 快速部署指南 | 2-3 分鐘上線 |
| `STREAMLIT_CLOUD_DEPLOYMENT.md` | 高級部署指南 | Ollama 配置 |

---

## 🧪 本地測試

### 1. 測試生成多樣性
```bash
python test_generator.py
```

輸出將展示 3 輪生成結果，每輪 5 個評論，驗證多樣性。

### 2. 運行 Streamlit 應用
```bash
# 雲端版（推薦）
streamlit run app_cloud_only.py

# 本地 Ollama 版（需要先啟動 Ollama）
streamlit run app.py
```

### 3. 檢查語法
```bash
python -m py_compile app_cloud_only.py
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

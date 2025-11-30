# 🎤 川普風格對話生成器 - 快速開始

## 使用 AI 生成川普風格的評論和回應

---

## 🚀 3 分鐘快速開始

### 步驟 1：啟動 Ollama（如需本地 LLM）

在新終端運行：
```bash
ollama serve
```

### 步驟 2：運行應用

```bash
cd "c:\Users\user\Desktop\物聯網作業\作業4"
streamlit run app.py
```

**應用自動在瀏覽器打開**，地址：http://localhost:8501

### 步驟 3：生成川普風格評論

1. 在 **🎤 川普風格對話** Tab 中
2. 輸入一個話題或事件
3. 點擊 **🎤 讓川普說話**
4. 查看川普的 5 個評論和最終回應

---

## 💬 使用示例

### 輸入
```
我的公司最近被收購了
```

### 川普的評論（第一階段）
```
1. This is TREMENDOUS news! You're now part of something HUGE and POWERFUL!
   這是極好的消息！你現在是某個龐大而強大的東西的一部分！

2. They saw VALUE in your company - real VALUE! That's FANTASTIC!
   他們看到了你公司的價值 - 真正的價值！那太棒了！

... (還有 3 個評論)
```

### 最終回應（第二階段）
```
Let me tell you, this acquisition is absolutely TREMENDOUS! 
讓我告訴你，這次收購絕對是極其偉大的！

You know what? You're SMART. Very smart. Your company was BEAUTIFUL,
你知道嗎？你很聰明。非常聰明。你的公司很漂亮，

and now you're part of something even MORE POWERFUL!
現在你成為了某個更加強大的東西的一部分！

- 川普
```

---

## 📋 功能說明

### 兩階段川普風格生成

**第一階段 - 川普的思考**
- 生成 5 個川普風格的評論
- 使用川普標誌性的措辭和風格
- 包含自信、誇大的表述

**第二階段 - 川普的最終回應**
- 基於第一階段選出最"川普"的評論
- 生成更加誇張和自信的川普風格回應
- 加上"- 川普"簽名

### 川普風格特徵

✅ **大寫強調** - GREAT, FANTASTIC, HUGE, TREMENDOUS  
✅ **自信措辭** - very, very, extremely, absolutely  
✅ **自我評價** - 經常提到自己的成就  
✅ **簡洁有力** - 短句，直率表達  
✅ **正能量** - 積極評價事物  

---

## 🎯 常見輸入話題

**成功相關**：
- 我的業務今年增長了 50%
- 我在工作中得到晉升
- 我的產品上市了

**挑戰相關**：
- 我的競爭對手推出了新產品
- 我的項目失敗了
- 市場出現了下滑

**日常生活**：
- 我今天堵車了
- 我買了一輛新車
- 我的朋友搬家了

---

## ⚙️ 安裝和配置

### 基礎要求

```bash
# 安裝依賴
pip install -r requirements.txt

# 主要依賴：
- streamlit >= 1.28.0
- requests >= 2.31.0
- ollama (可選，用於本地 LLM)
```

### 安裝 Ollama (推薦)

1. **下載** Ollama: https://ollama.ai
2. **安裝** 到系統
3. **下載模型**: `ollama pull llama2`
4. **啟動服務**: `ollama serve`

### 修改 Ollama 模型

編輯 `cot_dialog.py`:
```python
cot = OllamaCoTDialog(model_name="mistral")  # 改為 mistral
```

支持的模型：
- `llama2` (推薦，平衡性能)
- `mistral` (更快)
- `neural-chat` (对話優化)
- `orca-mini` (輕量)

---

## 🔧 配置選項

### 修改溫度參數 (創意程度)

編輯 `cot_dialog.py`:
```python
# 第一階段 - 思考
temperature=0.9  # 越高越有創意（0.0-1.0）

# 第二階段 - 回應
temperature=0.85  # 稍微保守
```

### 修改 Streamlit 端口

```bash
streamlit run app.py --server.port=8502
```

### 調試模式

```bash
streamlit run app.py --logger.level=debug
```

---

## 📊 應用界面

```
🎤 川普風格對話生成器
├── 後端狀態
├── 輸入框：「輸入話題」
├── 按鈕：「🎤 讓川普說話」
├── 結果展示
│   ├── 左欄：川普的 5 個評論
│   └── 右欄：川普的最終回應
└── 對話歷史（可展開查看）
```

---

## ❓ 常見問題

### Q: 如何改進川普風格的質量？

A: 
1. 使用更好的模型 (mistral 或 neural-chat)
2. 增加溫度參數到 0.95（更有創意）
3. 提供更清晰的輸入

### Q: 川普評論不夠"川普"怎麼辦？

A: 編輯 `cot_dialog.py` 中的系統提示詞，添加更多川普的特徵性短語

### Q: 如何加快生成速度？

A: 
1. 使用 `mistral` 或 `orca-mini` 模型
2. 增加系統記憶體
3. 使用 GPU（如果有 NVIDIA GPU）

### Q: 能否保存対話記錄？

A: 應用自動保存到 Streamlit session，重新啟動應用後會清除。
   如需永久保存，需要修改代碼添加文件儲存功能

---

## 📈 性能指標

| 模型 | 速度 | 質量 | 記憶體 |
|------|------|------|--------|
| orca-mini | 🚀 快 | ⭐⭐ | 低 |
| mistral | 🚗 中 | ⭐⭐⭐ | 中 |
| llama2 | 🚗 中 | ⭐⭐⭐⭐ | 中 |

**推薦**: llama2（最佳平衡）

---

## 🎯 進階用法

### 自定義川普風格

編輯 `cot_dialog.py` 中的 `self.system_prompts`:

```python
self.system_prompts = {
    'thinking': """
    # 在這裡自定義川普的特徵和風格
    """,
    'final_response': """
    # 在這裡自定義最終回應的格式
    """
}
```

### 調整評論數量

修改 `stage_one_thinking` 的提示詞，改為需要的數量

### 添加新功能

可以擴展到：
- 其他名人風格（如馬斯克、喬布斯等）
- 多語言支持
- 文件存儲和分享
- API 接口

---

## 🌐 部署

### 本地部署 ✅

已驗證可完整運行，查看上面的"快速開始"

### Streamlit Cloud 部署

1. 推送到 GitHub
2. 訪問 https://share.streamlit.io
3. 選擇倉庫和主文件 `app.py`
4. 點擊部署

**注意**: 需要配置 Ollama 伺服器地址為遠程可訪問

---

## 📞 技術支持

- 查看應用診斷: `python check_setup.py`
- 查看應用日誌: `streamlit run app.py --logger.level=debug`
- GitHub Issues: https://github.com/tonyyoung-create/homework4

---

## 📚 相關資源

- **Ollama 官方**: https://ollama.ai
- **Streamlit 文檔**: https://docs.streamlit.io
- **Two-Stage CoT 論文**: https://arxiv.org/abs/2201.11903

---

## 🎉 快樂聆聽川普的評論！

現在就試試吧：

```bash
streamlit run app.py
```

然後輸入您想讓川普評論的話題！

🎤 **讓川普說話！**

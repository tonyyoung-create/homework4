## Ollama 安裝和配置指南

本應用使用 **Ollama** 進行本地 LLM 推理。以下是完整的安裝步驟。

### 1️⃣ 什麼是 Ollama?

Ollama 是一個輕量級的 LLM 運行時，允許在本地運行大型語言模型（如 Llama 2），無需 GPU 或雲服務。

**優點：**
- ✅ 完全本地運行（隱私保護）
- ✅ 無需 API 密鑰
- ✅ 支持多種模型
- ✅ 低系統要求

### 2️⃣ 安裝 Ollama

#### Windows

1. **下載 Ollama**
   - 訪問 https://ollama.ai
   - 點擊 "Download" → 選擇 Windows 版本
   - 下載 `OllamaSetup.exe`

2. **安裝**
   - 雙擊 `OllamaSetup.exe`
   - 按照安裝嚮導完成安裝
   - 安裝到默認位置（如 `C:\Users\<YourUser>\AppData\Local\Programs\Ollama`）

3. **驗證安裝**
   ```powershell
   ollama --version
   ```
   應該顯示版本號，如 `ollama version 0.1.0`

#### macOS

```bash
# 使用 Homebrew
brew install ollama

# 或直接下載
# https://ollama.ai/download/mac
```

#### Linux

```bash
# Ubuntu/Debian
curl https://ollama.ai/install.sh | sh

# 其他發行版請訪問 https://ollama.ai/download/linux
```

### 3️⃣ 下載模型

Ollama 支持多種模型。對於本應用，我們推薦 **Llama 2**。

```bash
# 下載 Llama 2 (約 4GB)
ollama pull llama2

# 其他可選模型：
ollama pull mistral      # Mistral 模型
ollama pull neural-chat  # Neural Chat 模型
ollama pull orca-mini    # Orca Mini（輕量）

# 查看已下載的模型
ollama list
```

**模型大小參考：**
| 模型 | 大小 | 記憶體需求 | 推薦配置 |
|------|------|----------|--------|
| orca-mini | 1.7GB | 3GB | 低端設備 |
| mistral | 4.1GB | 8GB | 中等設備 |
| llama2 | 3.8GB | 8GB | 中等設備 |
| llama2-13b | 7.4GB | 16GB | 高端設備 |

### 4️⃣ 啟動 Ollama 服務

#### 方式 1: 後台運行（推薦）

**Windows:**
```powershell
# Ollama 已設置為自動啟動服務，檢查狀態：
wmic process list brief | find "ollama"

# 或者手動啟動
ollama serve
```

**macOS/Linux:**
```bash
# 在後台運行
ollama serve &

# 或使用 nohup
nohup ollama serve > ollama.log 2>&1 &
```

#### 方式 2: 測試連接

```bash
# 測試 Ollama API
curl http://localhost:11434/api/tags

# 如果返回 JSON，說明服務已成功啟動
```

### 5️⃣ 啟動應用

一旦 Ollama 服務正在運行，您可以啟動應用：

```bash
# 安裝依賴
pip install -r requirements.txt

# 運行應用
streamlit run app.py
```

應用將在 http://localhost:8501 打開

### 6️⃣ 排查常見問題

#### 問題 1: "無法連接到 Ollama 服務"

**解決方案：**
```bash
# 1. 確保 Ollama 正在運行
ollama serve

# 2. 檢查服務是否在監聽
netstat -an | grep 11434  # Linux/macOS
netstat -an | findstr 11434  # Windows

# 3. 測試連接
curl http://localhost:11434/api/tags
```

#### 問題 2: "模型加載失敗"

**解決方案：**
```bash
# 1. 重新下載模型
ollama pull llama2

# 2. 檢查磁盤空間（需要至少 5GB 空閒）
df -h  # Linux/macOS
wmic logicaldisk get size,freespace  # Windows

# 3. 清理舊模型（如需要）
ollama rm llama2
```

#### 問題 3: "應用響應緩慢"

**解決方案：**
```bash
# 1. 檢查 Ollama 進程消耗的資源
# Windows: 打開任務管理器，查看 ollama.exe 的 CPU 和記憶體
# Linux: top 或 htop

# 2. 嘗試使用較小的模型
ollama pull orca-mini

# 3. 增加請求超時時間（編輯 cot_dialog.py）
# 將 timeout=120 改為更大的值
```

### 7️⃣ 高級配置

#### 自定義模型位置

```bash
# 設置模型保存路徑（Windows）
$env:OLLAMA_MODELS = "C:\Your\Custom\Path"
ollama serve

# Linux/macOS
export OLLAMA_MODELS=/path/to/models
ollama serve
```

#### 使用 GPU 加速

**NVIDIA GPU (CUDA):**
```bash
# 自動檢測 CUDA
ollama serve

# 手動指定
export CUDA_VISIBLE_DEVICES=0
ollama serve
```

**AMD GPU:**
```bash
# 需要 ROCm 支持
export HSA_OVERRIDE_GFX_VERSION=gfx906
ollama serve
```

### 8️⃣ 驗證安裝完成

運行以下命令確保一切正常：

```bash
# 1. 檢查 Ollama 版本
ollama --version

# 2. 啟動服務
ollama serve

# 3. 在新終端測試
curl http://localhost:11434/api/tags

# 4. 測試模型推理
ollama run llama2 "Hello, how are you?"
```

### 9️⃣ 文件夾結構參考

安裝完成後，您應該看到：

```
你的應用目錄/
├── app.py                    # 主應用入口
├── cot_dialog.py            # CoT 對話模組
├── deeplearning_app.py      # CRISP-DM 工具
├── data_layer.py            # 數據層
├── model_layer.py           # 模型層
├── evaluation_layer.py      # 評估層
├── requirements.txt         # 依賴列表
├── OLLAMA_SETUP.md         # 本文檔
└── .streamlit/
    └── config.toml          # Streamlit 配置
```

### 🔟 性能優化建議

1. **使用較小的模型進行測試**
   ```bash
   ollama pull orca-mini
   ```

2. **增加系統內存**
   - 推薦最少 8GB
   - 對於大型模型推薦 16GB

3. **使用 SSD 存儲**
   - 模型加載速度更快

4. **關閉其他應用**
   - 釋放系統資源

### 📖 更多資源

- **官方網站:** https://ollama.ai
- **模型庫:** https://ollama.ai/library
- **GitHub:** https://github.com/ollama/ollama
- **API 文檔:** https://ollama.ai/api
- **討論社區:** https://github.com/ollama/ollama/discussions

---

### ✅ 快速檢查清單

- [ ] 已下載並安裝 Ollama
- [ ] 已下載至少一個模型 (推薦: llama2)
- [ ] Ollama 服務正在運行 (http://localhost:11434)
- [ ] 已安裝 Python 依賴 (`pip install -r requirements.txt`)
- [ ] 應用啟動成功 (`streamlit run app.py`)
- [ ] 可以在 CoT Tab 中測試對話功能

完成以上步驟後，您就可以享受完全本地化的 AI 應用了! 🚀

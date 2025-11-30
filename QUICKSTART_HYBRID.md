# 🚀 AI 混合應用 - 快速開始指南

## 5 分鐘快速上手

### 📦 前置條件檢查

運行診斷工具確保環境設置正確：

```bash
cd 作業4
python check_setup.py
```

如果所有項都標記為 ✅，您可以直接跳到「運行應用」。  
如果有 ❌ 標記，請按照下面的步驟進行修復。

---

## ✅ 修復缺失的依賴

### 問題 1: PyTorch/TensorFlow 未安裝

如果您想使用 CRISP-DM 深度學習工具，需要安裝深度學習框架：

**安裝 PyTorch (推薦):**
```bash
# Windows/macOS/Linux - CPU 版本
pip install torch torchvision

# 如果有 GPU，使用 CUDA 加速版本
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

**或安裝 TensorFlow:**
```bash
pip install tensorflow
```

### 問題 2: Ollama 未安裝或服務未運行

要使用 Two-Stage CoT 對話功能，需要安裝並運行 Ollama：

**第 1 步：安裝 Ollama**

- **Windows**: 下載 https://ollama.ai/download
- **macOS**: `brew install ollama`
- **Linux**: `curl https://ollama.ai/install.sh | sh`

**第 2 步：下載模型**

```bash
# 下載 Llama 2 模型 (約 4GB)
ollama pull llama2

# 或下載更小的模型
ollama pull orca-mini
```

**第 3 步：啟動服務**

在一個新的終端窗口中運行：
```bash
ollama serve
```

此終端窗口需要保持打開。您應該看到類似的輸出：
```
binding 127.0.0.1:11434
```

**驗證服務已啟動：**
```bash
curl http://localhost:11434/api/tags
```

應該返回 JSON，其中包含已下載的模型列表。

---

## 🎯 運行應用

### 方式 1：簡單啟動（推薦）

```bash
cd "c:\Users\user\Desktop\物聯網作業\作業4"
streamlit run app.py
```

應用將自動在瀏覽器中打開，地址為：
```
http://localhost:8501
```

### 方式 2：手動設置端口

```bash
streamlit run app.py --server.port=8502
```

然後訪問：
```
http://localhost:8502
```

### 方式 3：指定主機 (用於遠程訪問)

```bash
streamlit run app.py --server.address=0.0.0.0
```

---

## 🤖 使用 CoT 對話功能

### 步驟 1：打開應用

應用打開後，您會看到兩個 Tab：
- 🤖 **對話軟體 (Two-Stage CoT)** ← 點擊此 Tab
- 📊 **深度學習工具 (CRISP-DM)**

### 步驟 2：輸入事件

在「發生了什麼事?」文本框中輸入一個負面事件：

```
示例：
- 今天開會遲到了
- 工作被老闆批評了
- 朋友忽視了我的建議
- 電腦崩潰了，丟失了文件
```

### 步驟 3：分析

點擊 **✨ 分析** 按鈕。

系統會顯示：
1. **🤔 思考過程** - 5 個理由為什麼這是好事
2. **✨ 最終回應** - 優化的正能量回應

### 步驟 4：查看歷史

向下滾動查看之前的對話記錄。

---

## 📊 使用 CRISP-DM 深度學習工具

### 步驟 1：打開 CRISP-DM Tab

點擊 **📊 深度學習工具 (CRISP-DM)** Tab。

### 步驟 2：選擇階段

在左側邊欄中選擇要進行的 CRISP-DM 階段：

1. **1️⃣ 業務理解** - 查看項目目標
2. **2️⃣ 數據理解** - 上傳或生成數據
3. **3️⃣ 數據準備** - 清理和準備數據
4. **4️⃣ 建模** - 訓練模型
5. **5️⃣ 評估** - 評估模型性能
6. **6️⃣ 部署** - 保存模型

### 步驟 3：按階段完成任務

每個階段都有具體的任務和工具。

**示例工作流：**
```
數據理解 → 點擊「生成數據」
    ↓
數據準備 → 執行數據預處理
    ↓
建模 → 選擇模型並訓練
    ↓
評估 → 查看性能指標
    ↓
部署 → 下載模型
```

---

## 🔧 常見問題速查

### Q: 應用無法啟動？

```bash
# 檢查依賴是否完整
pip list | grep streamlit
pip list | grep requests

# 重新安裝依賴
pip install -r requirements.txt --upgrade
```

### Q: CoT 功能無法使用？

```bash
# 1. 檢查 Ollama 是否運行
curl http://localhost:11434/api/tags

# 2. 如果失敗，啟動 Ollama
ollama serve

# 3. 檢查是否已下載模型
ollama list

# 4. 如果沒有模型，下載
ollama pull llama2
```

### Q: 模型很慢怎麼辦？

1. **使用更小的模型：**
   ```bash
   ollama pull orca-mini
   ```

2. **增加系統內存** - 至少 8GB，推薦 16GB

3. **檢查磁盤空間** - 至少需要 5GB 空閒

4. **關閉其他應用** - 釋放系統資源

### Q: 應用無法上傳超過 200MB 的文件？

編輯 `.streamlit/config.toml`：
```toml
[server]
maxUploadSize = 500  # 改為 500MB
```

### Q: 如何使用 GPU 加速？

**PyTorch (GPU 版本):**
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

**Ollama GPU 支持：**
```bash
# NVIDIA GPU (自動檢測)
ollama serve

# 手動指定 GPU
export CUDA_VISIBLE_DEVICES=0
ollama serve
```

---

## 📁 文件位置參考

| 文件 | 用途 |
|------|------|
| `app.py` | 主應用入口 |
| `cot_dialog.py` | CoT 對話邏輯 |
| `deeplearning_app.py` | CRISP-DM 工具 |
| `check_setup.py` | 診斷工具 |
| `OLLAMA_SETUP.md` | Ollama 詳細指南 |
| `README.md` | 完整文檔 |

---

## 🆘 需要更多幫助？

1. **Ollama 問題** → 查看 `OLLAMA_SETUP.md`
2. **深度學習問題** → 查看 `CRISP_DM_START.md`
3. **Streamlit 問題** → 訪問 https://docs.streamlit.io
4. **GitHub 問題** → https://github.com/tonyyoung-create/homework4/issues

---

## ✨ 快速測試

準備好後，運行以下命令進行快速測試：

```bash
# 1. 診斷系統
python check_setup.py

# 2. 啟動應用
streamlit run app.py

# 3. 在浏览器中打開
# http://localhost:8501

# 4. 測試 CoT 功能
# 進入「🤖 對話軟體」Tab
# 輸入事件，點擊「✨ 分析」
```

---

**祝您使用愉快! 🚀**

如有任何問題，歡迎查閱完整文檔或提交 Issue。

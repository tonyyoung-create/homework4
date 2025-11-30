# 🚀 Streamlit 完整運行指南

## ✅ 應用已成功在 Streamlit 上運行！

您的 **AI 混合應用** 已驗證可以完整運行在 Streamlit 上。

---

## 📋 系統要求

| 項目 | 需求 | 當前狀態 |
|------|------|--------|
| Python | 3.8+ | ✅ 3.13.7 |
| Streamlit | 1.28.0+ | ✅ 1.51.0 |
| requests | 2.31.0+ | ✅ 已安裝 |
| pandas | 2.0.0+ | ✅ 已安裝 |
| numpy | 1.24.0+ | ✅ 已安裝 |
| **可選**: PyTorch | 2.0.0+ | ⚠️ 用於 CRISP-DM |
| **可選**: TensorFlow | 2.13.0+ | ⚠️ 用於 CRISP-DM |
| **可選**: Ollama | - | ⚠️ 用於 CoT 對話 |

---

## 🎯 兩種運行模式

### 模式 1️⃣ : CoT 對話軟體 (開箱即用 ✅)

**要求**: 無特殊要求（只需 Python 基礎依賴）

**使用 Ollama 增強** (可選):
```bash
# 1. 安裝 Ollama: https://ollama.ai
# 2. 下載模型
ollama pull llama2

# 3. 啟動服務
ollama serve
```

### 模式 2️⃣ : CRISP-DM 深度學習工具 (需要額外依賴)

**要求**: 以下至少一種框架

**選項 A: 安裝 PyTorch (推薦)**
```bash
pip install torch torchvision
```

**選項 B: 安裝 TensorFlow**
```bash
pip install tensorflow
```

---

## 🚀 快速啟動 (3 步)

### 第 1 步：確保依賴已安裝

```bash
cd "c:\Users\user\Desktop\物聯網作業\作業4"

# 安裝基礎依賴
pip install -r requirements.txt

# 可選：安裝深度學習框架
pip install torch torchvision
```

### 第 2 步：(可選) 啟動 Ollama 服務

在新的終端窗口運行：
```bash
ollama serve
```

此終端保持打開狀態。

### 第 3 步：運行應用

```bash
streamlit run app.py
```

**自動打開**: 應用將自動在瀏覽器中打開  
**手動訪問**: http://localhost:8501

---

## 🎨 應用界面

應用提供兩個主要 Tab：

### Tab 1: 🤖 對話軟體 (Two-Stage CoT)

```
輸入事件 → 第一階段思考 → 第二階段回應 → 查看結果
```

**示例事件**:
- 今天走路被雨淋濕了
- 工作被老闆批評了
- 與朋友吵架了

**特性**:
- ✅ 本地運行（無需 API）
- ✅ 對話歷史記錄
- ✅ 支持多模型

**狀態**:
- 無 Ollama: ⚠️ 提示安裝
- 有 Ollama: ✅ 完全可用

### Tab 2: 📊 深度學習工具 (CRISP-DM)

```
業務理解 → 數據理解 → 數據準備 → 建模 → 評估 → 部署
```

**CRISP-DM 6 個階段**:
1. 業務理解 - 定義目標
2. 數據理解 - 加載和探索
3. 數據準備 - 清理和預處理
4. 建模 - 訓練模型
5. 評估 - 性能評估
6. 部署 - 保存模型

**狀態**:
- 無 PyTorch/TensorFlow: ❌ 提示安裝
- 有框架: ✅ 完全可用

---

## 📖 完整使用工作流

### 使用 CoT 對話功能

```
1. 打開應用 → http://localhost:8501
2. 進入「🤖 對話軟體」Tab
3. 輸入一個負面事件
4. 點擊「✨ 分析」按鈕
5. 查看第一階段的思考過程
6. 查看第二階段的最終回應
7. 向下滾動查看對話歷史
```

### 使用 CRISP-DM 工具

```
1. 打開應用 → http://localhost:8501
2. 進入「📊 深度學習工具」Tab
3. 在左側邊欄選擇 CRISP-DM 階段
4. 按照提示完成每個階段的任務
5. 查看統計信息和可視化結果
```

---

## ⚙️ 配置選項

### 修改 Streamlit 配置

編輯 `.streamlit/config.toml`:

```toml
[theme]
primaryColor = "#1f77b4"
backgroundColor = "#ffffff"
secondaryBackgroundColor = "#f0f0f0"

[server]
maxUploadSize = 200              # 最大上傳大小 (MB)
port = 8501                      # 端口
headless = false                 # 自動打開瀏覽器
```

### 修改端口

```bash
streamlit run app.py --server.port=8502
```

### 指定主機 (遠程訪問)

```bash
streamlit run app.py --server.address=0.0.0.0
```

---

## 🔧 常見問題

### Q1: 應用啟動後卡住了？

**解決方案**:
```bash
# 1. 檢查是否有現有的 Streamlit 進程
Get-Process streamlit

# 2. 終止所有 Streamlit 進程
Get-Process streamlit | Stop-Process -Force

# 3. 重新啟動應用
streamlit run app.py
```

### Q2: 無法訪問 http://localhost:8501？

**解決方案**:
```bash
# 檢查端口是否在監聽
netstat -ano | findstr "8501"

# 如果被占用，使用不同端口
streamlit run app.py --server.port=8502
```

### Q3: CoT 功能顯示「無法連接到 Ollama」？

**解決方案**:
```bash
# 1. 在新終端啟動 Ollama
ollama serve

# 2. 驗證服務已啟動
curl http://localhost:11434/api/tags

# 3. 重新加載 Streamlit 應用
```

### Q4: CRISP-DM 工具顯示「不可用」？

**解決方案**:
```bash
# 安裝深度學習框架
pip install torch torchvision

# 或
pip install tensorflow

# 重新啟動應用
```

### Q5: 應用很慢怎麼辦？

**優化建議**:
1. 使用較小的數據集進行測試
2. 減少模型複雜度
3. 檢查系統資源使用情況
4. 使用 GPU 加速（如果有 NVIDIA GPU）

---

## 📊 監控應用

### 查看應用日誌

```bash
# 啟用詳細日誌
streamlit run app.py --logger.level=debug
```

### 查看應用統計

應用會在 Tab 上方的側邊欄顯示：
- CoT 請求數
- ML 模型數
- 數據行數
- 模型訓練狀態

---

## 🌐 部署到 Streamlit Cloud

### 步驟 1: 上傳到 GitHub

```bash
git add -A
git commit -m "Ready for Streamlit Cloud deployment"
git push origin main
```

### 步驟 2: 部署

1. 訪問 https://share.streamlit.io/
2. 點擊「New app」
3. 選擇 GitHub 倉庫
4. 選擇分支: `main`
5. 選擇主文件: `app.py`
6. 點擊「Deploy」

### 步驟 3: 訪問

```
https://share.streamlit.io/YOUR_USERNAME/YOUR_REPO/main/app.py
```

**注意**: Streamlit Cloud 上需要配置環境變量以支持 Ollama。

---

## 📁 應用文件結構

```
應用目錄/
├── app.py                      # 主應用入口 ⭐
├── cot_dialog.py              # CoT 對話模組
├── deeplearning_app.py        # CRISP-DM 工具
├── data_layer.py              # 數據處理層
├── model_layer.py             # 模型定義層
├── evaluation_layer.py        # 評估層
├── check_setup.py             # 診斷工具
├── requirements.txt           # 依賴列表
├── OLLAMA_SETUP.md           # Ollama 指南
├── QUICKSTART_HYBRID.md      # 快速開始
└── .streamlit/
    └── config.toml            # Streamlit 配置
```

---

## ✅ 驗證清單

運行以下命令進行驗證：

```bash
# 1. 檢查應用配置
python check_setup.py

# 2. 測試導入
python -c "import app; print('✅ 應用導入成功')"

# 3. 啟動應用
streamlit run app.py

# 4. 訪問應用
# 自動打開或手動訪問 http://localhost:8501
```

---

## 🎓 額外資源

- **Streamlit 文檔**: https://docs.streamlit.io
- **Ollama 官方**: https://ollama.ai
- **PyTorch 教程**: https://pytorch.org/tutorials
- **TensorFlow 指南**: https://www.tensorflow.org/learn

---

## 📞 支持

如遇到問題：

1. 檢查 `check_setup.py` 診斷報告
2. 查看應用日誌 (`--logger.level=debug`)
3. 驗證所有依賴已安裝
4. 確保 Ollama 服務（如需要）已啟動

---

## 🎉 總結

您的 **AI 混合應用** 已準備好在 Streamlit 上完整運行！

✅ **CoT 對話軟體** - 開箱即用  
✅ **CRISP-DM 工具** - 安裝依賴後可用  
✅ **Streamlit 集成** - 完全驗證  
✅ **文檔完整** - 已提供  

**立即啟動**:
```bash
streamlit run app.py
```

祝您使用愉快! 🚀

# 🚀 快速命令參考卡

## ⚡ 最基本的 3 個命令

```bash
# 1. 安裝
pip install -r requirements.txt

# 2. 運行
streamlit run deeplearning_app.py

# 3. 打開
# 在瀏覽器中訪問 http://localhost:8501
```

---

## 📁 文件導航

| 文件 | 用途 | 命令 |
|------|------|------|
| `deeplearning_app.py` | 主應用 | `streamlit run deeplearning_app.py` |
| `data_layer.py` | 數據層 | `python data_layer.py` |
| `model_layer.py` | 模型層 | `python model_layer.py` |
| `evaluation_layer.py` | 評估層 | `python evaluation_layer.py` |

---

## 📚 文檔快速路由

| 你想... | 讀這個文件 | 時間 |
|--------|----------|------|
| 快速了解 | `CRISP_DM_START.md` | 5 分鐘 |
| 快速開始 | `QUICKSTART_DL.md` | 10 分鐘 |
| 完整指南 | `README_DL.md` | 30 分鐘 |
| 解決問題 | `QUICKSTART_DL.md` 的故障排查 | 5 分鐘 |

---

## 🎯 常見任務

### 任務 1：5 分鐘演示

```bash
streamlit run deeplearning_app.py
# 1. 選擇「2️⃣ 數據理解」
# 2. 點擊「生成示例數據」
# 3. 選擇「4️⃣ 建模」
# 4. 點擊「開始訓練」
# 5. 查看結果
```

### 任務 2：使用自己的數據

```bash
streamlit run deeplearning_app.py
# 1. 準備 data.csv 文件
# 2. 選擇「2️⃣ 數據理解」
# 3. 選擇「上傳 CSV 文件」
# 4. 上傳你的文件
# 5. 完成後續步驟
```

### 任務 3：調試和測試

```bash
# 測試數據層
python data_layer.py

# 測試模型層
python model_layer.py

# 測試評估層
python evaluation_layer.py
```

---

## 🔧 環境設置

```bash
# 創建虛擬環境（推薦）
python -m venv venv

# 激活虛擬環境
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 安裝依賴
pip install -r requirements.txt

# 運行應用
streamlit run deeplearning_app.py
```

---

## 📊 工作流速查

```
1️⃣ 業務理解
   ← 了解項目目標

2️⃣ 數據理解
   ← 加載數據
   ← 生成數據或上傳 CSV
   ← 探索統計信息

3️⃣ 數據準備
   ← 選擇預處理選項
   ← 點擊「執行預處理」

4️⃣ 建模
   ← 配置模型參數
   ← 點擊「開始訓練」
   ← 等待訓練完成

5️⃣ 評估
   ← 點擊「評估模型」
   ← 查看性能指標

6️⃣ 部署
   ← 保存模型
   ← 下載報告
```

---

## 🎓 CRISP-DM 快速表

| 階段 | 說明 | 模塊 |
|------|------|------|
| 業務理解 | 定義目標 | 應用 UI |
| 數據理解 | 加載和探索 | `data_layer.py` |
| 數據準備 | 清理和轉換 | `data_layer.py` |
| 建模 | 訓練模型 | `model_layer.py` |
| 評估 | 測試性能 | `evaluation_layer.py` |
| 部署 | 發布模型 | 應用 UI |

---

## 💾 保存和加載模型

```python
# 保存模型
import torch
torch.save(model.state_dict(), 'model.pth')

# 加載模型
model.load_state_dict(torch.load('model.pth'))
```

---

## 🔍 故障排查快速表

| 錯誤 | 解決方案 |
|------|---------|
| `ModuleNotFoundError` | `pip install -r requirements.txt` |
| GPU 未檢測到 | 正常，使用 CPU |
| 應用啟動慢 | 首次需要時間，耐心等待 |
| 訓練失敗 | 檢查數據和參數 |
| 內存不足 | 減少批大小 |

---

## 📞 快速聯繫

文件位置：`c:\Users\user\Desktop\物聯網作業\作業4\`

主要文件：
- `deeplearning_app.py` - 運行這個
- `README_DL.md` - 讀這個
- `QUICKSTART_DL.md` - 快速幫助

---

## ⚡ 一行命令快速開始

```bash
pip install -r requirements.txt && streamlit run deeplearning_app.py
```

然後訪問 http://localhost:8501

---

祝你使用愉快！🚀

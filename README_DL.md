# 🤖 深度學習應用 - CRISP-DM 方法論

## 📌 項目概述

這是一個完整的 **深度學習應用**，遵循 **CRISP-DM** (Cross-industry standard Process for Data Mining) 方法論。應用**本地運行**，**無需 API 調用**。

### ✨ 核心特點

- ✅ **完全本地運行** - 無需 API，無需網絡
- ✅ **遵循 CRISP-DM** - 6 階段完整工作流
- ✅ **深度學習框架** - PyTorch/TensorFlow
- ✅ **交互式界面** - Streamlit Web UI
- ✅ **端到端工作流** - 從數據到部署

---

## 🎯 CRISP-DM 6 個階段

### 1️⃣ 業務理解 (Business Understanding)
- 定義項目目標
- 評估形勢
- 制定項目計劃

### 2️⃣ 數據理解 (Data Understanding)
- 收集數據
- 探索數據特性
- 驗證數據質量
- 識別數據問題

### 3️⃣ 數據準備 (Data Preparation)
- 特征選擇
- 缺失值處理
- 異常值處理
- 特征縮放
- 數據轉換

### 4️⃣ 建模 (Modeling)
- 選擇建模技術
- 設計測試方法
- 構建深度學習模型
- 訓練模型

### 5️⃣ 評估 (Evaluation)
- 模型性能評估
- 混淆矩陣分析
- 性能指標計算
- 結果可視化

### 6️⃣ 部署 (Deployment)
- 模型部署
- 性能監控
- 生成報告
- 文檔化

---

## 📁 項目結構

```
作業4/
├── 📱 應用層
│   ├── deeplearning_app.py          # 主 Streamlit 應用
│   └── requirements.txt              # 依賴清單
│
├── 🔧 核心模塊
│   ├── data_layer.py                # 數據層（數據理解 + 準備）
│   ├── model_layer.py               # 模型層（建模）
│   ├── evaluation_layer.py          # 評估層（評估）
│   └── __init__.py                  # 初始化文件
│
├── 📊 模型
│   └── models/                      # 保存的模型
│
├── 📖 文檔
│   ├── README_DL.md                 # 本文件
│   ├── CRISP_DM_GUIDE.md           # CRISP-DM 詳細指南
│   └── QUICKSTART_DL.md            # 快速開始指南
│
└── 📝 配置
    └── .env                         # 環境配置
```

---

## 🚀 5 分鐘快速開始

### 步驟 1：安裝依賴

```bash
pip install -r requirements.txt
```

**預期時間：3-5 分鐘**

### 步驟 2：運行應用

```bash
streamlit run deeplearning_app.py
```

**預期時間：1-2 分鐘**

### 步驟 3：按照 6 個階段操作

1. **業務理解** - 了解項目目標
2. **數據理解** - 加載和探索數據
3. **數據準備** - 預處理數據
4. **建模** - 訓練深度學習模型
5. **評估** - 評估模型性能
6. **部署** - 保存並部署模型

---

## 💻 系統要求

### 必需

- **Python** 3.8+
- **內存** 至少 4GB（建議 8GB+）
- **磁盤空間** 至少 2GB

### 可選

- **CUDA** - GPU 加速訓練（推薦使用 NVIDIA GPU）
- **cuDNN** - CUDA 深度神經網絡加速庫

---

## 📚 模塊詳解

### 數據層 (`data_layer.py`)

**CRISP-DM 階段：** 業務理解 + 數據理解 + 數據準備

**主要類：**
- `DataExplorer` - 數據探索和分析
- `DataPreprocessor` - 數據預處理
- `DataVisualizer` - 數據可視化

**功能：**
```python
# 加載數據
explorer = DataExplorer()
data = explorer.load_data()

# 探索數據
info = explorer.explore_data()
quality_report = explorer.get_data_quality_report()

# 預處理數據
preprocessor = DataPreprocessor(data)
preprocessor.handle_missing_values(strategy='mean')
preprocessor.handle_outliers(method='iqr')
preprocessor.scale_features(method='standard')
processed_data = preprocessor.get_processed_data()
```

### 模型層 (`model_layer.py`)

**CRISP-DM 階段：** 數據準備 + 建模

**主要類：**
- `NeuralNetwork` - 全連接神經網絡
- `ConvolutionalNeuralNetwork` - CNN（圖像）
- `RecurrentNeuralNetwork` - RNN（序列）
- `ModelTrainer` - 模型訓練器

**功能：**
```python
# 創建模型
model = NeuralNetwork(
    input_size=10,
    hidden_sizes=[128, 64, 32],
    output_size=1,
    dropout_rate=0.3
)

# 訓練模型
trainer = ModelTrainer(model, learning_rate=0.001)
trainer.set_criterion(nn.BCEWithLogitsLoss())
history = trainer.train(train_loader, val_loader, epochs=50)

# 保存模型
trainer.save_model('model.pth')
```

### 評估層 (`evaluation_layer.py`)

**CRISP-DM 階段：** 評估

**主要類：**
- `ModelEvaluator` - 分類模型評估
- `RegressionEvaluator` - 迴歸模型評估
- `EvaluationReport` - 報告生成

**功能：**
```python
# 創建評估器
evaluator = ModelEvaluator(model)

# 進行預測
predictions = evaluator.predict(X_test)

# 評估模型
metrics = evaluator.evaluate(y_test)
# 返回: 準確率, 精準率, 召回率, F1, ROC-AUC

# 可視化
evaluator.plot_confusion_matrix()
evaluator.plot_roc_curve()
evaluator.plot_metrics_comparison()
```

---

## 🧠 深度學習模型詳解

### 1. 全連接神經網絡 (DNN)

適用於：表格數據、結構化數據

```
輸入層 → 隱層1 (128) → 隱層2 (64) → 隱層3 (32) → 輸出層
         ↓ ReLU       ↓ ReLU       ↓ ReLU
         ↓ Dropout    ↓ Dropout    ↓ Dropout
         ↓ BatchNorm  ↓ BatchNorm
```

### 2. 卷積神經網絡 (CNN)

適用於：圖像分類、計算機視覺

```
輸入 → Conv2D → ReLU → MaxPool → Conv2D → ReLU → MaxPool → FC層 → 輸出
```

### 3. 遞歸神經網絡 (RNN/LSTM)

適用於：序列數據、時間序列、自然語言處理

```
輸入序列 → LSTM層 → LSTM層 → FC層 → 輸出
```

---

## 📊 數據預處理流程

### 1. 缺失值處理
```
策略：mean（均值）、median（中位數）、drop（刪除）、forward_fill（前向填充）
```

### 2. 重複值移除
```
檢測並移除完全相同的行
```

### 3. 異常值處理
```
方法1：IQR（四分位距）- 保留在 Q1-1.5*IQR 到 Q3+1.5*IQR 之間
方法2：Z-Score - 保留在 ±3σ 之內
```

### 4. 特征縮放
```
標準化（Standard Scaler）：(x - mean) / std
最小最大化（MinMax Scaler）：(x - min) / (max - min)
```

---

## 🎯 評估指標詳解

### 分類任務

| 指標 | 說明 | 計算方式 |
|------|------|---------|
| **準確率** | 正確預測占總預測的比例 | TP + TN / Total |
| **精準率** | 正樣本預測準確度 | TP / (TP + FP) |
| **召回率** | 實際正樣本識別率 | TP / (TP + FN) |
| **F1 分數** | 精準率和召回率的調和平均 | 2 × (P × R) / (P + R) |
| **ROC-AUC** | ROC 曲線下面積 | 0-1，越大越好 |

### 迴歸任務

| 指標 | 說明 |
|------|------|
| **MSE** | 均方誤差 - 預測誤差平均平方 |
| **RMSE** | 均方根誤差 - MSE 的平方根 |
| **MAE** | 平均絕對誤差 - 預測誤差的絕對值平均 |
| **R²** | 決定系數 - 模型解釋力 (0-1) |

---

## 🔧 高級配置

### 模型架構自定義

```python
# 修改隱藏層大小
model = NeuralNetwork(
    input_size=20,
    hidden_sizes=[256, 128, 64, 32],  # 更深的網絡
    output_size=1,
    dropout_rate=0.5  # 更高的正則化
)
```

### 訓練參數調整

```python
trainer = ModelTrainer(
    model,
    learning_rate=0.0001,  # 更低的學習率
    device='cuda'  # 使用 GPU
)
```

### 數據預處理參數

```python
# 異常值處理
preprocessor.handle_outliers(
    method='zscore',
    threshold=3
)

# 特征縮放
preprocessor.scale_features(
    method='minmax',
    exclude_cols=['target', 'id']
)
```

---

## 📈 使用示例

### 完整工作流

```python
# 1. 數據理解
from data_layer import DataExplorer, DataPreprocessor

explorer = DataExplorer()
data = explorer.load_data('data.csv')
info = explorer.explore_data()

# 2. 數據準備
preprocessor = DataPreprocessor(data)
preprocessor.handle_missing_values()
preprocessor.handle_outliers()
preprocessor.scale_features()

# 3. 數據分割
X_train, X_test, y_train, y_test = preprocessor.get_split_data(
    test_size=0.2,
    target_col='target'
)

# 4. 建模
from model_layer import crisp_dm_modeling

result = crisp_dm_modeling(
    X_train, y_train, X_test, y_test,
    model_type='nn',
    epochs=50,
    batch_size=32
)

# 5. 評估
from evaluation_layer import crisp_dm_evaluation

eval_result = crisp_dm_evaluation(
    result['model'],
    X_test,
    y_test,
    task='classification'
)

print("準確率:", eval_result['metrics']['準確率 (Accuracy)'])
```

---

## 🚀 部署指南

### 本地部署

```bash
# 保存模型
torch.save(model.state_dict(), 'model.pth')

# 加載模型
model = NeuralNetwork(input_size=10, hidden_sizes=[128, 64, 32])
model.load_state_dict(torch.load('model.pth'))
```

### Docker 部署

```dockerfile
FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["streamlit", "run", "deeplearning_app.py"]
```

### 雲平台部署

- **AWS SageMaker** - Amazon 託管的 ML 服務
- **Google Cloud AI** - Google 的 ML 平台
- **Azure ML** - Microsoft 的機器學習服務

---

## 🐛 故障排查

### 問題 1：GPU 不被識別

```bash
# 檢查 CUDA
import torch
print(torch.cuda.is_available())
print(torch.cuda.get_device_name(0))
```

### 問題 2：內存不足

```python
# 減少批大小
batch_size = 8  # 改為更小的值

# 減少隱藏層大小
hidden_sizes = [64, 32]
```

### 問題 3：模型過擬合

```python
# 增加 Dropout
dropout_rate = 0.5

# 增加正則化
# 早停
early_stopping_patience = 5
```

---

## 📚 參考資源

### CRISP-DM
- [CRISP-DM 官方網站](https://www.crisp-dm.org/)
- [IBM CRISP-DM 指南](https://www.ibm.com/cloud/learn/data-mining)

### 深度學習
- [PyTorch 官方文檔](https://pytorch.org/)
- [TensorFlow 官方文檔](https://www.tensorflow.org/)
- [Deep Learning Book](https://www.deeplearningbook.org/)

### Streamlit
- [Streamlit 文檔](https://docs.streamlit.io/)
- [Streamlit 社區論壇](https://discuss.streamlit.io/)

---

## 💡 最佳實踐

1. **始終遵循 CRISP-DM** - 每個階段都很重要
2. **數據質量第一** - 垃圾進，垃圾出
3. **進行驗證** - 不要在測試集上調參數
4. **監控過擬合** - 檢查訓練/驗證損失
5. **記錄實驗** - 跟踪超參數和結果
6. **保存模型** - 定期備份
7. **文檔化** - 記錄決策和理由

---

## 🎓 學習路徑

**初級 (Week 1)**
- [ ] 理解 CRISP-DM 流程
- [ ] 運行示例應用
- [ ] 加載和探索數據

**中級 (Week 2-3)**
- [ ] 預處理不同類型的數據
- [ ] 構建和訓練模型
- [ ] 評估模型性能

**高級 (Week 4+)**
- [ ] 自定義模型架構
- [ ] 超參數調優
- [ ] 部署和監控

---

## 🎉 完成清單

在使用此應用前，確保：

- [ ] Python 3.8+ 已安裝
- [ ] 依賴已通過 `pip install -r requirements.txt` 安裝
- [ ] 了解 CRISP-DM 的 6 個階段
- [ ] 有可用的訓練數據（或使用示例數據）
- [ ] GPU（可選但推薦）已配置

---

## 📞 支援和反饋

遇到問題？

1. 查看本文檔的故障排查部分
2. 檢查 [Streamlit 文檔](https://docs.streamlit.io/)
3. 查閱 [PyTorch 文檔](https://pytorch.org/docs/)
4. 在社區尋求幫助

---

**創建日期：** 2025 年 11 月 30 日
**最後更新：** 2025 年 11 月 30 日
**版本：** 1.0.0

祝你使用愉快！🚀

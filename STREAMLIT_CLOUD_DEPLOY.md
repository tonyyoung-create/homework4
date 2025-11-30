# 📤 Streamlit Community Cloud 部署指南

## 快速部署步驟

### 1️⃣ 前置需求
- GitHub 帳戶
- Streamlit Community Cloud 帳戶
- 項目上傳至 GitHub

### 2️⃣ GitHub 上傳步驟

```bash
# 1. 初始化 Git 倉庫
git init

# 2. 添加所有文件
git add .

# 3. 提交更改
git commit -m "Add deep learning CRISP-DM app for Streamlit Cloud"

# 4. 添加遠程倉庫
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git

# 5. 推送到 GitHub
git branch -M main
git push -u origin main
```

### 3️⃣ Streamlit Cloud 部署

1. **訪問** https://share.streamlit.io/
2. **點擊** "New app"
3. **選擇** GitHub 倉庫
4. **主文件** 選擇 `deeplearning_app.py`
5. **點擊** "Deploy"

### 4️⃣ 部署完成

等待約 2-3 分鐘後，應用即可在以下地址訪問：
```
https://share.streamlit.io/YOUR_USERNAME/YOUR_REPO_NAME/main/deeplearning_app.py
```

## 📋 項目文件檢查清單

✅ 必需文件：
- [ ] `deeplearning_app.py` - 主應用
- [ ] `data_layer.py` - 數據層
- [ ] `model_layer.py` - 模型層  
- [ ] `evaluation_layer.py` - 評估層
- [ ] `requirements.txt` - 依賴文件
- [ ] `.streamlit/config.toml` - Streamlit 配置
- [ ] `.gitignore` - Git 忽略配置

✅ 文檔文件：
- [ ] `README_DL.md` - 項目說明
- [ ] `QUICKSTART_DL.md` - 快速開始
- [ ] `CRISP_DM_START.md` - 方法論說明

## 🔧 常見問題排查

### Q: 應用無法啟動？
**A:** 檢查 `requirements.txt` 中是否有舊版本依賴
- 更新為兼容版本
- 移除不必要的依賴

### Q: 模型加載失敗？
**A:** 確保所有模型文件都在項目目錄中
- 避免使用絕對路徑
- 使用相對路徑引用文件

### Q: 內存不足？
**A:** Streamlit Cloud 資源有限
- 減少數據集大小
- 使用輕量級模型
- 優化函數性能

## 📊 性能優化建議

1. **緩存計算結果**
   ```python
   @st.cache_data
   def load_data():
       return pd.read_csv("data.csv")
   ```

2. **使用會話狀態存儲狀態**
   ```python
   if 'model' not in st.session_state:
       st.session_state.model = None
   ```

3. **限制數據集大小**
   - 實際部署應使用樣本數據
   - 避免加載超大文件

## 🔐 環保和安全

- ✅ 所有計算在用戶瀏覽器中執行
- ✅ 無需 API 密鑰或密碼
- ✅ 數據不上傳到外部服務
- ✅ 完全本地化部署

## 📞 獲取幫助

- Streamlit 文檔：https://docs.streamlit.io/
- GitHub Issues：https://github.com/streamlit/streamlit/issues
- Streamlit 論壇：https://discuss.streamlit.io/

---

**最後修改:** 2025-11-30
**狀態:** ✅ 準備就緒

# 🚀 Streamlit Cloud 快速部署 - 3 步完成

## 最快的方案：使用 ngrok

### 步驟 1️⃣: 安裝 ngrok (2 分鐘)

```bash
# Windows: 用 Chocolatey
choco install ngrok

# macOS: 用 Homebrew
brew install ngrok

# 或直接下載: https://ngrok.com/download
```

### 步驟 2️⃣: 啟動 Ollama + ngrok (1 分鐘)

**終端 1: 啟動 Ollama**
```bash
ollama serve
# 等待: server started on 127.0.0.1:11434
```

**終端 2: 建立 ngrok 隧道**
```bash
ngrok http 11434

# 您會看到類似的輸出:
# Forwarding  https://abcd1234-efgh.ngrok.io -> http://localhost:11434
# 
# 複製這個 URL: https://abcd1234-efgh.ngrok.io
```

### 步驟 3️⃣: 部署到 Streamlit Cloud (2 分鐘)

#### 3.1 代碼已推送 ✅

```bash
# 已完成，無需操作
# 提交 6383c9d 已推送
```

#### 3.2 進入 Streamlit Cloud

訪問: https://share.streamlit.io

按鈕: **New app**

選擇：
- **Repository**: `tonyyoung-create/homework4`
- **Branch**: `main`
- **Main file path**: `app.py`

點擊: **Deploy**

等待 2-5 分鐘...

#### 3.3 配置 Secrets

部署後，進入您的應用：

1. 點擊右上角 ⚙️ **Settings**
2. 左側選擇 **Secrets**
3. 粘貼以下內容：

```toml
OLLAMA_URL = "https://abcd1234-efgh.ngrok.io"
```

> ⚠️ 替換成您的 ngrok URL

4. 點擊 **Save**

應用會自動重新加載！

---

## ✅ 測試成功

在應用中應該看到：

```
✅ Ollama: 連接成功
後端狀態: 🟢 已連接
Model: llama2
```

然後輸入任何話題，享受川普風格的評論！🎤

---

## 📊 整個流程時間線

| 步驟 | 時間 | 狀態 |
|------|------|------|
| 1. 安裝 ngrok | 2 分鐘 | 🟢 |
| 2. 啟動 Ollama + ngrok | 1 分鐘 | 🟢 |
| 3. 部署到 Streamlit | 5 分鐘 | 🟢 |
| 4. 配置 Secrets | 1 分鐘 | 🟢 |
| **總計** | **9 分鐘** | ✅ |

---

## ⚠️ ngrok URL 變化問題

**問題**: 每次重啟 ngrok，URL 會變化

**解決方案 1: 免費方案（每次更新）**
```
每次重啟 ngrok 後：
1. 複製新 URL
2. 進入 Streamlit Cloud Settings → Secrets
3. 更新 OLLAMA_URL
4. 應用重新加載
```

**解決方案 2: 付費方案（固定 URL）**
```
ngrok 付費 Pro: $10/月
- 獲得固定靜態 URL
- 無需每次更新
```

**解決方案 3: 購買 VPS（完全穩定）**
```
DigitalOcean: $5-10/月
- 完全控制
- 無流量限制
- 永久 URL
```

---

## 🔍 故障排除

### 問題：Ollama 連接失敗

```
❌ HTTPConnectionPool connection refused
```

**檢查清單**:
- [ ] ngrok 隧道還在運行？(`ngrok http 11434`)
- [ ] URL 是否已複製到 Secrets？
- [ ] Secrets 是否已保存？
- [ ] URL 格式是否正確？(以 https:// 開頭)

### 問題：Secrets 未生效

**解決方案**:
1. 複製 URL 到 Secrets
2. 點擊 **Save**
3. 等待 10 秒
4. 重新載入應用 (Ctrl+R)

### 問題：模型加載中...

這是正常的！

```
⏳ 首次調用模型時會下載和加載
   耗時: 30-60 秒

✅ 之後會快得多
```

---

## 🎯 現在您可以

✅ **分享應用 URL** 給任何人  
✅ **從任何地方訪問** (手機、平板、電腦)  
✅ **生成川普風格評論** 在雲端  
✅ **無需本地運行** Streamlit  

### 應用 URL

```
https://your-username-appname-xxxxx.streamlit.app
```

---

## 📚 完整資源

- **Streamlit Cloud**: https://share.streamlit.io
- **ngrok 文檔**: https://ngrok.com/docs
- **部署指南**: 查看 `STREAMLIT_CLOUD_DEPLOYMENT.md`

---

## 💡 下一步選擇

### 如果 ngrok 不穩定 → 選 VPS
查看 `STREAMLIT_CLOUD_DEPLOYMENT.md` → 方案 B

### 如果想要固定 URL → 升級 ngrok Pro
訪問: https://ngrok.com/pricing

### 如果想要完全控制 → 使用 Docker
部署到 Render、Railway 等

---

**就這麼簡單！祝您部署順利！🚀**

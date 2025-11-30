# 🚀 Streamlit Cloud 部署指南

將川普風格對話生成器部署到 Streamlit Cloud

---

## 📋 前置要求

- ✅ 代碼已推送到 GitHub (commit 19541fe)
- ✅ Ollama 支持環境變數配置 (已更新)
- ✅ 遠程 Ollama 服務可用或 ngrok 隧道已建立

---

## 🎯 兩個部署方案

### 方案 A: 使用 ngrok 隧道（推薦 - 簡單）

**優點**：
- ✅ 快速簡單
- ✅ 無需購買服務器
- ✅ 本地 Ollama 立即可用

**缺點**：
- ⚠️ ngrok 免費版有流量限制
- ⚠️ 隧道 URL 每次重啟會變化

#### A1: 安裝 ngrok

訪問 https://ngrok.com 註冊和下載

```bash
# Windows 安裝
choco install ngrok
# 或下載然後解壓

# macOS
brew install ngrok

# Linux
# 下載二進制文件
```

#### A2: 啟動 Ollama 和 ngrok

**終端 1: 啟動 Ollama**
```bash
ollama serve
# 輸出: server started on 127.0.0.1:11434
```

**終端 2: 建立 ngrok 隧道**
```bash
ngrok http 11434
# 輸出類似:
# Forwarding                    https://xxxxx.ngrok.io -> http://localhost:11434
```

複製 ngrok URL（例如：`https://xxxxx.ngrok.io`）

#### A3: 在 Streamlit Cloud 上配置

1. 訪問 https://share.streamlit.io
2. 選擇倉庫: `tonyyoung-create/homework4`
3. 部署應用: `app.py`
4. 進入應用 → Settings → Secrets

在 **Secrets** 中添加：
```toml
OLLAMA_URL = "https://xxxxx.ngrok.io"
```

> ⚠️ 每次 ngrok 重啟後，URL 會變化，需要更新 Secrets

---

### 方案 B: 使用遠程 Ollama 服務器

**優點**：
- ✅ 穩定可靠
- ✅ URL 不會變化

**缺點**：
- ⚠️ 需要購買 VPS 或雲服務器
- ⚠️ 需要 Linux 服務器配置

#### B1: 購買 VPS

推薦服務：
- AWS EC2 (t3.micro 免費層)
- DigitalOcean ($4-6/月)
- Linode ($5/月)
- Google Cloud (免費層)

#### B2: 在服務器上安裝 Ollama

```bash
# SSH 連接到服務器
ssh user@your-server.com

# 下載並安裝 Ollama
curl https://ollama.ai/install.sh | sh

# 啟動 Ollama（後台運行）
ollama serve &

# 下載模型
ollama pull llama2

# 確保防火牆允許 11434 端口
# 編輯防火牆規則允許外部訪問
```

#### B3: 在 Streamlit Cloud 上配置

在 **Secrets** 中添加：
```toml
OLLAMA_URL = "http://your-server-ip:11434"
```

---

## 📝 逐步部署流程

### 步驟 1: 更新代碼（已完成 ✅）

代碼已支持環境變數，無需進一步修改。

### 步驟 2: 選擇方案並設置

**選 A (ngrok)** → 執行 ngrok 隧道設置  
**選 B (遠程服務器)** → 購買並配置 VPS

### 步驟 3: 推送到 GitHub

```bash
cd "c:\Users\user\Desktop\物聯網作業\作業4"
git add -A
git commit -m "feat: 添加遠程 Ollama 支持"
git push origin main
```

### 步驟 4: 部署到 Streamlit Cloud

1. 訪問 https://share.streamlit.io
2. 選擇 GitHub 倉庫: `tonyyoung-create/homework4`
3. 選擇分支: `main`
4. 選擇文件: `app.py`
5. 點擊 **Deploy**

等待部署完成（通常 2-5 分鐘）

### 步驟 5: 配置 Secrets

1. 部署後進入應用
2. 點擊右上角 **Settings**
3. 選擇 **Secrets**
4. 添加：
   ```toml
   OLLAMA_URL = "你的 Ollama 遠程 URL"
   ```
5. 保存並重新加載應用

### 步驟 6: 測試

在應用中輸入話題，如果成功連接，應該看到：

```
✅ Ollama: 連接成功
後端狀態: 🟢 已連接
Model: llama2
```

---

## 🔧 故障排除

### 問題 1: Ollama 連接失敗

```
❌ Ollama 連接失敗: HTTPConnectionPool
```

**解決方案**:
1. 檢查 OLLAMA_URL 是否正確
2. 檢查遠程服務是否正在運行
3. 檢查防火牆設置是否允許連接
4. 檢查 Secrets 是否已保存

### 問題 2: ngrok 隧道 URL 已過期

```
❌ Connection refused
```

**解決方案**:
1. 重新啟動 ngrok
2. 複製新的 URL
3. 更新 Streamlit Cloud Secrets
4. 應用將自動重新加載

### 問題 3: 連接超時

```
❌ Connection timeout
```

**解決方案**:
1. 檢查遠程服務器是否在線
2. 檢查模型是否已下載 (`ollama pull llama2`)
3. 增加超時時間（編輯 cot_dialog.py）
4. 檢查網絡連接

### 問題 4: 模型未找到

```
❌ Model 'llama2' not found
```

**解決方案**:
在遠程服務器上下載模型：
```bash
ollama pull llama2
```

---

## 📊 性能對比

| 方案 | 成本 | 穩定性 | 複雜度 | 推薦 |
|------|------|--------|--------|------|
| **ngrok** | 免費 | ⭐⭐⭐ | ⭐ | ✅ 入門 |
| **VPS** | $5-10/月 | ⭐⭐⭐⭐⭐ | ⭐⭐ | ✅ 生產 |

---

## 🚀 快速檢查清單

部署前：
- [ ] 代碼已推送到 GitHub
- [ ] cot_dialog.py 支持環境變數 (已完成)
- [ ] Ollama 服務已配置

部署時：
- [ ] 選擇部署方案 (ngrok 或 VPS)
- [ ] 設置遠程 Ollama
- [ ] 部署到 Streamlit Cloud
- [ ] 配置 Secrets

部署後：
- [ ] 應用成功加載
- [ ] Ollama 連接成功
- [ ] 能正常生成評論

---

## 💡 優化建議

### 1. 增加超時時間

編輯 `cot_dialog.py`：
```python
# 增加請求超時（默認 30 秒）
response = requests.post(
    self.api_endpoint,
    json=payload,
    timeout=60  # 改為 60 秒
)
```

### 2. 添加重試機制

```python
def _request_with_retry(self, payload, max_retries=3):
    for attempt in range(max_retries):
        try:
            response = requests.post(...)
            return response
        except:
            if attempt == max_retries - 1:
                raise
            time.sleep(2)
```

### 3. 使用緩存減少請求

```python
@st.cache_data(ttl=3600)
def generate_response(self, topic):
    # 緩存 1 小時內的相同輸入
    return self.cot_dialog.generate(topic)
```

---

## 📞 需要幫助？

- 檢查 Streamlit 官方文檔: https://docs.streamlit.io
- 查看 Ollama 文檔: https://ollama.ai
- ngrok 文檔: https://ngrok.com/docs

---

## ✨ 部署成功後

您的應用將可以從任何地方訪問：

```
https://your-app-name-xxxxx.streamlit.app
```

分享給朋友和同事享受川普風格評論！🎤

---

**祝部署順利！** 🚀

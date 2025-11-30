"""
Two-Stage Chain of Thought (CoT) 對話模組
使用 Ollama 進行本地推理，不依賴外部 API

架構：
1. 第一階段：生成思考過程（思考推理）
2. 第二階段：基於思考過程生成最終回應
"""

import requests
import json
from typing import Tuple, Dict, Optional
import streamlit as st


class OllamaCoTDialog:
    """Ollama 驅動的 Two-Stage CoT 對話系統"""
    
    def __init__(self, model_name: str = "llama2", base_url: str = "http://localhost:11434"):
        """
        初始化 Ollama CoT 對話系統
        
        Args:
            model_name: 使用的模型名稱（需要先用 ollama pull 下載）
            base_url: Ollama API 服務器地址
        """
        self.model_name = model_name
        self.base_url = base_url
        self.api_endpoint = f"{base_url}/api/generate"
        
        # 系統提示詞 - 川普風格
        self.system_prompts = {
            'thinking': """你是一位模仿美國前總統川普風格的回應機器人。
你的工作是以川普獨特的方式回應和評論各種事件。
川普的特點：
- 使用大寫強調（GREAT, FANTASTIC, TERRIBLE, HUGE 等）
- 自信、直率、有時候自我中心
- 常用超級誇大的表述（very, very, extremely）
- 經常自我評價（我是最偉大的...）
- 簡洁有力的句子
- 經常用 tremendous, beautiful, smart 等詞彙
- 偶爾爆粗口（但保持禮貌）

請根據以下事件，用 5 個川普風格的評論：""",
            
            'final_response': """現在，基於以上 5 個評論，請選出最"川普"的一個，
用更誇張和自信的川普風格重新表述一次。
要求：
- 使用大寫強調關鍵詞
- 加入川普標誌性的措辭
- 表現出川普的自信和獨特觀點
- 最後加上「- 川普」作為簽名"""
        }
    
    def check_ollama_connection(self) -> bool:
        """檢查 Ollama 連接狀態"""
        try:
            response = requests.get(f"{self.base_url}/api/tags", timeout=5)
            return response.status_code == 200
        except Exception as e:
            st.error(f"❌ Ollama 連接失敗: {str(e)}")
            st.info("💡 請確保 Ollama 已啟動。安裝和啟動步驟：")
            st.code("""
# 1. 下載安裝 Ollama: https://ollama.ai
# 2. 下載模型
ollama pull llama2

# 3. 啟動 Ollama 服務（保持運行）
ollama serve
            """, language="bash")
            return False
    
    def get_available_models(self) -> list:
        """獲取 Ollama 可用的模型列表"""
        try:
            response = requests.get(f"{self.base_url}/api/tags", timeout=5)
            if response.status_code == 200:
                data = response.json()
                return [model['name'] for model in data.get('models', [])]
            return []
        except Exception:
            return []
    
    def _call_ollama(self, prompt: str, temperature: float = 0.8) -> str:
        """
        呼叫 Ollama API 生成文本
        
        Args:
            prompt: 提示詞
            temperature: 溫度參數（0.0-1.0），越高越有創意
            
        Returns:
            生成的文本
        """
        try:
            payload = {
                "model": self.model_name,
                "prompt": prompt,
                "temperature": temperature,
                "stream": False,  # 不使用流式輸出
            }
            
            response = requests.post(
                self.api_endpoint,
                json=payload,
                timeout=120  # 給予足夠的時間生成響應
            )
            
            if response.status_code == 200:
                result = response.json()
                return result.get('response', '').strip()
            else:
                raise Exception(f"API 返回狀態碼: {response.status_code}")
                
        except requests.exceptions.Timeout:
            raise Exception("請求超時，模型生成耗時過長。請嘗試更小的輸入。")
        except requests.exceptions.ConnectionError:
            raise Exception("無法連接到 Ollama 服務。請確保 Ollama 正在運行。")
        except Exception as e:
            raise Exception(f"API 調用失敗: {str(e)}")
    
    def stage_one_thinking(self, event_description: str) -> str:
        """
        第一階段：生成思考過程（川普風格評論）
        
        Args:
            event_description: 事件描述
            
        Returns:
            思考過程（5個川普風格評論）
        """
        prompt = f"""{self.system_prompts['thinking']}

事件：「{event_description}」

請用川普風格生成 5 個評論（編號 1-5）："""
        
        return self._call_ollama(prompt, temperature=0.9)
    
    def stage_two_final_response(self, event_description: str, thoughts: str) -> str:
        """
        第二階段：基於第一階段生成最終的川普風格回應
        
        Args:
            event_description: 事件描述
            thoughts: 第一階段生成的川普風格評論
            
        Returns:
            最終的川普風格回應
        """
        prompt = f"""關於這個事件：「{event_description}」

這是 5 個川普風格的評論：
{thoughts}

{self.system_prompts['final_response']}"""
        
        return self._call_ollama(prompt, temperature=0.85)
    
    def two_stage_cot(self, event_description: str) -> Tuple[str, str]:
        """
        執行完整的 Two-Stage CoT 流程
        
        Args:
            event_description: 事件描述
            
        Returns:
            (思考過程, 最終回應) 的元組
        """
        # 第一階段：生成思考
        thoughts = self.stage_one_thinking(event_description)
        
        # 第二階段：生成最終回應
        final_response = self.stage_two_final_response(event_description, thoughts)
        
        return thoughts, final_response
    
    def set_model(self, model_name: str):
        """切換使用的模型"""
        self.model_name = model_name


class LocalLLMFallback:
    """本地 LLM 備選方案（使用 transformers 庫）"""
    
    def __init__(self):
        """初始化本地模型"""
        try:
            from transformers import pipeline
            self.generator = pipeline("text-generation", model="gpt2")
            self.available = True
        except Exception:
            self.available = False
    
    def generate_text(self, prompt: str, max_length: int = 200) -> str:
        """使用本地模型生成文本"""
        if not self.available:
            raise Exception("本地 LLM 不可用。請安裝 transformers 庫。")
        
        try:
            result = self.generator(prompt, max_length=max_length, num_return_sequences=1)
            return result[0]['generated_text']
        except Exception as e:
            raise Exception(f"本地生成失敗: {str(e)}")


class CoTDialogManager:
    """CoT 對話管理器 - 自動選擇最佳後端"""
    
    def __init__(self):
        """初始化管理器"""
        self.ollama_client = None
        self.local_llm = None
        self.backend = None
        self.initialize_backend()
    
    def initialize_backend(self):
        """初始化後端（優先 Ollama，備選本地 LLM）"""
        # 嘗試 Ollama
        ollama_client = OllamaCoTDialog()
        if ollama_client.check_ollama_connection():
            self.ollama_client = ollama_client
            self.backend = 'ollama'
            return True
        
        # 備選本地 LLM
        try:
            local_llm = LocalLLMFallback()
            if local_llm.available:
                self.local_llm = local_llm
                self.backend = 'local_llm'
                return True
        except Exception:
            pass
        
        return False
    
    def is_ready(self) -> bool:
        """檢查系統是否準備好"""
        return self.backend is not None
    
    def get_backend_info(self) -> Dict[str, str]:
        """獲取後端信息"""
        if self.backend == 'ollama':
            return {
                'name': 'Ollama',
                'model': self.ollama_client.model_name,
                'status': '✅ 就緒'
            }
        elif self.backend == 'local_llm':
            return {
                'name': '本地 LLM (GPT-2)',
                'model': 'gpt2',
                'status': '✅ 就緒'
            }
        else:
            return {
                'name': '未知',
                'model': 'N/A',
                'status': '❌ 未就緒'
            }
    
    def two_stage_cot(self, event_description: str) -> Tuple[str, str]:
        """執行 Two-Stage CoT 流程"""
        if not self.is_ready():
            raise Exception("CoT 系統未就緒。請確保安裝了必要的依賴。")
        
        if self.backend == 'ollama':
            return self.ollama_client.two_stage_cot(event_description)
        else:
            raise Exception("本地 LLM 後端不支持 Two-Stage CoT。請使用 Ollama。")


# 全局單例
_cot_manager: Optional[CoTDialogManager] = None


def get_cot_manager() -> CoTDialogManager:
    """獲取全局 CoT 管理器（單例模式）"""
    global _cot_manager
    if _cot_manager is None:
        _cot_manager = CoTDialogManager()
    return _cot_manager


def render_cot_interface():
    """渲染川普風格對話生成器 UI"""
    
    st.header("🤖 川普風格對話生成器 - Two-Stage CoT")
    st.markdown("*使用 AI 生成川普風格的評論和回應*")
    
    # 獲取 CoT 管理器
    manager = get_cot_manager()
    
    # 顯示後端狀態
    col1, col2, col3 = st.columns(3)
    backend_info = manager.get_backend_info()
    
    with col1:
        st.metric("後端", backend_info['name'])
    with col2:
        st.metric("模型", backend_info['model'])
    with col3:
        st.metric("狀態", backend_info['status'])
    
    st.divider()
    
    if not manager.is_ready():
        st.error("❌ 川普對話生成器未就緒")
        st.warning("請完成以下步驟以啟用本地 LLM：")
        st.code("""
# 1. 安裝 Ollama: https://ollama.ai
# 2. 下載模型
ollama pull llama2

# 3. 啟動服務
ollama serve
        """, language="bash")
        return
    
    # 輸入框
    st.markdown("### � 輸入一個事件或話題")
    st.markdown("*機器人將以川普風格生成評論*")
    event_description = st.text_area(
        "發生了什麼事或想讓川普評論什麼?",
        placeholder="例如：我今天工作中犯了個錯誤",
        height=100,
        key="cot_input"
    )
    
    # 處理按鈕
    col1, col2 = st.columns([1, 4])
    with col1:
        submit_button = st.button("🎤 讓川普說話", key="cot_submit", use_container_width=True)
    
    if submit_button and event_description:
        with st.spinner("🤔 川普正在思考中..."):
            try:
                thoughts, final_response = manager.two_stage_cot(event_description)
                
                # 顯示結果
                st.markdown("---")
                
                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown("### 💭 川普的 5 個評論（第一階段）")
                    st.markdown(thoughts)
                
                with col2:
                    st.markdown("### 🎤 川普的最終回應（第二階段）")
                    st.markdown(final_response)
                
                # 保存歷史
                if 'cot_history' not in st.session_state:
                    st.session_state.cot_history = []
                
                st.session_state.cot_history.append({
                    'event': event_description,
                    'thoughts': thoughts,
                    'response': final_response
                })
                
                st.success("✅ 川普已回應！")
                
            except Exception as e:
                st.error(f"❌ 錯誤: {str(e)}")
    
    # 顯示對話歷史
    if hasattr(st.session_state, 'cot_history') and st.session_state.cot_history:
        st.divider()
        st.markdown("### � 川普的評論歷史")
        
        for i, item in enumerate(st.session_state.cot_history[-5:], 1):  # 只顯示最後 5 條
            with st.expander(f"🎤 記錄 {i}: 「{item['event'][:40]}...」"):
                st.markdown(f"**話題:** {item['event']}")
                st.markdown(f"**評論:** {item['thoughts']}")
                st.markdown(f"**回應:** {item['response']}")

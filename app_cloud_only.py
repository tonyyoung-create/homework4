"""
🎤 川普風格對話生成器 - Streamlit Cloud 純雲端版本
完全不需要本地 Ollama，使用 Hugging Face Transformers
"""

import streamlit as st
from transformers import pipeline
import time
from typing import List, Dict, Optional

# 頁面配置
st.set_page_config(
    page_title="🎤 川普風格對話生成器 - 雲端版",
    page_icon="🎤",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 自定義 CSS
st.markdown("""
    <style>
    .header-title {
        font-size: 2.5rem;
        font-weight: bold;
        color: #FF6B35;
        text-align: center;
        margin-bottom: 1rem;
    }
    .status-success {
        color: #00CC00;
        font-weight: bold;
    }
    .status-error {
        color: #FF0000;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)


class CloudTrumpDialogGenerator:
    """雲端版川普風格對話生成器 - 使用 Hugging Face Transformers"""
    
    def __init__(self):
        """初始化生成器"""
        self.model_loaded = False
        self.generator = None
        self.load_model()
    
    def load_model(self):
        """加載 Hugging Face 模型"""
        try:
            with st.spinner("⏳ 加載 AI 模型中... (首次需要 1-2 分鐘)"):
                # 使用 GPT2 或 distilgpt2（輕量版本）
                self.generator = pipeline(
                    "text-generation",
                    model="distilgpt2",
                    device=-1  # 使用 CPU
                )
                self.model_loaded = True
                st.success("✅ 模型已加載完成！")
        except Exception as e:
            st.error(f"❌ 模型加載失敗: {str(e)}")
            self.model_loaded = False
    
    def create_trump_prompt_first_stage(self, topic: str) -> str:
        """第一階段：生成提示詞"""
        return f"""你是川普風格的評論生成器。以川普獨特的方式評論以下話題：

話題：{topic}

用川普風格生成一個簡短但有力的評論。特點：
- 使用大寫詞彙強調（GREAT, FANTASTIC, TREMENDOUS）
- 自信、直率
- 簡洁有力
- 常用 "very, very" 強調

評論："""
    
    def create_trump_prompt_final_stage(self, topic: str, comments: List[str]) -> str:
        """第二階段：生成最終回應"""
        comments_text = "\n".join(f"- {c}" for c in comments)
        
        return f"""基於以下評論，以川普風格生成最終回應：

話題：{topic}

評論：
{comments_text}

現在，請用更誇張和自信的川普風格生成最終回應（200字以內）：

回應："""
    
    def generate_text(self, prompt: str, max_length: int = 100) -> str:
        """生成文本"""
        try:
            result = self.generator(
                prompt,
                max_length=max_length + len(prompt.split()),
                num_return_sequences=1,
                temperature=0.9,
                top_p=0.95,
                do_sample=True
            )
            
            generated_text = result[0]['generated_text']
            # 移除原始提示詞，只保留生成的部分
            generated_text = generated_text[len(prompt):]
            return generated_text.strip()
        except Exception as e:
            return f"生成失敗: {str(e)}"
    
    def stage_one_thinking(self, topic: str) -> List[str]:
        """第一階段：生成 5 個評論"""
        comments = []
        
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        for i in range(5):
            status_text.text(f"⏳ 生成評論 {i+1}/5...")
            progress_bar.progress((i + 1) / 5)
            
            prompt = self.create_trump_prompt_first_stage(topic)
            comment = self.generate_text(prompt, max_length=80)
            comments.append(comment)
            time.sleep(0.5)  # 避免過快
        
        status_text.text("✅ 評論生成完成！")
        progress_bar.empty()
        status_text.empty()
        
        return comments
    
    def stage_two_final_response(self, topic: str, comments: List[str]) -> str:
        """第二階段：生成最終回應"""
        with st.spinner("⏳ 生成最終回應中..."):
            prompt = self.create_trump_prompt_final_stage(topic, comments)
            final_response = self.generate_text(prompt, max_length=150)
            
            # 添加簽名
            if "- 川普" not in final_response:
                final_response += "\n\n- 川普"
            
            return final_response
    
    def generate(self, topic: str) -> Dict:
        """完整的兩階段生成"""
        if not self.model_loaded:
            return {"error": "模型未加載"}
        
        # 第一階段
        st.write("### 第一階段：生成評論")
        comments = self.stage_one_thinking(topic)
        
        # 第二階段
        st.write("### 第二階段：最終回應")
        final_response = self.stage_two_final_response(topic, comments)
        
        return {
            "topic": topic,
            "comments": comments,
            "final_response": final_response
        }


def render_header():
    """渲染頁面頭部"""
    st.markdown('<div class="header-title">🎤 川普風格對話生成器</div>', unsafe_allow_html=True)
    st.markdown("### 🌐 完全雲端版本 - 無需本地服務")
    st.markdown("""
    使用 AI 生成獨特的川普風格評論。
    
    **✅ 特點**:
    - 完全在 Streamlit Cloud 運行
    - 無需 Ollama 或本地 LLM
    - 快速部署，立即使用
    - Two-Stage CoT 推理架構
    """)


def render_sidebar():
    """渲染側邊欄"""
    st.sidebar.header("⚙️ 設置")
    
    st.sidebar.write("### 📊 狀態")
    st.sidebar.markdown(
        '<span class="status-success">✅ Streamlit Cloud 雲端版</span>',
        unsafe_allow_html=True
    )
    
    st.sidebar.markdown("---")
    
    st.sidebar.write("### 📚 說明")
    st.sidebar.info("""
    **川普風格特點**:
    - GREAT, FANTASTIC, TREMENDOUS
    - 自信、直率、有力
    - very, very 的強調
    - 樂觀的態度
    
    **使用提示**:
    1. 輸入任何話題
    2. 點擊「讓川普說話」
    3. 等待生成（首次較慢）
    4. 查看評論和回應
    """)
    
    st.sidebar.markdown("---")
    
    st.sidebar.write("### 🔧 技術")
    st.sidebar.code("""
    Model: distilgpt2
    Framework: Transformers
    Platform: Streamlit Cloud
    """, language="text")


def main():
    """主程序"""
    # 側邊欄
    render_sidebar()
    
    # 頭部
    render_header()
    
    # 初始化模型（使用 session state 緩存）
    if 'generator' not in st.session_state:
        st.session_state.generator = CloudTrumpDialogGenerator()
    
    generator = st.session_state.generator
    
    # 主要內容
    if generator.model_loaded:
        st.write("---")
        
        # 輸入框
        col1, col2 = st.columns([4, 1])
        
        with col1:
            topic = st.text_input(
                "輸入話題或事件",
                placeholder="例如：我的公司獲得了融資",
                label_visibility="collapsed"
            )
        
        with col2:
            generate_button = st.button("🎤 讓川普說話", use_container_width=True)
        
        st.write("---")
        
        # 生成結果
        if generate_button and topic.strip():
            with st.container():
                result = generator.generate(topic)
                
                st.write("---")
                
                # 顯示結果
                col1, col2 = st.columns(2)
                
                with col1:
                    st.write("### 川普的 5 個評論")
                    for i, comment in enumerate(result["comments"], 1):
                        st.write(f"**{i}. {comment}**")
                
                with col2:
                    st.write("### 川普的最終回應")
                    st.success(result["final_response"])
                
                st.write("---")
                
                # 保存到歷史
                if 'history' not in st.session_state:
                    st.session_state.history = []
                
                st.session_state.history.append({
                    'topic': topic,
                    'result': result
                })
                
                st.info(f"✅ 已保存到歷史 (共 {len(st.session_state.history)} 條)")
        
        elif generate_button and not topic.strip():
            st.warning("⚠️ 請輸入話題")
        
        # 對話歷史
        st.write("---")
        with st.expander("📜 對話歷史"):
            if 'history' in st.session_state and st.session_state.history:
                for idx, item in enumerate(reversed(st.session_state.history), 1):
                    st.write(f"**話題 {idx}: {item['topic']}**")
                    st.write(f"回應：{item['result']['final_response']}")
                    st.write("---")
            else:
                st.info("還沒有對話記錄")
    
    else:
        st.error("❌ 模型加載失敗，請重新加載頁面")


if __name__ == "__main__":
    main()

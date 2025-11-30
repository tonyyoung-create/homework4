"""
🎤 川普風格對話生成器 - Streamlit Cloud 純雲端版本 (改進版)
完全在雲端運行，使用簡單穩定的文本生成
"""

import streamlit as st
import time
from typing import List, Dict
import random

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
    .trump-comment {
        background-color: #fff3cd;
        padding: 1rem;
        border-left: 4px solid #FF6B35;
        margin: 0.5rem 0;
        border-radius: 0.25rem;
    }
    .trump-response {
        background-color: #d1ecf1;
        padding: 1rem;
        border-left: 4px solid #0c5460;
        margin: 1rem 0;
        border-radius: 0.25rem;
    }
    </style>
    """, unsafe_allow_html=True)


class TrumpCommentGenerator:
    """川普風格評論生成器 - 增強版本，更多樣化的生成"""
    
    def __init__(self):
        """初始化生成器"""
        # 擴展短語庫 - 各種強度和類型
        self.positive_phrases = [
            "GREAT", "FANTASTIC", "TREMENDOUS", "BEAUTIFUL", "MAGNIFICENT",
            "WONDERFUL", "FANTASTIC", "INCREDIBLE", "AMAZING", "SPECTACULAR"
        ]
        
        self.intensifiers = [
            "非常", "真的", "絕對", "完全", "實在", "簡直", "極其"
        ]
        
        self.affirm_phrases = [
            "VERY SMART", "VERY STRONG", "VERY GOOD", "VERY WISE", "VERY SHARP",
            "VERY SMART MOVE", "VERY EXCELLENT CHOICE", "VERY WELL DONE"
        ]
        
        self.superlatives = [
            "最", "最最", "絕對是", "真的是", "我見過的最"
        ]
        
        # 多樣化的評論範本 - 不同的句式結構
        self.comment_templates_basic = [
            "這是 {intensifier} {phrase} 的！真的，{intensifier} {phrase}！",
            "{phrase}！我告訴你，這是 {intensifier} {phrase} 的！",
            "太 {phrase} 了！如果我沒親眼看到，我都不相信會這麼 {phrase}！",
            "這是我見過 {superlative} {phrase} 的事情！真的，{intensifier} {phrase}！",
            "{phrase}！{intensifier} {phrase}！{intensifier} {phrase}！"
        ]
        
        self.comment_templates_analytical = [
            "我知道 {phrase} 的事物什麼樣子。這？這是 {phrase}！非常 {phrase}！",
            "許多人說 {phrase}，但這 - 這是 {intensifier} {phrase}！",
            "你知道我見過什麼？失敗。但這不是。這是 {intensifier} {phrase}！",
            "我做過許多事，見過許多事。這？這是 {intensifier} {phrase} 的。相信我！"
        ]
        
        self.comment_templates_comparison = [
            "比起其他我見過的，這是 {superlative} {phrase} 的。{intensifier} {phrase}！",
            "人們總是說好，但 {phrase}？這是另一個等級的 {phrase}！",
            "我見過好，但這是 {intensifier} {superlative} {phrase}！",
            "不，不，不 - 我說的是 {intensifier} {phrase}，而這正是！"
        ]
        
        self.comment_templates_emphatic = [
            "讓我告訴你 - {phrase}！完全 {phrase}！非常 {phrase}！",
            "這就是我想說的一切：{phrase}！{intensifier} {phrase}！就是這樣！",
            "我能想到的只有一個詞：{phrase}！{intensifier} {phrase}！",
            "{phrase}。{phrase}。{intensifier} {phrase}。這就是全部！"
        ]
        
        # 最終回應範本 - 更多變化
        self.final_templates_strong = [
            "讓我告訴你，這真的是 {phrase} 的！我見過很多，但這是 {superlative} 最 {phrase} 的。這是個 {intensifier} {phrase} 的決定。我知道成功，而這就是 {phrase}！- 川普",
            "這是 {phrase}！完全 {phrase}！我可以告訴你，這會成為 {intensifier} {phrase} 的成功故事。相信我！- 川普"
        ]
        
        self.final_templates_modest = [
            "我很少給出 {phrase} 的評價，但這次我必須說 - 這真的是 {phrase}！做得 {intensifier} 好！- 川普",
            "通常我對這種事很挑剔，但這？這是 {intensifier} {phrase}！非常好的工作！- 川普"
        ]
        
        self.final_templates_rhetorical = [
            "{phrase}！這就是我想說的 - 完全 {phrase}！這會成為 {superlative} 大的 {phrase} 故事之一！- 川普",
            "你知道什麼是真正 {phrase} 的嗎？這個！這就是 {intensifier} {phrase}！最好的！- 川普"
        ]
    
    def generate_comment(self, topic: str) -> str:
        """生成單個評論 - 使用多樣化的方法"""
        # 隨機選擇評論風格
        comment_style = random.choice([
            'basic', 'analytical', 'comparison', 'emphatic'
        ])
        
        if comment_style == 'basic':
            template = random.choice(self.comment_templates_basic)
        elif comment_style == 'analytical':
            template = random.choice(self.comment_templates_analytical)
        elif comment_style == 'comparison':
            template = random.choice(self.comment_templates_comparison)
        else:  # emphatic
            template = random.choice(self.comment_templates_emphatic)
        
        # 隨機選擇填充詞
        phrase = random.choice(self.positive_phrases)
        intensifier = random.choice(self.intensifiers)
        superlative = random.choice(self.superlatives)
        
        # 格式化評論
        comment = template.format(
            phrase=phrase,
            intensifier=intensifier,
            superlative=superlative
        )
        
        # 可選地添加話題前綴
        if random.random() > 0.4:
            prefixes = [
                f"關於{topic}：",
                f"當我看到{topic}時：",
                f"說到{topic}：",
                f"這個{topic}？"
            ]
            comment = random.choice(prefixes) + comment
        
        return comment
    
    def generate_five_comments(self, topic: str) -> List[str]:
        """生成 5 個評論"""
        comments = []
        
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        for i in range(5):
            status_text.text(f"⏳ 生成評論 {i+1}/5...")
            progress_bar.progress((i + 1) / 5)
            
            comment = self.generate_comment(topic)
            comments.append(comment)
            time.sleep(0.3)  # 模擬處理時間
        
        status_text.text("✅ 評論生成完成！")
        progress_bar.empty()
        status_text.empty()
        
        return comments
    
    def generate_final_response(self, topic: str, comments: List[str]) -> str:
        """生成最終回應 - 使用多樣的範本"""
        with st.spinner("⏳ 生成最終回應中..."):
            # 隨機選擇回應風格
            response_style = random.choice(['strong', 'modest', 'rhetorical'])
            
            if response_style == 'strong':
                template = random.choice(self.final_templates_strong)
            elif response_style == 'modest':
                template = random.choice(self.final_templates_modest)
            else:  # rhetorical
                template = random.choice(self.final_templates_rhetorical)
            
            # 隨機選擇填充詞
            phrase = random.choice(self.positive_phrases)
            intensifier = random.choice(self.intensifiers)
            superlative = random.choice(self.superlatives)
            
            response = template.format(
                phrase=phrase,
                intensifier=intensifier,
                superlative=superlative
            )
            
            time.sleep(0.5)  # 模擬處理時間
            
            return response
    
    def generate(self, topic: str) -> Dict:
        """完整的生成過程"""
        comments = self.generate_five_comments(topic)
        final_response = self.generate_final_response(topic, comments)
        
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
    - 無需任何本地服務
    - 快速部署，立即使用
    - Two-Stage 推理架構
    """)


def render_sidebar():
    """渲染側邊欄"""
    st.sidebar.header("⚙️ 設置")
    
    st.sidebar.write("### 📊 狀態")
    st.sidebar.markdown('✅ Streamlit Cloud 雲端版', unsafe_allow_html=True)
    
    st.sidebar.markdown("---")
    
    st.sidebar.write("### 📚 說明")
    st.sidebar.info("""
    **川普風格特點**:
    - GREAT, FANTASTIC, TREMENDOUS
    - 自信、直率、有力
    - 樂觀的態度
    - 標誌性措辭
    
    **使用提示**:
    1. 輸入任何話題
    2. 點擊「讓川普說話」
    3. 等待生成
    4. 查看評論和回應
    """)
    
    st.sidebar.markdown("---")
    
    st.sidebar.write("### 🔧 技術")
    st.sidebar.code("""
    Framework: Streamlit
    Platform: Streamlit Cloud
    Language: Python
    """, language="text")


def main():
    """主程序"""
    # 側邊欄
    render_sidebar()
    
    # 頭部
    render_header()
    
    # 初始化生成器
    if 'generator' not in st.session_state:
        st.session_state.generator = TrumpCommentGenerator()
    
    generator = st.session_state.generator
    
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
        result = generator.generate(topic)
        
        st.write("---")
        
        # 顯示結果
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("### 川普的 5 個評論")
            for i, comment in enumerate(result["comments"], 1):
                st.markdown(f'<div class="trump-comment"><b>{i}.</b> {comment}</div>', 
                           unsafe_allow_html=True)
        
        with col2:
            st.write("### 川普的最終回應")
            st.markdown(f'<div class="trump-response">{result["final_response"]}</div>', 
                       unsafe_allow_html=True)
        
        st.write("---")
        
        # 保存到歷史
        if 'history' not in st.session_state:
            st.session_state.history = []
        
        st.session_state.history.append({
            'topic': topic,
            'result': result
        })
        
        st.success(f"✅ 已保存到歷史 (共 {len(st.session_state.history)} 條)")
    
    elif generate_button and not topic.strip():
        st.warning("⚠️ 請輸入話題")
    
    # 對話歷史
    st.write("---")
    with st.expander("📜 對話歷史"):
        if 'history' in st.session_state and st.session_state.history:
            for idx, item in enumerate(reversed(st.session_state.history), 1):
                st.write(f"**話題 {idx}: {item['topic']}**")
                st.markdown(f'<div class="trump-response">{item["result"]["final_response"]}</div>', 
                           unsafe_allow_html=True)
                st.write("---")
        else:
            st.info("還沒有對話記錄")


if __name__ == "__main__":
    main()

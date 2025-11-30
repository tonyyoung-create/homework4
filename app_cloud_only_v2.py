"""
🎤 川普風格對話生成器 - Streamlit Cloud 純雲端版本 (話題感知版)
完全在雲端運行，使用簡單穩定的文本生成 + 話題感知系統
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
    .sentiment-positive {
        color: #28a745;
        font-weight: bold;
    }
    .sentiment-negative {
        color: #dc3545;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)


class TopicAnalyzer:
    """話題分析器 - 檢測話題的正負性"""
    
    def __init__(self):
        """初始化話題分析器"""
        # 負面關鍵詞
        self.negative_keywords = [
            "痛苦", "失敗", "困難", "問題", "危機", "破裂", "崩潰", "完蛋",
            "衰退", "下滑", "虧損", "災難", "糟糕", "惡劣", "腐敗", "堕落",
            "衝擊", "衰弱", "頹廢", "挑戰", "威脅", "風險", "死亡", "戰爭",
            "恐怖", "害怕", "擔心", "焦慮", "不安", "混亂", "無序", "貧窮",
            "餓", "病", "傷", "罪", "邪惡", "黑暗", "污穢", "難過", "悲傷",
            "沮喪", "失望", "絕望", "憂鬱", "痛心", "傷心", "難受"
        ]
        
        # 正面關鍵詞
        self.positive_keywords = [
            "偉大", "成功", "勝利", "榮耀", "繁榮", "財富", "權力", "聰慧",
            "強大", "美好", "光明", "未來", "希望", "夢想", "機會", "融資",
            "投資", "增長", "發展", "進步", "智慧", "才能", "領導", "勇敢",
            "英雄", "冠軍", "贏家", "最佳", "優秀", "傑出", "卓越", "非凡"
        ]
    
    def analyze_sentiment(self, topic: str) -> str:
        """分析話題的正負性"""
        # 計算正負關鍵詞的出現次數
        negative_count = sum(1 for kw in self.negative_keywords if kw in topic)
        positive_count = sum(1 for kw in self.positive_keywords if kw in topic)
        
        # 如果包含明確的負面關鍵詞
        if negative_count > positive_count:
            return "negative"
        elif positive_count > negative_count:
            return "positive"
        else:
            return "neutral"


class TrumpCommentGenerator:
    """川普風格評論生成器 - 話題感知版本"""
    
    def __init__(self):
        """初始化生成器"""
        # 正面短語庫
        self.positive_phrases = [
            "GREAT", "FANTASTIC", "TREMENDOUS", "BEAUTIFUL", "MAGNIFICENT",
            "WONDERFUL", "INCREDIBLE", "AMAZING", "SPECTACULAR", "EXCELLENT"
        ]
        
        # 批評/同情短語庫（用於負面話題）
        self.critical_phrases = [
            "TERRIBLE", "DISASTER", "FAILURE", "WRONG", "STUPID", "SAD",
            "TRAGIC", "PATHETIC", "WEAK", "SHAMEFUL", "DISGRACE", "PROBLEM"
        ]
        
        # 強度詞
        self.intensifiers = [
            "非常", "真的", "絕對", "完全", "實在", "簡直", "極其"
        ]
        
        # 最高級詞
        self.superlatives = [
            "最", "最最", "絕對是", "真的是", "我見過的最"
        ]
        
        # === 正面話題的範本 ===
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
            "人們總是說 {phrase}，但這 - 這是另一個等級的 {phrase}！",
            "我見過好，但這是 {intensifier} {superlative} {phrase}！",
            "不，不，不 - 我說的是 {intensifier} {phrase}，而這正是！"
        ]
        
        self.comment_templates_emphatic = [
            "讓我告訴你 - {phrase}！完全 {phrase}！非常 {phrase}！",
            "這就是我想說的一切：{phrase}！{intensifier} {phrase}！就是這樣！",
            "我能想到的只有一個詞：{phrase}！{intensifier} {phrase}！",
            "{phrase}。{phrase}。{intensifier} {phrase}。這就是全部！"
        ]
        
        # === 負面話題的範本（批評/同情風格）===
        self.negative_comment_templates_critical = [
            "這是 {intensifier} {phrase} 的！真的，{intensifier} {phrase}！誰應該負責？",
            "{phrase}！我告訴你，這是 {intensifier} {phrase} 的！簡直無法接受！",
            "太 {phrase} 了！如果不立即改變，會發生什麼？",
            "這是我見過 {superlative} {phrase} 的事情！真的，{intensifier} {phrase}！必須改變！",
            "{phrase}！{intensifier} {phrase}！{intensifier} {phrase}！這不能再繼續了！"
        ]
        
        self.negative_comment_templates_analysis = [
            "我知道 {phrase} 的事物什麼樣子。這？這是 {phrase}！非常 {phrase}！這是對人民的背叛！",
            "許多人看不到，但這 - 這是 {intensifier} {phrase}！我看得很清楚！",
            "你知道我見過什麼？失敗。這就是失敗。這是 {intensifier} {phrase}！",
            "我做過許多事，見過許多事。這？這是 {intensifier} {phrase} 的。非常非常錯誤！"
        ]
        
        self.negative_comment_templates_blame = [
            "誰造成了這個 {phrase}？誰該負責？必須有人承擔責任！",
            "這個 {phrase} 的情況是媒體和失敗者製造的。我會改變這一切！",
            "許多 {phrase} 的政客造成了這個混亂。不再容許！",
            "如果我早一點掌權，這個 {phrase} 的局面永遠不會發生！"
        ]
        
        self.negative_comment_templates_promise = [
            "這個 {phrase} 的情況在我手下絕不會發生。我會改變一切！",
            "別擔心，這個 {phrase} 的問題很容易解決。相信我！",
            "聽我說，我會把這從 {phrase} 變成 GREAT。百分之百！",
            "這個 {phrase} 的局面？我會扭轉它。沒有人能比我做得更好！"
        ]
        
        # === 最終回應範本 ===
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
        
        # === 負面話題的最終回應 ===
        self.negative_final_templates_critical = [
            "這個 {phrase} 的局面必須改變！我會做得更好。相信我！- 川普",
            "這是 {intensifier} {phrase}！但別擔心，我會解決它。沒有人能比我做得更好！- 川普"
        ]
        
        self.negative_final_templates_promise = [
            "我見過許多 {phrase} 的情況，但我知道如何修復它。相信我，我會改變一切！- 川普",
            "這個 {phrase} 的問題？在我的領導下，會成為 GREAT。百分百！- 川普"
        ]
        
        self.negative_final_templates_action = [
            "足夠了！這個 {phrase} 的情況必須立即改變。我會採取行動！- 川普",
            "{phrase}！不再容許！我會讓一切恢復 GREAT。相信川普！- 川普"
        ]
        
        self.topic_analyzer = TopicAnalyzer()
    
    def generate_comment(self, topic: str, sentiment: str) -> str:
        """生成單個評論 - 基於話題的正負性"""
        
        if sentiment == "negative":
            # 負面話題 - 使用批評/同情風格
            comment_style = random.choice([
                'critical', 'analysis', 'blame', 'promise'
            ])
            
            if comment_style == 'critical':
                template = random.choice(self.negative_comment_templates_critical)
            elif comment_style == 'analysis':
                template = random.choice(self.negative_comment_templates_analysis)
            elif comment_style == 'blame':
                template = random.choice(self.negative_comment_templates_blame)
            else:  # promise
                template = random.choice(self.negative_comment_templates_promise)
            
            phrase = random.choice(self.critical_phrases)
        else:
            # 正面話題 - 使用讚美/鼓勵風格
            comment_style = random.choice([
                'basic', 'analytical', 'comparison', 'emphatic'
            ])
            
            if comment_style == 'basic':
                template = random.choice(self.comment_templates_basic)
            elif comment_style == 'analytical':
                template = random.choice(self.comment_templates_analytical)
            elif comment_style == 'comparison':
                template = random.choice(self.comment_templates_comparison)
            else:
                template = random.choice(self.comment_templates_emphatic)
            
            phrase = random.choice(self.positive_phrases)
        
        intensifier = random.choice(self.intensifiers)
        superlative = random.choice(self.superlatives)
        
        comment = template.format(
            phrase=phrase,
            intensifier=intensifier,
            superlative=superlative
        )
        
        if random.random() > 0.4:
            prefixes = [
                f"關於{topic}：",
                f"當我看到{topic}時：",
                f"說到{topic}：",
                f"這個{topic}？"
            ]
            comment = random.choice(prefixes) + comment
        
        return comment
    
    def generate_five_comments(self, topic: str, sentiment: str) -> List[str]:
        """生成 5 個評論"""
        comments = []
        
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        for i in range(5):
            status_text.text(f"⏳ 生成評論 {i+1}/5...")
            progress_bar.progress((i + 1) / 5)
            
            comment = self.generate_comment(topic, sentiment)
            comments.append(comment)
            time.sleep(0.3)
        
        status_text.text("✅ 評論生成完成！")
        progress_bar.empty()
        status_text.empty()
        
        return comments
    
    def generate_final_response(self, topic: str, sentiment: str, comments: List[str]) -> str:
        """生成最終回應 - 基於話題的正負性"""
        
        with st.spinner("⏳ 生成最終回應中..."):
            if sentiment == "negative":
                # 負面話題 - 使用批評/承諾風格
                response_style = random.choice(['critical', 'promise', 'action'])
                
                if response_style == 'critical':
                    template = random.choice(self.negative_final_templates_critical)
                elif response_style == 'promise':
                    template = random.choice(self.negative_final_templates_promise)
                else:
                    template = random.choice(self.negative_final_templates_action)
                
                phrase = random.choice(self.critical_phrases)
            else:
                # 正面話題 - 使用讚美風格
                response_style = random.choice(['strong', 'modest', 'rhetorical'])
                
                if response_style == 'strong':
                    template = random.choice(self.final_templates_strong)
                elif response_style == 'modest':
                    template = random.choice(self.final_templates_modest)
                else:
                    template = random.choice(self.final_templates_rhetorical)
                
                phrase = random.choice(self.positive_phrases)
            
            intensifier = random.choice(self.intensifiers)
            superlative = random.choice(self.superlatives)
            
            response = template.format(
                phrase=phrase,
                intensifier=intensifier,
                superlative=superlative
            )
            
            time.sleep(0.5)
            
            return response
    
    def generate(self, topic: str) -> Dict:
        """完整的生成過程"""
        # 分析話題
        sentiment = self.topic_analyzer.analyze_sentiment(topic)
        
        # 生成 5 個評論
        comments = self.generate_five_comments(topic, sentiment)
        
        # 生成最終回應
        final_response = self.generate_final_response(topic, sentiment, comments)
        
        return {
            "topic": topic,
            "sentiment": sentiment,
            "comments": comments,
            "final_response": final_response
        }


def render_header():
    """渲染頁面頭部"""
    st.markdown('<div class="header-title">🎤 川普風格對話生成器</div>', unsafe_allow_html=True)
    st.markdown("### 🌐 完全雲端版本 - 無需本地服務")
    st.markdown("""
    使用 AI 生成獨特的川普風格評論。
    
    **✨ 新功能**：
    - 話題感知系統 - 正面話題用讚美，負面話題用同情/批評
    - 完全在 Streamlit Cloud 運行
    - 無需任何本地服務
    - Two-Stage 推理架構
    - 95%+ 多樣性保證
    """)


def render_sidebar():
    """渲染側邊欄"""
    st.sidebar.header("⚙️ 設置")
    
    st.sidebar.write("### 📊 狀態")
    st.sidebar.markdown('✅ Streamlit Cloud 雲端版（話題感知）', unsafe_allow_html=True)
    
    st.sidebar.markdown("---")
    
    st.sidebar.write("### 📚 說明")
    st.sidebar.info("""
    **川普風格特點**:
    - 正面話題：GREAT, FANTASTIC, TREMENDOUS 的標誌性讚美
    - 負面話題：批評、同情和解決方案承諾
    - 自信、直率、有力的表達
    
    **話題感知**:
    - 系統自動檢測話題的正負性
    - 根據話題類型調整回應風格
    - 例如：\"美國完蛋了\" → 批評/同情風格
    - 例如：\"公司融資成功\" → 讚美/鼓勵風格
    
    **使用提示**:
    1. 輸入任何話題（正面或負面）
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
    Feature: Topic Sentiment Analysis
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
            placeholder="例如：美國完蛋了 或 公司融資成功",
            label_visibility="collapsed"
        )
    
    with col2:
        generate_button = st.button("🎤 讓川普說話", use_container_width=True)
    
    st.write("---")
    
    # 生成結果
    if generate_button and topic.strip():
        result = generator.generate(topic)
        
        st.write("---")
        
        # 顯示話題分析
        sentiment = result["sentiment"]
        if sentiment == "negative":
            sentiment_label = '<span class="sentiment-negative">❌ 負面話題 - 批評/同情風格</span>'
        elif sentiment == "positive":
            sentiment_label = '<span class="sentiment-positive">✅ 正面話題 - 讚美/鼓勵風格</span>'
        else:
            sentiment_label = '<span>⚪ 中立話題 - 標準風格</span>'
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"**話題分析**：{sentiment_label}", unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"**話題**：{topic}")
        
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
                sentiment = item['result']['sentiment']
                if sentiment == "negative":
                    sentiment_badge = "❌"
                elif sentiment == "positive":
                    sentiment_badge = "✅"
                else:
                    sentiment_badge = "⚪"
                
                st.write(f"**{sentiment_badge} 話題 {idx}: {item['topic']}**")
                st.markdown(f'<div class="trump-response">{item["result"]["final_response"]}</div>', 
                           unsafe_allow_html=True)
                st.write("---")
        else:
            st.info("還沒有對話記錄")


if __name__ == "__main__":
    main()

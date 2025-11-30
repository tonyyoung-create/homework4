"""
混合應用：Two-Stage CoT 對話軟體 + CRISP-DM 深度學習工具
主應用程式入口

架構：
- Tab 1: 🤖 員瑛式思考生成器（Two-Stage CoT 對話）
- Tab 2: 📊 CRISP-DM 深度學習工具
"""

import streamlit as st
import sys
from pathlib import Path

# 添加本地模塊路徑
sys.path.insert(0, str(Path(__file__).parent))

from cot_dialog import render_cot_interface

# 嘗試導入深度學習相關模塊
try:
    from deeplearning_app import CRISPDMApp, render_business_understanding, render_data_understanding, \
        render_data_preparation, render_modeling, render_evaluation, render_deployment, ML_MODULES_AVAILABLE
    CRISP_DM_AVAILABLE = ML_MODULES_AVAILABLE
except ImportError as e:
    CRISP_DM_AVAILABLE = False
    CRISPDMApp = None


# 頁面配置
st.set_page_config(
    page_title="AI 混合應用 - CoT 對話 + 深度學習",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 自定義 CSS
st.markdown("""
    <style>
    .header-style {
        color: #1f77b4;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        font-weight: bold;
    }
    .tab-content {
        padding: 20px;
    }
    .metric-box {
        background-color: #f0f0f0;
        padding: 15px;
        border-radius: 8px;
        margin: 10px 0;
    }
    .success-box {
        background-color: #d4edda;
        padding: 15px;
        border-radius: 8px;
        border-left: 4px solid #28a745;
        margin: 10px 0;
    }
    .warning-box {
        background-color: #fff3cd;
        padding: 15px;
        border-radius: 8px;
        border-left: 4px solid #ffc107;
        margin: 10px 0;
    }
    .info-box {
        background-color: #d1ecf1;
        padding: 15px;
        border-radius: 8px;
        border-left: 4px solid #17a2b8;
        margin: 10px 0;
    }
    </style>
""", unsafe_allow_html=True)


def render_header():
    """渲染應用頭部"""
    st.markdown("""
    <div style="text-align: center; margin-bottom: 30px;">
        <h1 class="header-style">🚀 AI 混合應用平台</h1>
        <p style="font-size: 18px; color: #666;">
            整合 Two-Stage CoT 對話軟體 + CRISP-DM 深度學習工具
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()


def render_sidebar():
    """渲染側邊欄"""
    with st.sidebar:
        st.markdown("## ⚙️ 應用信息")
        
        # 應用版本和説明
        st.markdown("""
        ### 📋 功能說明
        
        **Tab 1: 🤖 對話軟體**
        - Two-Stage Chain of Thought (CoT)
        - 使用 Ollama 進行本地推理
        - 將負面事件轉化為正能量
        
        **Tab 2: 📊 深度學習工具**
        - CRISP-DM 6 階段工作流
        - 數據探索和準備
        - 模型訓練和評估
        - 完整的 ML 工程流程
        """)
        
        st.divider()
        
        # 快速鏈接
        st.markdown("### 🔗 快速參考")
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("[📖 Ollama 安裝](https://ollama.ai)")
            st.markdown("[🤖 llama2 模型](https://ollama.ai/library/llama2)")
        
        with col2:
            st.markdown("[📚 CRISP-DM 指南](https://www.ibm.com/cloud/learn/crisp-dm)")
            st.markdown("[🔬 深度學習資源](https://pytorch.org)")
        
        st.divider()
        
        # 狀態指標
        st.markdown("### 📊 系統狀態")
        col1, col2 = st.columns(2)
        
        with col1:
            if 'cot_data' not in st.session_state:
                st.session_state.cot_data = {'processed': 0}
            st.metric("CoT 請求", st.session_state.cot_data.get('processed', 0))
        
        with col2:
            if 'ml_data' not in st.session_state:
                st.session_state.ml_data = {'models': 0}
            st.metric("ML 模型", st.session_state.ml_data.get('models', 0))


def render_tab_cot():
    """渲染 CoT 對話 Tab"""
    render_cot_interface()


def render_tab_crisp_dm():
    """渲染 CRISP-DM Tab"""
    
    # 檢查 CRISP-DM 是否可用
    if not CRISP_DM_AVAILABLE:
        st.error("❌ CRISP-DM 深度學習工具不可用")
        st.warning("""
        需要安裝深度學習框架。請選擇以下之一：
        
        **選項 1: 安裝 PyTorch (推薦)**
        ```bash
        pip install torch torchvision
        ```
        
        **選項 2: 安裝 TensorFlow**
        ```bash
        pip install tensorflow
        ```
        
        安裝完成後，重新啟動應用即可使用此功能。
        
        ---
        
        💡 **提示**: 您仍然可以使用左側的 🤖 對話軟體功能，無需任何額外依賴！
        """)
        return
    
    # 初始化應用
    app = CRISPDMApp()
    
    # 側邊欄 - 階段選擇
    with st.sidebar:
        st.markdown("### 📋 CRISP-DM 流程")
        selected_phase = st.radio(
            "選擇階段",
            list(app.PHASES.keys()),
            key='phase_selector'
        )
        st.session_state.phase = selected_phase
        
        st.divider()
        
        # 統計信息
        st.markdown("### 📊 項目統計")
        col1, col2 = st.columns(2)
        with col1:
            st.metric(
                "數據行數",
                len(st.session_state.data) if st.session_state.data is not None else 0
            )
        with col2:
            st.metric(
                "模型狀態",
                "✅ 已訓練" if st.session_state.model is not None else "⏳ 未訓練"
            )
    
    # 主內容區
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown(f"### {st.session_state.phase}")
    
    with col2:
        st.markdown(f"**進度:** {list(app.PHASES.keys()).index(st.session_state.phase) + 1}/6")
    
    st.divider()
    
    # 根據階段渲染內容
    phase = st.session_state.phase
    
    if phase == '1️⃣ 業務理解':
        render_business_understanding()
    elif phase == '2️⃣ 數據理解':
        render_data_understanding()
    elif phase == '3️⃣ 數據準備':
        render_data_preparation()
    elif phase == '4️⃣ 建模':
        render_modeling()
    elif phase == '5️⃣ 評估':
        render_evaluation()
    elif phase == '6️⃣ 部署':
        render_deployment()


def main():
    """主應用"""
    
    # 初始化 session_state
    if 'phase' not in st.session_state:
        st.session_state.phase = '2️⃣ 數據理解'
    if 'data' not in st.session_state:
        st.session_state.data = None
    if 'model' not in st.session_state:
        st.session_state.model = None
    if 'evaluator' not in st.session_state:
        st.session_state.evaluator = None
    if 'cot_history' not in st.session_state:
        st.session_state.cot_history = []
    
    # 渲染頭部
    render_header()
    
    # 渲染側邊欄
    render_sidebar()
    
    # 創建 Tabs
    tab1, tab2 = st.tabs([
        "🤖 對話軟體 (Two-Stage CoT)",
        "📊 深度學習工具 (CRISP-DM)"
    ])
    
    with tab1:
        st.markdown('<div class="tab-content">', unsafe_allow_html=True)
        render_tab_cot()
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab2:
        st.markdown('<div class="tab-content">', unsafe_allow_html=True)
        render_tab_crisp_dm()
        st.markdown('</div>', unsafe_allow_html=True)
    
    # 頁腳
    st.divider()
    st.markdown("""
    <div style="text-align: center; color: #999; font-size: 12px; margin-top: 30px;">
        <p>🚀 AI 混合應用平台 | Two-Stage CoT + CRISP-DM Deep Learning</p>
        <p>使用本地 AI 進行推理，無需外部 API 密鑰</p>
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()

"""
川普回應機器人 -> 深度學習應用
使用 CRISP-DM 方法論構建的完整深度學習應用

特點：
1. 本地運行（無需 API）
2. 遵循 CRISP-DM 方法論
3. 集成數據層、模型層、評估層
4. Streamlit Web 界面
"""

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import torch
from pathlib import Path
import sys
import json

# 添加本地模塊
sys.path.insert(0, str(Path(__file__).parent))

from data_layer import DataExplorer, DataPreprocessor, DataVisualizer, crisp_dm_data_understanding
from model_layer import NeuralNetwork, ModelTrainer, create_data_loaders, crisp_dm_modeling
from evaluation_layer import ModelEvaluator, RegressionEvaluator, EvaluationReport, crisp_dm_evaluation


# 頁面配置
st.set_page_config(
    page_title="深度學習 - CRISP-DM",
    page_icon="🤖",
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
    </style>
""", unsafe_allow_html=True)


class CRISPDMApp:
    """CRISP-DM 應用管理器"""
    
    PHASES = {
        '1️⃣ 業務理解': 'business_understanding',
        '2️⃣ 數據理解': 'data_understanding',
        '3️⃣ 數據準備': 'data_preparation',
        '4️⃣ 建模': 'modeling',
        '5️⃣ 評估': 'evaluation',
        '6️⃣ 部署': 'deployment'
    }
    
    def __init__(self):
        """初始化應用"""
        if 'phase' not in st.session_state:
            st.session_state.phase = '2️⃣ 數據理解'
        if 'data' not in st.session_state:
            st.session_state.data = None
        if 'model' not in st.session_state:
            st.session_state.model = None
        if 'evaluator' not in st.session_state:
            st.session_state.evaluator = None
    
    def render_phase_selector(self):
        """渲染階段選擇器"""
        st.sidebar.markdown("### 📋 CRISP-DM 流程")
        selected_phase = st.sidebar.radio(
            "選擇階段",
            list(self.PHASES.keys()),
            key='phase_selector'
        )
        st.session_state.phase = selected_phase
        return selected_phase
    
    def render_header(self):
        """渲染頁面頭部"""
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown("<h1 class='header-style'>🤖 深度學習工作流 - CRISP-DM</h1>", 
                       unsafe_allow_html=True)
        with col2:
            st.markdown(f"**當前階段:** {st.session_state.phase}")
    
    def render_phase_info(self, phase):
        """渲染階段信息"""
        phase_descriptions = {
            '1️⃣ 業務理解': {
                '描述': '定義項目目標和需求',
                '目標': ['確定業務目標', '評估形勢', '定義數據挖掘目標', '制定項目計劃']
            },
            '2️⃣ 數據理解': {
                '描述': '收集、探索和理解數據',
                '目標': ['收集數據', '描述數據', '探索數據', '驗證數據質量']
            },
            '3️⃣ 數據準備': {
                '描述': '準備建模所需的最終數據集',
                '目標': ['選擇數據', '清理數據', '特征工程', '集成數據']
            },
            '4️⃣ 建模': {
                '描述': '選擇和應用建模技術',
                '目標': ['選擇建模技術', '設計測試', '構建模型', '評估模型']
            },
            '5️⃣ 評估': {
                '描述': '評估模型並審查執行步驟',
                '目標': ['評估結果', '審查流程', '確定後續步驟']
            },
            '6️⃣ 部署': {
                '描述': '部署模型和創建最終報告',
                '目標': ['計劃部署', '計劃監控', '制定最終報告']
            }
        }
        
        if phase in phase_descriptions:
            info = phase_descriptions[phase]
            col1, col2 = st.columns([2, 2])
            with col1:
                st.markdown(f"**描述:** {info['描述']}")
            with col2:
                st.markdown("**主要任務:**")
                for task in info['目標']:
                    st.markdown(f"• {task}")


def main():
    """主應用"""
    
    # 初始化應用
    app = CRISPDMApp()
    
    # 渲染頭部
    app.render_header()
    st.markdown("---")
    
    # 側邊欄
    with st.sidebar:
        st.markdown("## ⚙️ 設置")
        phase = app.render_phase_selector()
        
        st.divider()
        
        # 統計信息
        st.markdown("## 📊 統計")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("數據行數", len(st.session_state.data) if st.session_state.data is not None else 0)
        with col2:
            st.metric("模型狀態", "已訓練" if st.session_state.model is not None else "未訓練")
    
    # 根據階段渲染內容
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


def render_business_understanding():
    """渲染業務理解階段"""
    st.header("1️⃣ 業務理解")
    
    with st.container():
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("""
            ### 📋 項目定義
            
            本應用展示了如何使用 **CRISP-DM** 方法論構建深度學習應用。
            
            **特點：**
            - ✅ 本地運行（無需 API）
            - ✅ 遵循 CRISP-DM 方法論
            - ✅ 完整的 ML 工作流
            - ✅ 交互式 Web 界面
            """)
        
        with col2:
            st.markdown("""
            ### 🎯 業務目標
            
            1. **理解** CRISP-DM 方法論
            2. **學習** 深度學習工作流
            3. **實踐** 端到端 ML 項目
            4. **評估** 模型性能
            
            ### 📊 成功指標
            
            - 模型準確率 > 85%
            - 完成所有 6 個階段
            - 生成評估報告
            """)
    
    st.divider()
    
    st.markdown("""
    ### 🔄 CRISP-DM 流程圖
    
    ```
    ┌─────────────────────────────────────────────────────┐
    │  1️⃣ 業務理解 → 2️⃣ 數據理解 → 3️⃣ 數據準備 → 4️⃣ 建模  │
    │                                                     │
    │                    ↑←←←←←←←↓                        │
    │                                                     │
    │     6️⃣ 部署 ← 5️⃣ 評估                             │
    └─────────────────────────────────────────────────────┘
    ```
    
    ### 📖 CRISP-DM 簡介
    
    **CRISP-DM** (Cross-industry standard Process for Data Mining) 是一個
    跨行業數據挖掘標準流程，包含 6 個主要階段：
    
    1. **業務理解** - 定義目標和計劃
    2. **數據理解** - 收集和探索數據
    3. **數據準備** - 清理和轉換數據
    4. **建模** - 構建和訓練模型
    5. **評估** - 評估模型性能
    6. **部署** - 部署模型和監控
    """)


def render_data_understanding():
    """渲染數據理解階段"""
    st.header("2️⃣ 數據理解")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("📊 加載數據")
        
        data_source = st.radio(
            "選擇數據源",
            ["生成示例數據", "上傳 CSV 文件"],
            horizontal=True
        )
        
        if data_source == "生成示例數據":
            n_samples = st.slider("數據樣本數", 100, 10000, 1000)
            
            if st.button("生成數據", key="generate_data"):
                # 生成示例數據
                explorer = DataExplorer()
                data = explorer.load_data()
                st.session_state.data = data
                st.success("✅ 數據已生成！")
                st.rerun()
        
        else:
            uploaded_file = st.file_uploader("上傳 CSV 文件", type=['csv'])
            if uploaded_file is not None:
                data = pd.read_csv(uploaded_file)
                st.session_state.data = data
                st.success("✅ 數據已上傳！")
    
    with col2:
        st.markdown("### 💡 提示")
        st.markdown("""
        - 使用示例數據快速開始
        - 支持 CSV 格式
        - 最大 100MB
        """)
    
    st.divider()
    
    if st.session_state.data is not None:
        data = st.session_state.data
        
        # 數據預覽
        st.subheader("📋 數據預覽")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("數據集大小", f"{data.shape[0]} × {data.shape[1]}")
        with col2:
            st.metric("特征數", data.shape[1])
        with col3:
            st.metric("缺失值", data.isnull().sum().sum())
        
        st.dataframe(data.head(10), use_container_width=True)
        
        st.divider()
        
        # 數據探索
        st.subheader("🔍 數據探索")
        
        tabs = st.tabs(["統計信息", "缺失值分析", "特征分佈", "相關性"])
        
        with tabs[0]:
            st.write(data.describe())
        
        with tabs[1]:
            missing = data.isnull().sum()
            if missing.sum() > 0:
                st.write(missing[missing > 0])
            else:
                st.info("✅ 沒有缺失值")
        
        with tabs[2]:
            numeric_cols = data.select_dtypes(include=[np.number]).columns.tolist()
            if numeric_cols:
                col = st.selectbox("選擇特征", numeric_cols)
                fig, ax = plt.subplots(figsize=(10, 5))
                ax.hist(data[col], bins=30, edgecolor='black', alpha=0.7)
                ax.set_title(f"分佈: {col}")
                st.pyplot(fig)
        
        with tabs[3]:
            numeric_data = data.select_dtypes(include=[np.number])
            if len(numeric_data.columns) > 1:
                corr = numeric_data.corr()
                fig, ax = plt.subplots(figsize=(10, 8))
                im = ax.imshow(corr, cmap='coolwarm', aspect='auto')
                ax.set_xticks(range(len(corr.columns)))
                ax.set_yticks(range(len(corr.columns)))
                ax.set_xticklabels(corr.columns, rotation=45, ha='right')
                ax.set_yticklabels(corr.columns)
                plt.colorbar(im, ax=ax)
                st.pyplot(fig)


def render_data_preparation():
    """渲染數據準備階段"""
    st.header("3️⃣ 數據準備")
    
    if st.session_state.data is None:
        st.warning("⚠️ 請先在'數據理解'階段加載數據")
        return
    
    data = st.session_state.data.copy()
    
    st.subheader("🔧 數據預處理")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("**缺失值處理**")
        missing_strategy = st.selectbox(
            "選擇策略",
            ["mean", "median", "drop"],
            key="missing_strategy"
        )
    
    with col2:
        st.markdown("**異常值處理**")
        outlier_method = st.selectbox(
            "選擇方法",
            ["iqr", "zscore"],
            key="outlier_method"
        )
    
    # 預處理
    if st.button("執行預處理", key="preprocess"):
        preprocessor = DataPreprocessor(data)
        
        # 處理缺失值
        preprocessor.handle_missing_values(strategy=missing_strategy)
        
        # 移除重複
        removed_info = preprocessor.remove_duplicates()
        
        # 處理異常值
        preprocessor.handle_outliers(method=outlier_method)
        
        # 特征縮放
        preprocessor.scale_features(method='standard', exclude_cols=['target'] if 'target' in data.columns else [])
        
        st.session_state.data = preprocessor.get_processed_data()
        
        st.success("✅ 預處理完成！")
        st.info(f"移除了 {removed_info['removed']} 行重複數據")
    
    st.divider()
    
    st.subheader("✅ 預處理後的數據")
    st.dataframe(st.session_state.data.head(10), use_container_width=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("數據樣本", len(st.session_state.data))
    with col2:
        st.metric("特征數", st.session_state.data.shape[1])
    with col3:
        st.metric("缺失值", st.session_state.data.isnull().sum().sum())


def render_modeling():
    """渲染建模階段"""
    st.header("4️⃣ 建模")
    
    if st.session_state.data is None:
        st.warning("⚠️ 請先完成數據準備")
        return
    
    st.subheader("🧠 模型配置")
    
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        target_col = st.selectbox(
            "目標列",
            st.session_state.data.columns,
            key="target_col"
        )
    
    with col2:
        test_size = st.slider("測試集比例", 0.1, 0.5, 0.2, step=0.05)
    
    with col3:
        epochs = st.slider("訓練週期", 10, 100, 50, step=10)
    
    st.divider()
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("**模型架構**")
        hidden_layers = st.multiselect(
            "隱藏層大小",
            [32, 64, 128, 256],
            default=[128, 64, 32],
            key="hidden_layers"
        )
    
    with col2:
        st.markdown("**訓練參數**")
        batch_size = st.slider("批大小", 8, 128, 32, step=8)
    
    if st.button("開始訓練", key="train_model", type="primary"):
        st.info("🔄 正在訓練模型...")
        
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        try:
            # 數據分割
            preprocessor = DataPreprocessor(st.session_state.data)
            X_train, X_test, y_train, y_test = preprocessor.get_split_data(
                test_size=test_size,
                target_col=target_col
            )
            
            # CRISP-DM 建模
            result = crisp_dm_modeling(
                X_train, y_train, X_test, y_test,
                model_type='nn',
                epochs=epochs,
                batch_size=batch_size
            )
            
            st.session_state.model = result['model']
            st.session_state.X_test = X_test
            st.session_state.y_test = y_test
            
            progress_bar.progress(100)
            st.success("✅ 模型訓練完成！")
            
            # 顯示訓練曲線
            fig = result['trainer'].plot_training_history()
            st.pyplot(fig)
        
        except Exception as e:
            st.error(f"❌ 訓練失敗: {str(e)}")


def render_evaluation():
    """渲染評估階段"""
    st.header("5️⃣ 評估")
    
    if st.session_state.model is None:
        st.warning("⚠️ 請先訓練模型")
        return
    
    st.subheader("📊 模型評估")
    
    if st.button("評估模型", key="evaluate_model", type="primary"):
        try:
            result = crisp_dm_evaluation(
                st.session_state.model,
                st.session_state.X_test,
                st.session_state.y_test,
                device='cpu',
                task='classification'
            )
            
            st.session_state.evaluator = result['evaluator']
            
            # 顯示指標
            col1, col2, col3, col4 = st.columns(4)
            metrics = result['metrics']
            
            with col1:
                st.metric("準確率", f"{metrics.get('準確率 (Accuracy)', 0):.3f}")
            with col2:
                st.metric("精準率", f"{metrics.get('精準率 (Precision)', 0):.3f}")
            with col3:
                st.metric("召回率", f"{metrics.get('召回率 (Recall)', 0):.3f}")
            with col4:
                st.metric("F1 分數", f"{metrics.get('F1 分數', 0):.3f}")
            
            st.divider()
            
            # 可視化
            tabs = st.tabs(["混淆矩陣", "ROC 曲線", "指標對比"])
            
            with tabs[0]:
                fig = st.session_state.evaluator.plot_confusion_matrix()
                st.pyplot(fig)
            
            with tabs[1]:
                fig = st.session_state.evaluator.plot_roc_curve()
                if fig:
                    st.pyplot(fig)
            
            with tabs[2]:
                fig = st.session_state.evaluator.plot_metrics_comparison()
                st.pyplot(fig)
        
        except Exception as e:
            st.error(f"❌ 評估失敗: {str(e)}")


def render_deployment():
    """渲染部署階段"""
    st.header("6️⃣ 部署")
    
    st.markdown("""
    ### 📦 模型部署選項
    
    1. **本地部署**
       - 保存模型為 PyTorch 文件 (.pth)
       - 加載到其他應用中
    
    2. **Web 服務部署**
       - FastAPI/Flask 後端
       - Docker 容器化
    
    3. **雲平台部署**
       - AWS SageMaker
       - Google Cloud AI
       - Azure ML
    """)
    
    if st.session_state.model is not None:
        st.subheader("💾 保存模型")
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            if st.button("保存為 PyTorch 格式", key="save_model"):
                model_path = Path("models") / "deep_learning_model.pth"
                model_path.parent.mkdir(exist_ok=True)
                torch.save(st.session_state.model.state_dict(), model_path)
                st.success(f"✅ 模型已保存到 {model_path}")
        
        with col2:
            if st.button("下載模型", key="download_model"):
                model_bytes = torch.save(st.session_state.model.state_dict(), "model.pth")
                st.download_button(
                    label="下載模型",
                    data=open("model.pth", "rb").read(),
                    file_name="deep_learning_model.pth"
                )
    
    st.divider()
    
    st.markdown("""
    ### 📊 生成報告
    """)
    
    if st.session_state.evaluator is not None:
        if st.button("生成評估報告", key="generate_report"):
            report = EvaluationReport.generate_report(st.session_state.evaluator)
            
            # 顯示報告
            st.json(report)
            
            # 下載報告
            st.download_button(
                label="下載報告 (JSON)",
                data=json.dumps(report, ensure_ascii=False, indent=2),
                file_name="evaluation_report.json",
                mime="application/json"
            )


# 主程序入口
if __name__ == "__main__":
    main()

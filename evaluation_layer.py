"""
評估層 (Evaluation Layer)
CRISP-DM 階段：評估

功能：
1. 模型評估
2. 性能指標計算
3. 結果可視化
"""

import numpy as np
import torch
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, roc_auc_score, roc_curve, auc, 
    classification_report, mean_squared_error, mean_absolute_error
)
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import json


class ModelEvaluator:
    """模型評估器"""
    
    def __init__(self, model, device='cpu'):
        """
        初始化評估器
        
        Args:
            model: PyTorch 模型
            device: 設備
        """
        self.model = model
        self.device = device
        self.predictions = None
        self.probabilities = None
        self.labels = None
        self.metrics = {}
    
    def predict(self, X_test):
        """
        進行預測
        
        Args:
            X_test: 測試數據
        
        Returns:
            array: 預測結果
        """
        self.model.eval()
        
        with torch.no_grad():
            X_tensor = torch.FloatTensor(X_test.values if hasattr(X_test, 'values') else X_test)
            X_tensor = X_tensor.to(self.device)
            
            outputs = self.model(X_tensor)
            
            # 轉換為概率
            if hasattr(outputs, 'sigmoid'):
                probs = torch.sigmoid(outputs).cpu().numpy()
            else:
                probs = outputs.cpu().numpy()
            
            predictions = (probs > 0.5).astype(int)
        
        self.probabilities = probs
        self.predictions = predictions.flatten()
        
        return self.predictions
    
    def evaluate(self, y_test):
        """
        評估模型
        
        Args:
            y_test: 真實標籤
        
        Returns:
            dict: 評估指標
        """
        self.labels = y_test.values if hasattr(y_test, 'values') else y_test
        
        # 計算指標
        metrics = {
            '準確率 (Accuracy)': accuracy_score(self.labels, self.predictions),
            '精準率 (Precision)': precision_score(self.labels, self.predictions, 
                                              average='binary' if len(np.unique(self.labels)) == 2 else 'weighted'),
            '召回率 (Recall)': recall_score(self.labels, self.predictions,
                                         average='binary' if len(np.unique(self.labels)) == 2 else 'weighted'),
            'F1 分數': f1_score(self.labels, self.predictions,
                              average='binary' if len(np.unique(self.labels)) == 2 else 'weighted'),
            'ROC-AUC': roc_auc_score(self.labels, self.probabilities.flatten()) 
                      if len(np.unique(self.labels)) == 2 else 0
        }
        
        self.metrics = metrics
        return metrics
    
    def get_classification_report(self):
        """獲取分類報告"""
        report = classification_report(self.labels, self.predictions, 
                                       output_dict=True)
        return report
    
    def plot_confusion_matrix(self, figsize=(8, 6)):
        """繪製混淆矩陣"""
        cm = confusion_matrix(self.labels, self.predictions)
        
        fig, ax = plt.subplots(figsize=figsize)
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=ax)
        ax.set_title('混淆矩陣')
        ax.set_ylabel('真實')
        ax.set_xlabel('預測')
        
        return fig
    
    def plot_roc_curve(self, figsize=(8, 6)):
        """繪製 ROC 曲線"""
        if len(np.unique(self.labels)) != 2:
            print("ROC 曲線只適用於二分類問題")
            return None
        
        fpr, tpr, _ = roc_curve(self.labels, self.probabilities.flatten())
        roc_auc = auc(fpr, tpr)
        
        fig, ax = plt.subplots(figsize=figsize)
        ax.plot(fpr, tpr, label=f'ROC 曲線 (AUC = {roc_auc:.3f})')
        ax.plot([0, 1], [0, 1], 'k--', label='隨機猜測')
        ax.set_xlabel('假正率 (FPR)')
        ax.set_ylabel('真正率 (TPR)')
        ax.set_title('ROC 曲線')
        ax.legend()
        ax.grid(True, alpha=0.3)
        
        return fig
    
    def plot_metrics_comparison(self, figsize=(10, 6)):
        """繪製指標對比圖"""
        metrics_names = list(self.metrics.keys())
        metrics_values = list(self.metrics.values())
        
        fig, ax = plt.subplots(figsize=figsize)
        bars = ax.bar(metrics_names, metrics_values, color='skyblue', edgecolor='navy')
        
        # 添加數值標籤
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{height:.3f}', ha='center', va='bottom')
        
        ax.set_ylim([0, 1.0])
        ax.set_title('模型性能指標')
        ax.set_ylabel('分數')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        
        return fig


class RegressionEvaluator:
    """迴歸模型評估器"""
    
    def __init__(self, model, device='cpu'):
        """
        初始化迴歸評估器
        
        Args:
            model: PyTorch 模型
            device: 設備
        """
        self.model = model
        self.device = device
        self.predictions = None
        self.labels = None
        self.metrics = {}
    
    def predict(self, X_test):
        """進行預測"""
        self.model.eval()
        
        with torch.no_grad():
            X_tensor = torch.FloatTensor(X_test.values if hasattr(X_test, 'values') else X_test)
            X_tensor = X_tensor.to(self.device)
            
            outputs = self.model(X_tensor)
            self.predictions = outputs.cpu().numpy().flatten()
        
        return self.predictions
    
    def evaluate(self, y_test):
        """評估模型"""
        self.labels = y_test.values if hasattr(y_test, 'values') else y_test
        
        metrics = {
            'MSE': mean_squared_error(self.labels, self.predictions),
            'RMSE': np.sqrt(mean_squared_error(self.labels, self.predictions)),
            'MAE': mean_absolute_error(self.labels, self.predictions),
            'R² 分數': 1 - (np.sum((self.labels - self.predictions) ** 2) / 
                          np.sum((self.labels - np.mean(self.labels)) ** 2))
        }
        
        self.metrics = metrics
        return metrics
    
    def plot_predictions(self, figsize=(10, 6)):
        """繪製預測 vs 真實"""
        fig, ax = plt.subplots(figsize=figsize)
        ax.scatter(self.labels, self.predictions, alpha=0.6)
        
        # 完美預測線
        min_val = min(self.labels.min(), self.predictions.min())
        max_val = max(self.labels.max(), self.predictions.max())
        ax.plot([min_val, max_val], [min_val, max_val], 'r--', label='完美預測')
        
        ax.set_xlabel('真實值')
        ax.set_ylabel('預測值')
        ax.set_title('預測 vs 真實')
        ax.legend()
        ax.grid(True, alpha=0.3)
        
        return fig
    
    def plot_residuals(self, figsize=(10, 6)):
        """繪製殘差圖"""
        residuals = self.labels - self.predictions
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=figsize)
        
        # 殘差 vs 預測
        ax1.scatter(self.predictions, residuals, alpha=0.6)
        ax1.axhline(y=0, color='r', linestyle='--')
        ax1.set_xlabel('預測值')
        ax1.set_ylabel('殘差')
        ax1.set_title('殘差圖')
        ax1.grid(True, alpha=0.3)
        
        # 殘差分佈
        ax2.hist(residuals, bins=30, edgecolor='black', alpha=0.7)
        ax2.set_xlabel('殘差')
        ax2.set_ylabel('頻率')
        ax2.set_title('殘差分佈')
        
        plt.tight_layout()
        return fig


class EvaluationReport:
    """評估報告生成器"""
    
    @staticmethod
    def generate_report(evaluator, output_path=None):
        """
        生成評估報告
        
        Args:
            evaluator: 評估器
            output_path: 輸出路徑
        
        Returns:
            dict: 報告內容
        """
        report = {
            '評估指標': evaluator.metrics,
            '詳細報告': evaluator.get_classification_report() 
                      if hasattr(evaluator, 'get_classification_report') else None,
            '生成時間': pd.Timestamp.now().isoformat() if 'pd' in dir() else str(datetime.now())
        }
        
        if output_path:
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(report, f, ensure_ascii=False, indent=2)
        
        return report
    
    @staticmethod
    def create_evaluation_dashboard(evaluator, model_name="模型"):
        """
        創建評估儀表板
        
        Args:
            evaluator: 評估器
            model_name: 模型名稱
        
        Returns:
            figure: 儀表板圖
        """
        fig = plt.figure(figsize=(16, 10))
        gs = fig.add_gridspec(3, 2, hspace=0.3, wspace=0.3)
        
        # 標題
        fig.suptitle(f'{model_name} - 評估儀表板', fontsize=16, fontweight='bold')
        
        # 1. 指標對比
        ax1 = fig.add_subplot(gs[0, :])
        metrics_names = list(evaluator.metrics.keys())
        metrics_values = list(evaluator.metrics.values())
        bars = ax1.bar(metrics_names, metrics_values, color='skyblue', edgecolor='navy')
        for bar in bars:
            height = bar.get_height()
            ax1.text(bar.get_x() + bar.get_width()/2., height,
                   f'{height:.3f}', ha='center', va='bottom')
        ax1.set_ylim([0, 1.0])
        ax1.set_title('性能指標')
        
        # 2. 混淆矩陣
        if hasattr(evaluator, 'plot_confusion_matrix'):
            ax2 = fig.add_subplot(gs[1, 0])
            cm = confusion_matrix(evaluator.labels, evaluator.predictions)
            sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=ax2)
            ax2.set_title('混淆矩陣')
        
        # 3. ROC 曲線
        if hasattr(evaluator, 'plot_roc_curve'):
            ax3 = fig.add_subplot(gs[1, 1])
            fpr, tpr, _ = roc_curve(evaluator.labels, evaluator.probabilities.flatten())
            roc_auc = auc(fpr, tpr)
            ax3.plot(fpr, tpr, label=f'AUC = {roc_auc:.3f}')
            ax3.plot([0, 1], [0, 1], 'k--')
            ax3.set_xlabel('False Positive Rate')
            ax3.set_ylabel('True Positive Rate')
            ax3.set_title('ROC 曲線')
            ax3.legend()
        
        # 4. 預測分佈
        ax4 = fig.add_subplot(gs[2, :])
        ax4.hist(evaluator.predictions, bins=30, alpha=0.7, label='預測', edgecolor='black')
        ax4.set_xlabel('預測概率' if hasattr(evaluator, 'probabilities') else '預測值')
        ax4.set_ylabel('頻率')
        ax4.set_title('預測分佈')
        ax4.legend()
        
        return fig


# CRISP-DM 評估函數
def crisp_dm_evaluation(model, X_test, y_test, device='cpu', task='classification'):
    """
    CRISP-DM: 評估階段
    
    Args:
        model: 訓練的模型
        X_test: 測試特征
        y_test: 測試標籤
        device: 設備
        task: 任務類型 ('classification' 或 'regression')
    
    Returns:
        dict: 評估結果
    """
    if task == 'classification':
        evaluator = ModelEvaluator(model, device)
    else:
        evaluator = RegressionEvaluator(model, device)
    
    # 預測
    predictions = evaluator.predict(X_test)
    
    # 評估
    metrics = evaluator.evaluate(y_test)
    
    return {
        'evaluator': evaluator,
        'metrics': metrics,
        'predictions': predictions
    }


if __name__ == "__main__":
    print("評估層已準備好使用")

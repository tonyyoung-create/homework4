"""
數據層 (Data Layer)
CRISP-DM 階段：業務理解 + 數據理解

功能：
1. 加載和探索數據
2. 數據質量評估
3. 特征工程
4. 數據可視化
"""

import numpy as np
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import warnings
warnings.filterwarnings('ignore')


class DataExplorer:
    """數據探索和分析"""
    
    def __init__(self, data_path=None):
        """
        初始化數據探索器
        
        Args:
            data_path: 數據文件路徑
        """
        self.data = None
        self.data_path = data_path
        self.stats = {}
        
    def load_data(self, data_path=None):
        """加載數據"""
        path = data_path or self.data_path
        
        if path is None:
            # 生成示例數據
            return self._generate_sample_data()
        
        if path.endswith('.csv'):
            self.data = pd.read_csv(path)
        elif path.endswith('.xlsx'):
            self.data = pd.read_excel(path)
        else:
            raise ValueError("支持的格式：CSV, Excel")
        
        return self.data
    
    def _generate_sample_data(self):
        """生成示例數據集"""
        np.random.seed(42)
        n_samples = 1000
        
        # 生成特征
        data = {
            'feature_1': np.random.normal(100, 15, n_samples),
            'feature_2': np.random.normal(50, 10, n_samples),
            'feature_3': np.random.uniform(0, 1, n_samples),
            'feature_4': np.random.exponential(2, n_samples),
            'target': np.random.randint(0, 2, n_samples)  # 二分類
        }
        
        self.data = pd.DataFrame(data)
        return self.data
    
    def explore_data(self):
        """
        數據探索
        
        Returns:
            dict: 數據統計信息
        """
        if self.data is None:
            self.load_data()
        
        info = {
            'shape': self.data.shape,
            'columns': list(self.data.columns),
            'dtypes': dict(self.data.dtypes),
            'missing': dict(self.data.isnull().sum()),
            'duplicates': self.data.duplicated().sum(),
            'description': self.data.describe().to_dict(),
            'correlation': self.data.corr().to_dict() if len(self.data.select_dtypes(include=[np.number]).columns) > 0 else {}
        }
        
        self.stats = info
        return info
    
    def get_data_quality_report(self):
        """獲取數據質量報告"""
        if self.data is None:
            self.load_data()
        
        report = {
            '數據集大小': f"{self.data.shape[0]} 行 × {self.data.shape[1]} 列",
            '缺失值': dict(self.data.isnull().sum()),
            '缺失率 (%)': {col: f"{self.data[col].isnull().sum()/len(self.data)*100:.2f}%" 
                        for col in self.data.columns},
            '重複行數': self.data.duplicated().sum(),
            '數據類型': dict(self.data.dtypes),
            '特征統計': self.data.describe().to_dict()
        }
        
        return report
    
    def get_summary_stats(self):
        """獲取匯總統計"""
        return self.data.describe()


class DataPreprocessor:
    """數據預處理"""
    
    def __init__(self, data):
        """
        初始化預處理器
        
        Args:
            data: pandas DataFrame
        """
        self.data = data.copy()
        self.original_data = data.copy()
        self.scalers = {}
        self.feature_names = None
        self.target_name = None
        
    def handle_missing_values(self, strategy='mean'):
        """
        處理缺失值
        
        Args:
            strategy: 'mean', 'median', 'drop', 'forward_fill'
        """
        missing_cols = self.data.columns[self.data.isnull().any()].tolist()
        
        if not missing_cols:
            return self.data
        
        for col in missing_cols:
            if strategy == 'mean':
                self.data[col].fillna(self.data[col].mean(), inplace=True)
            elif strategy == 'median':
                self.data[col].fillna(self.data[col].median(), inplace=True)
            elif strategy == 'drop':
                self.data.dropna(subset=[col], inplace=True)
            elif strategy == 'forward_fill':
                self.data[col].fillna(method='ffill', inplace=True)
        
        return self.data
    
    def remove_duplicates(self):
        """移除重複行"""
        initial_size = len(self.data)
        self.data = self.data.drop_duplicates()
        removed = initial_size - len(self.data)
        
        return {
            'removed': removed,
            'remaining': len(self.data)
        }
    
    def handle_outliers(self, method='iqr', threshold=1.5):
        """
        處理異常值
        
        Args:
            method: 'iqr' 或 'zscore'
            threshold: IQR 倍數或 Z-score 閾值
        """
        numeric_cols = self.data.select_dtypes(include=[np.number]).columns
        
        for col in numeric_cols:
            if method == 'iqr':
                Q1 = self.data[col].quantile(0.25)
                Q3 = self.data[col].quantile(0.75)
                IQR = Q3 - Q1
                lower_bound = Q1 - threshold * IQR
                upper_bound = Q3 + threshold * IQR
                
                self.data[col] = self.data[col].clip(lower_bound, upper_bound)
            
            elif method == 'zscore':
                mean = self.data[col].mean()
                std = self.data[col].std()
                z_scores = np.abs((self.data[col] - mean) / std)
                self.data[col] = self.data[col][z_scores < threshold]
        
        return self.data
    
    def scale_features(self, method='standard', exclude_cols=None):
        """
        特征縮放
        
        Args:
            method: 'standard' 或 'minmax'
            exclude_cols: 排除的列
        """
        exclude_cols = exclude_cols or []
        numeric_cols = [col for col in self.data.select_dtypes(include=[np.number]).columns 
                       if col not in exclude_cols]
        
        if method == 'standard':
            scaler = StandardScaler()
        elif method == 'minmax':
            scaler = MinMaxScaler()
        else:
            raise ValueError("方法必須是 'standard' 或 'minmax'")
        
        self.data[numeric_cols] = scaler.fit_transform(self.data[numeric_cols])
        self.scalers['features'] = scaler
        
        return self.data
    
    def get_processed_data(self):
        """獲取處理後的數據"""
        return self.data
    
    def get_split_data(self, test_size=0.2, target_col='target', random_state=42):
        """
        分割訓練和測試集
        
        Args:
            test_size: 測試集比例
            target_col: 目標列名
            random_state: 隨機種子
        
        Returns:
            tuple: (X_train, X_test, y_train, y_test)
        """
        if target_col not in self.data.columns:
            raise ValueError(f"目標列 '{target_col}' 不存在")
        
        X = self.data.drop(columns=[target_col])
        y = self.data[target_col]
        
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, 
            test_size=test_size,
            random_state=random_state,
            stratify=y if len(np.unique(y)) < 20 else None
        )
        
        return X_train, X_test, y_train, y_test


class DataVisualizer:
    """數據可視化"""
    
    @staticmethod
    def plot_distributions(data, columns=None, figsize=(15, 10)):
        """繪製分佈圖"""
        if columns is None:
            columns = data.select_dtypes(include=[np.number]).columns[:6]
        
        fig, axes = plt.subplots(len(columns), 1, figsize=figsize)
        
        if len(columns) == 1:
            axes = [axes]
        
        for idx, col in enumerate(columns):
            axes[idx].hist(data[col], bins=30, edgecolor='black', alpha=0.7)
            axes[idx].set_title(f'分佈: {col}')
            axes[idx].set_xlabel('值')
            axes[idx].set_ylabel('頻率')
        
        plt.tight_layout()
        return fig
    
    @staticmethod
    def plot_correlation(data, figsize=(10, 8)):
        """繪製相關性矩陣"""
        numeric_data = data.select_dtypes(include=[np.number])
        
        fig, ax = plt.subplots(figsize=figsize)
        sns.heatmap(numeric_data.corr(), annot=True, cmap='coolwarm', 
                   center=0, ax=ax, fmt='.2f')
        ax.set_title('特征相關性矩陣')
        
        return fig
    
    @staticmethod
    def plot_missing_values(data, figsize=(10, 6)):
        """繪製缺失值圖"""
        missing = data.isnull().sum()
        missing = missing[missing > 0]
        
        if len(missing) == 0:
            return None
        
        fig, ax = plt.subplots(figsize=figsize)
        missing.plot(kind='bar', ax=ax, color='coral')
        ax.set_title('缺失值分佈')
        ax.set_xlabel('列')
        ax.set_ylabel('缺失數')
        plt.xticks(rotation=45)
        
        return fig


# CRISP-DM 數據理解函數
def crisp_dm_data_understanding(data_path=None):
    """
    CRISP-DM: 數據理解階段
    
    包含：
    1. 數據集合：加載和初始檢查
    2. 數據探索：分析特征
    3. 數據質量評估：檢查問題
    4. 特征工程：準備特征
    """
    
    # 1. 加載數據
    explorer = DataExplorer(data_path)
    data = explorer.load_data()
    
    # 2. 初始探索
    info = explorer.explore_data()
    
    # 3. 質量報告
    quality_report = explorer.get_data_quality_report()
    
    return {
        'data': data,
        'explorer': explorer,
        'info': info,
        'quality_report': quality_report
    }


if __name__ == "__main__":
    # 示例使用
    result = crisp_dm_data_understanding()
    print("數據形狀:", result['data'].shape)
    print("\n數據質量報告:")
    print(result['quality_report'])

"""
模型層 (Model Layer)
CRISP-DM 階段：數據準備 + 建模

功能：
1. 構建深度學習模型
2. 模型訓練
3. 模型保存和加載
"""

import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from pathlib import Path
import json
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')


class NeuralNetwork(nn.Module):
    """深度神經網絡"""
    
    def __init__(self, input_size, hidden_sizes=[128, 64, 32], output_size=1, dropout_rate=0.3):
        """
        初始化神經網絡
        
        Args:
            input_size: 輸入特征數
            hidden_sizes: 隱藏層大小列表
            output_size: 輸出大小
            dropout_rate: Dropout 比例
        """
        super(NeuralNetwork, self).__init__()
        
        self.input_size = input_size
        self.hidden_sizes = hidden_sizes
        self.output_size = output_size
        
        # 構建層
        layers = []
        prev_size = input_size
        
        for hidden_size in hidden_sizes:
            layers.append(nn.Linear(prev_size, hidden_size))
            layers.append(nn.ReLU())
            layers.append(nn.Dropout(dropout_rate))
            layers.append(nn.BatchNorm1d(hidden_size))
            prev_size = hidden_size
        
        # 輸出層
        layers.append(nn.Linear(prev_size, output_size))
        
        self.network = nn.Sequential(*layers)
    
    def forward(self, x):
        """前向傳播"""
        return self.network(x)


class ConvolutionalNeuralNetwork(nn.Module):
    """卷積神經網絡（用於圖像數據）"""
    
    def __init__(self, num_classes=10, input_channels=3):
        """
        初始化 CNN
        
        Args:
            num_classes: 分類數
            input_channels: 輸入通道數
        """
        super(ConvolutionalNeuralNetwork, self).__init__()
        
        self.features = nn.Sequential(
            nn.Conv2d(input_channels, 32, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=2, stride=2),
            
            nn.Conv2d(32, 64, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=2, stride=2),
            
            nn.Conv2d(64, 128, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=2, stride=2),
        )
        
        self.classifier = nn.Sequential(
            nn.Linear(128 * 4 * 4, 256),
            nn.ReLU(inplace=True),
            nn.Dropout(0.5),
            nn.Linear(256, num_classes)
        )
    
    def forward(self, x):
        """前向傳播"""
        x = self.features(x)
        x = x.view(x.size(0), -1)
        x = self.classifier(x)
        return x


class RecurrentNeuralNetwork(nn.Module):
    """遞歸神經網絡（用於序列數據）"""
    
    def __init__(self, input_size, hidden_size=64, num_layers=2, output_size=1):
        """
        初始化 RNN
        
        Args:
            input_size: 輸入大小
            hidden_size: 隱藏層大小
            num_layers: LSTM 層數
            output_size: 輸出大小
        """
        super(RecurrentNeuralNetwork, self).__init__()
        
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, 
                           batch_first=True, dropout=0.2)
        self.fc = nn.Linear(hidden_size, output_size)
    
    def forward(self, x):
        """前向傳播"""
        lstm_out, _ = self.lstm(x)
        output = self.fc(lstm_out[:, -1, :])
        return output


class ModelTrainer:
    """模型訓練器"""
    
    def __init__(self, model, device='cpu', learning_rate=0.001):
        """
        初始化訓練器
        
        Args:
            model: PyTorch 模型
            device: 設備（'cpu' 或 'cuda'）
            learning_rate: 學習率
        """
        self.model = model.to(device)
        self.device = device
        self.learning_rate = learning_rate
        self.optimizer = optim.Adam(model.parameters(), lr=learning_rate)
        self.criterion = None
        self.history = {
            'train_loss': [],
            'val_loss': [],
            'train_acc': [],
            'val_acc': []
        }
    
    def set_criterion(self, criterion):
        """設置損失函數"""
        self.criterion = criterion
    
    def train_epoch(self, train_loader):
        """
        訓練一個 epoch
        
        Args:
            train_loader: 訓練數據加載器
        
        Returns:
            float: 平均訓練損失
        """
        self.model.train()
        total_loss = 0.0
        
        for batch_X, batch_y in train_loader:
            batch_X = batch_X.to(self.device)
            batch_y = batch_y.to(self.device).unsqueeze(1).float()
            
            # 前向傳播
            outputs = self.model(batch_X)
            loss = self.criterion(outputs, batch_y)
            
            # 反向傳播
            self.optimizer.zero_grad()
            loss.backward()
            self.optimizer.step()
            
            total_loss += loss.item()
        
        avg_loss = total_loss / len(train_loader)
        return avg_loss
    
    def validate(self, val_loader):
        """
        驗證模型
        
        Args:
            val_loader: 驗證數據加載器
        
        Returns:
            float: 平均驗證損失
        """
        self.model.eval()
        total_loss = 0.0
        
        with torch.no_grad():
            for batch_X, batch_y in val_loader:
                batch_X = batch_X.to(self.device)
                batch_y = batch_y.to(self.device).unsqueeze(1).float()
                
                outputs = self.model(batch_X)
                loss = self.criterion(outputs, batch_y)
                total_loss += loss.item()
        
        avg_loss = total_loss / len(val_loader)
        return avg_loss
    
    def train(self, train_loader, val_loader, epochs=50, early_stopping_patience=10):
        """
        完整訓練流程
        
        Args:
            train_loader: 訓練數據加載器
            val_loader: 驗證數據加載器
            epochs: 訓練週期數
            early_stopping_patience: 早停耐心值
        
        Returns:
            dict: 訓練歷史
        """
        best_val_loss = float('inf')
        patience_counter = 0
        
        for epoch in range(epochs):
            # 訓練
            train_loss = self.train_epoch(train_loader)
            self.history['train_loss'].append(train_loss)
            
            # 驗證
            val_loss = self.validate(val_loader)
            self.history['val_loss'].append(val_loss)
            
            # 早停檢查
            if val_loss < best_val_loss:
                best_val_loss = val_loss
                patience_counter = 0
            else:
                patience_counter += 1
            
            if patience_counter >= early_stopping_patience:
                print(f"早停：第 {epoch+1} 個 epoch 時停止")
                break
            
            if (epoch + 1) % 10 == 0:
                print(f"Epoch {epoch+1}/{epochs} - Train Loss: {train_loss:.4f}, Val Loss: {val_loss:.4f}")
        
        return self.history
    
    def save_model(self, filepath):
        """保存模型"""
        torch.save({
            'model_state_dict': self.model.state_dict(),
            'model_config': {
                'learning_rate': self.learning_rate,
                'history': self.history
            },
            'timestamp': datetime.now().isoformat()
        }, filepath)
    
    def load_model(self, filepath):
        """加載模型"""
        checkpoint = torch.load(filepath, map_location=self.device)
        self.model.load_state_dict(checkpoint['model_state_dict'])
        self.history = checkpoint['model_config'].get('history', {})
    
    def plot_training_history(self):
        """繪製訓練歷史"""
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
        
        # 損失
        ax1.plot(self.history['train_loss'], label='Training Loss', marker='o')
        ax1.plot(self.history['val_loss'], label='Validation Loss', marker='s')
        ax1.set_xlabel('Epoch')
        ax1.set_ylabel('Loss')
        ax1.set_title('Model Loss')
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        
        # 精度（如果有）
        if self.history['train_acc']:
            ax2.plot(self.history['train_acc'], label='Training Accuracy', marker='o')
            ax2.plot(self.history['val_acc'], label='Validation Accuracy', marker='s')
            ax2.set_xlabel('Epoch')
            ax2.set_ylabel('Accuracy')
            ax2.set_title('Model Accuracy')
            ax2.legend()
            ax2.grid(True, alpha=0.3)
        
        plt.tight_layout()
        return fig


def create_data_loaders(X_train, y_train, X_val, y_val, batch_size=32):
    """
    創建 PyTorch 數據加載器
    
    Args:
        X_train: 訓練特征
        y_train: 訓練標籤
        X_val: 驗證特征
        y_val: 驗證標籤
        batch_size: 批大小
    
    Returns:
        tuple: (train_loader, val_loader)
    """
    # 轉換為張量
    X_train_tensor = torch.FloatTensor(X_train.values if hasattr(X_train, 'values') else X_train)
    y_train_tensor = torch.FloatTensor(y_train.values if hasattr(y_train, 'values') else y_train)
    
    X_val_tensor = torch.FloatTensor(X_val.values if hasattr(X_val, 'values') else X_val)
    y_val_tensor = torch.FloatTensor(y_val.values if hasattr(y_val, 'values') else y_val)
    
    # 創建數據集
    train_dataset = TensorDataset(X_train_tensor, y_train_tensor)
    val_dataset = TensorDataset(X_val_tensor, y_val_tensor)
    
    # 創建加載器
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False)
    
    return train_loader, val_loader


# CRISP-DM 建模函數
def crisp_dm_modeling(X_train, y_train, X_val, y_val, 
                      model_type='nn', epochs=50, batch_size=32):
    """
    CRISP-DM: 數據準備 + 建模階段
    
    Args:
        X_train: 訓練特征
        y_train: 訓練標籤
        X_val: 驗證特征
        y_val: 驗證標籤
        model_type: 模型類型 ('nn', 'cnn', 'rnn')
        epochs: 訓練週期
        batch_size: 批大小
    
    Returns:
        dict: 訓練結果
    """
    # 確定設備
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    
    # 創建數據加載器
    train_loader, val_loader = create_data_loaders(X_train, y_train, X_val, y_val, batch_size)
    
    # 創建模型
    input_size = X_train.shape[1]
    
    if model_type == 'nn':
        model = NeuralNetwork(input_size, hidden_sizes=[128, 64, 32], output_size=1)
    elif model_type == 'cnn':
        model = ConvolutionalNeuralNetwork()
    elif model_type == 'rnn':
        model = RecurrentNeuralNetwork(input_size)
    else:
        raise ValueError("模型類型必須是 'nn', 'cnn' 或 'rnn'")
    
    # 初始化訓練器
    trainer = ModelTrainer(model, device=device, learning_rate=0.001)
    trainer.set_criterion(nn.BCEWithLogitsLoss())
    
    # 訓練
    history = trainer.train(train_loader, val_loader, epochs=epochs, early_stopping_patience=10)
    
    return {
        'model': model,
        'trainer': trainer,
        'history': history,
        'device': device
    }


if __name__ == "__main__":
    print("模型層已準備好使用")
    print(f"CUDA 可用: {torch.cuda.is_available()}")

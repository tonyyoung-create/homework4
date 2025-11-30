"""
應用配置驗證和診斷腳本
用於檢查應用是否正確設置
"""

import sys
import os
from pathlib import Path

def check_python_version():
    """檢查 Python 版本"""
    version = sys.version_info
    print(f"✓ Python 版本: {version.major}.{version.minor}.{version.micro}")
    if version.major >= 3 and version.minor >= 8:
        print("  ✅ 版本滿足要求 (>= 3.8)")
        return True
    else:
        print("  ❌ 版本過低，需要 Python 3.8+")
        return False


def check_dependencies():
    """檢查必要的依賴"""
    dependencies = {
        'streamlit': 'Streamlit Web 框架',
        'requests': 'HTTP 客戶端 (用於 Ollama)',
        'pandas': '數據處理',
        'numpy': '數值計算',
        'torch': 'PyTorch 深度學習框架',
        'tensorflow': 'TensorFlow 深度學習框架',
    }
    
    print("\n📦 檢查依賴:")
    all_installed = True
    for package, description in dependencies.items():
        try:
            __import__(package)
            print(f"  ✅ {package:15} - {description}")
        except ImportError:
            print(f"  ❌ {package:15} - {description} (未安裝)")
            all_installed = False
    
    return all_installed


def check_ollama_connection():
    """檢查 Ollama 連接"""
    print("\n🤖 檢查 Ollama 連接:")
    try:
        import requests
        response = requests.get("http://localhost:11434/api/tags", timeout=5)
        if response.status_code == 200:
            print("  ✅ Ollama 服務已連接")
            data = response.json()
            models = data.get('models', [])
            if models:
                print(f"  ✅ 可用模型數: {len(models)}")
                for model in models[:3]:  # 只顯示前 3 個
                    print(f"     - {model.get('name', 'Unknown')}")
            else:
                print("  ⚠️  未發現任何模型，需要下載: ollama pull llama2")
            return True
        else:
            print(f"  ❌ Ollama 返回狀態碼: {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("  ❌ 無法連接到 Ollama (http://localhost:11434)")
        print("  💡 請運行: ollama serve")
        return False
    except Exception as e:
        print(f"  ❌ 錯誤: {str(e)}")
        return False


def check_project_files():
    """檢查項目文件"""
    print("\n📁 檢查項目文件:")
    required_files = {
        'app.py': '主應用入口',
        'cot_dialog.py': 'CoT 對話模組',
        'deeplearning_app.py': 'CRISP-DM 工具',
        'data_layer.py': '數據層',
        'model_layer.py': '模型層',
        'evaluation_layer.py': '評估層',
        'requirements.txt': '依賴列表',
        'OLLAMA_SETUP.md': 'Ollama 安裝指南',
    }
    
    project_dir = Path(__file__).parent
    all_exist = True
    for filename, description in required_files.items():
        filepath = project_dir / filename
        if filepath.exists():
            size = filepath.stat().st_size
            print(f"  ✅ {filename:25} - {description} ({size} bytes)")
        else:
            print(f"  ❌ {filename:25} - {description} (未找到)")
            all_exist = False
    
    return all_exist


def print_quick_start():
    """打印快速開始指南"""
    print("\n" + "="*60)
    print("🚀 快速開始指南")
    print("="*60)
    
    print("""
如果上述檢查有任何 ❌ 標記，請執行以下步驟：

1️⃣  安裝 Ollama:
    - Windows: https://ollama.ai/download
    - macOS: brew install ollama
    - Linux: curl https://ollama.ai/install.sh | sh

2️⃣  下載模型:
    ollama pull llama2

3️⃣  啟動 Ollama 服務:
    ollama serve

4️⃣  安裝 Python 依賴:
    pip install -r requirements.txt

5️⃣  運行應用:
    streamlit run app.py

6️⃣  訪問應用:
    http://localhost:8501
    """)
    
    print("="*60)
    print("📖 更多幫助: 查看 OLLAMA_SETUP.md")
    print("="*60)


def main():
    """主檢查函數"""
    print("="*60)
    print("🔍 AI 混合應用 - 配置診斷工具")
    print("="*60)
    
    checks = {
        'Python 版本': check_python_version(),
        '依賴安裝': check_dependencies(),
        'Ollama 連接': check_ollama_connection(),
        '項目文件': check_project_files(),
    }
    
    print("\n" + "="*60)
    print("📊 檢查摘要")
    print("="*60)
    
    for check_name, result in checks.items():
        status = "✅ 通過" if result else "❌ 失敗"
        print(f"{check_name:15} {status}")
    
    all_passed = all(checks.values())
    
    if all_passed:
        print("\n🎉 所有檢查都通過了！")
        print("您可以直接運行: streamlit run app.py")
    else:
        print("\n⚠️  部分檢查未通過，請按照上述指導進行修復")
        print_quick_start()
    
    print("="*60)


if __name__ == "__main__":
    main()

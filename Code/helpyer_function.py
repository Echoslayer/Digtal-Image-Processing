import subprocess
import sys

def import_or_install(module_name):
    try:
        # 嘗試導入模組
        __import__(module_name)
    except ImportError:
        # 如果模組不存在，則安裝它
        subprocess.check_call([sys.executable, "-m", "pip", "install", module_name])

# 測試範例

import subprocess
import sys

def import_or_install(module_name, install_name=None):
    if install_name is None:
        install_name = module_name
    try:
        # 嘗試導入模組
        __import__(module_name)
    except ImportError:
        # 如果模組不存在，則安裝它
        subprocess.check_call([sys.executable, "-m", "pip", "install", install_name])

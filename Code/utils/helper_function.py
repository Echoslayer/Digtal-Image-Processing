import subprocess
import sys
import numpy as np
import matplotlib.pyplot as  plt 

'''
import sys
import os

# 將父目錄加入到模組搜索路徑中
sys.path.append(os.path.abspath(os.path.join('..')))
'''

def import_or_install(module_name, install_name=None):
    '''
    from utils import helper_function as hp

    hp.import_or_install('cv2', 'opencv-python')
    hp.import_or_install("numpy")
    '''
    if install_name is None:
        install_name = module_name
    try:
        # 嘗試導入模組
        __import__(module_name)
    except ImportError:
        # 如果模組不存在，則安裝它
        subprocess.check_call([sys.executable, "-m", "pip", "install", install_name])

def matrix_values_distribution(data:np.ndarray, bins=20):
    '''
    import utils
    import utils.helper_function

    utils.helper_function.matrix_values_distribution(image, bins=100)
    '''
    # 使用較少的bin數計算數字值的直方圖
    hist, bin_edges = np.histogram(data, bins=bins) 

    # 打印直方圖數據
    print("Histogram values:", hist)
    print("Bin edges:", bin_edges)

    # 使用 matplotlib 顯示數字值分布的直方圖
    plt.figure(figsize=(10, 6))
    plt.hist(data.ravel(), bins=bins, edgecolor='black')  # 使用ravel將數據展平成一維
    plt.title('Number Distribution')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.grid(False)
    plt.show()
    
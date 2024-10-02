import matplotlib.pyplot as plt
import numpy as np
import cv2

def histogram_show(image):
    """顯示圖片的直方圖"""
    
    plt.hist(image.ravel(), bins=256, color='black')
    plt.title('Histogram')
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    plt.show()
    
def equalized_image(image:np.ndarray):

    # 計算原始圖像的直方圖
    original_hist, bins = np.histogram(image.flatten(), 256, [0, 256])

    # 計算累積直方圖
    cdf = original_hist.cumsum()
    
    # 掩蔽CDF中的零值，避免在後續計算中出現問題
    cdf_m = np.ma.masked_equal(cdf, 0)
    cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())
    cdf_final = np.ma.filled(cdf_m, 0).astype('uint8')

    # 使用累積直方圖來進行影像規範化
    image_equalized = cdf_final[image]
    
    return image_equalized

def image_binary(image, standard=2, threshold_value=False, print_threshold=False):
    mean = np.mean(image)
    std_dev = np.std(image)
    
    if not threshold_value:
        threshold_value = min(mean+std_dev*standard, 255) if mean+std_dev*standard >0 else 0
        threshold_value = int(threshold_value)
    
    # 根據門檻值進行二值化
    _, binary_image = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)
    
    if print_threshold:
        print(f"mean+std_dev*standard: {mean+std_dev*standard}, final thershold = {threshold_value}")
    
    return binary_image

def laplacian(image:np.ndarray, ksize=5):
    # 應用拉普拉斯算子
    laplacian = cv2.Laplacian(image, cv2.CV_64F, ksize=ksize)  # 設置kernel size

    # 將結果轉換為絕對值並縮放到8位
    return cv2.convertScaleAbs(laplacian)

def medianBlur(image, size=5):
    """中值濾波器 (Median Filter)"""
    return cv2.medianBlur(image, size)

def gaussianBlur(image, kernel_size=(5, 5), sigma=0):
    """高斯濾波器 (Gaussian Blur)"""
    return cv2.GaussianBlur(image, kernel_size, sigma)

def highPassFilter(image, kernel=None):
    """高通濾波器 (High-Pass Filter)"""
    if kernel is None:
        # 預設的高通濾波器核
        kernel = np.array([[-1, -1, -1],
                           [-1,  8, -1],
                           [-1, -1, -1]])
    return cv2.filter2D(image, -1, kernel)


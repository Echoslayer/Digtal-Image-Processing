import matplotlib.pyplot as plt
import numpy as np
import cv2

def equalized_image(image:np.ndarray):
    """影像規範化"""
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
    """影像二值化"""
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

def get_lines_hough(image, threshold=30, min_line_length=50, max_line_gap=25):
    # 使用 HoughLinesP 函數來檢測影像中的直線
    lines = cv2.HoughLinesP(image, rho=1, theta=np.pi/180, threshold=threshold,
                            minLineLength=min_line_length, maxLineGap=max_line_gap)
    
    # 創建一個空白影像，用於繪製檢測到的直線
    lines_image = np.zeros_like(image)
    
    if lines is not None:
        for line in lines:
            for x1, y1, x2, y2 in line:
                cv2.line(lines_image, (x1, y1), (x2, y2), 255, 1)
    
    return lines_image
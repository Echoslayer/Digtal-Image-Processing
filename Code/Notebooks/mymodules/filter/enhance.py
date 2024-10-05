import numpy as np
import cv2

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

def meanFilter(image, kernel_size=(5, 5)):
    """均值濾波器 (Mean Filter)"""
    mean_filter = np.ones(kernel_size, np.float32) / (kernel_size[0] * kernel_size[1])
    return cv2.filter2D(image, -1, mean_filter)

    
def vertical_sobel(image:np.ndarray, ksize=5, x=1, y=0):
    """sobel算子"""
    sobel_image = cv2.Sobel(image, cv2.CV_64F, x, y, ksize=ksize)
    sobel_image = np.abs(sobel_image)
    sobel_image = np.uint8(np.clip(sobel_image, 0, 255))
    return sobel_image

def horizontal_sobel(image:np.ndarray, ksize=5, x=0, y=1):
    """sobel算子"""
    sobel_image = cv2.Sobel(image, cv2.CV_64F, x, y, ksize=ksize)
    sobel_image = np.abs(sobel_image)
    sobel_image = np.uint8(np.clip(sobel_image, 0, 255))
    return sobel_image

def laplacian(image:np.ndarray, ksize=5):
    """拉普拉斯算子"""
    # 應用拉普拉斯算子
    laplacian = cv2.Laplacian(image, cv2.CV_64F, ksize=ksize)  # 設置kernel size

    # 將結果轉換為絕對值並縮放到8位
    return cv2.convertScaleAbs(laplacian)

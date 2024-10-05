import cv2
import numpy as np

def laplacianOfGaussian(image, ksize=5, sigma=1.0):
    """Laplacian of Gaussian (LoG) 濾波器"""
    gaussian_blur = cv2.GaussianBlur(image, (ksize, ksize), sigma)
    laplacian = cv2.Laplacian(gaussian_blur, cv2.CV_64F)
    # 將 Laplacian 濾波結果轉換為 8 位單通道圖像
    laplacian = np.uint8(np.absolute(laplacian))
    return laplacian

def differenceOfGaussian(image, ksize=(5, 5), sigma1=1, sigma2=2):
    """Difference of Gaussian (DoG) 濾波器"""
    gaussian_1 = cv2.GaussianBlur(image, ksize, sigma1)
    gaussian_2 = cv2.GaussianBlur(image, ksize, sigma2)
    dog = gaussian_1 - gaussian_2
    return dog

def morphologicalGradient(image, kernel_size=(5, 5), shape=cv2.MORPH_RECT):
    """形態學梯度濾波器 (Morphological Gradient Filter)"""
    kernel = cv2.getStructuringElement(shape, kernel_size)
    return cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel)


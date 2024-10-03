import matplotlib.pyplot as plt
import numpy as np
import cv2
    
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

def gaborFilter(image, ksize=31, sigma=4.0, theta=0, lambd=10.0, gamma=0.5, psi=0):
    """Gabor 濾波器 (Gabor Filter)"""
    kernel = cv2.getGaborKernel((ksize, ksize), sigma, theta, lambd, gamma, psi)
    return cv2.filter2D(image, cv2.CV_8UC3, kernel)

def laplacianOfGaussian(image, ksize=5, sigma=1.0):
    """Laplacian of Gaussian (LoG) 濾波器"""
    gaussian_blur = cv2.GaussianBlur(image, (ksize, ksize), sigma)
    laplacian = cv2.Laplacian(gaussian_blur, cv2.CV_64F)
    # 將 Laplacian 濾波結果轉換為 8 位單通道圖像
    laplacian = np.uint8(np.absolute(laplacian))
    return laplacian

def nonLocalMeansFilter(image, h=30, templateWindowSize=7, searchWindowSize=21):
    """非局部均值濾波器 (Non-Local Means Filter)"""
    return cv2.fastNlMeansDenoising(image, None, h, templateWindowSize, searchWindowSize)

def bilateralFilter(image, d=9, sigmaColor=75, sigmaSpace=75):
    """雙邊濾波器 (Bilateral Filter)"""
    return cv2.bilateralFilter(image, d, sigmaColor, sigmaSpace)

def kmeansFilter(image, K=2, criteria=None, attempts=10, flags=cv2.KMEANS_RANDOM_CENTERS):
    """K均值濾波器 (K-means Filter)"""
    if len(image.shape) == 3 and image.shape[2] == 3:
        # 如果圖像是彩色圖像 (RGB)
        Z = image.reshape((-1, 3))  # 將圖像重新形狀為2D數組 (3 通道)
    else:
        # 如果圖像是灰度圖像 (單通道)
        Z = image.reshape((-1, 1))  # 將圖像重新形狀為2D數組 (1 通道)
    
    Z = np.float32(Z)
    
    if criteria is None:
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
    
    ret, label, center = cv2.kmeans(Z, K, None, criteria, attempts, flags)
    center = np.uint8(center)
    res = center[label.flatten()]
    
    # 恢復圖像形狀
    if len(image.shape) == 3 and image.shape[2] == 3:
        result_image = res.reshape((image.shape))
    else:
        result_image = res.reshape((image.shape[0], image.shape[1]))
    
    return result_image

def differenceOfGaussian(image, ksize=(5, 5), sigma1=1, sigma2=2):
    """Difference of Gaussian (DoG) 濾波器"""
    gaussian_1 = cv2.GaussianBlur(image, ksize, sigma1)
    gaussian_2 = cv2.GaussianBlur(image, ksize, sigma2)
    dog = gaussian_1 - gaussian_2
    return dog

def frangiFilter(image):
    """Frangi 濾波器 (Frangi Filter)"""
    from skimage.filters import frangi
    image = frangi(image)
    image = image * 255
    return cv2.convertScaleAbs(image)

def hessianFilter(image):
    """Hessian 濾波器"""
    from skimage.filters import hessian
    image = hessian(image)
    return cv2.convertScaleAbs(image)

def ridgeFilter(image):
    """Ridge 濾波器 (Meijering Filter)"""
    from skimage.filters import meijering
    image = meijering(image)
    return cv2.convertScaleAbs(image)

def morphologicalGradient(image, kernel_size=(5, 5), shape=cv2.MORPH_RECT):
    """形態學梯度濾波器 (Morphological Gradient Filter)"""
    kernel = cv2.getStructuringElement(shape, kernel_size)
    return cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel)

def sideWindowFilter(image, kernel=3, mode='mean'):
    """Side Window Filtering (SWF) 濾波器"""
    try:
        from swf_filter import SideWindowFiltering
    except ImportError:
        from mymodules.swf_filter import SideWindowFiltering
    return SideWindowFiltering(img=image, kernel=kernel, mode=mode)
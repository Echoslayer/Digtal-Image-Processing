import cv2
import numpy as np

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
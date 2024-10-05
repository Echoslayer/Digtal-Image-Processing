import cv2
import numpy as np

def dilate(image: np.ndarray, kernel: np.ndarray = None, iterations: int = 1) -> np.ndarray:
    """膨脹操作 (Dilation)"""
    if kernel is None:
        kernel = np.ones((5, 5), np.uint8)  # 默認為 5x5 的正方形內核
    return cv2.dilate(image, kernel, iterations=iterations)

def erode(image: np.ndarray, kernel: np.ndarray = None, iterations: int = 1) -> np.ndarray:
    """侵蝕操作 (Erosion)"""
    if kernel is None:
        kernel = np.ones((5, 5), np.uint8)  # 默認為 5x5 的正方形內核
    return cv2.erode(image, kernel, iterations=iterations)

def close(image: np.ndarray, kernel: np.ndarray = None) -> np.ndarray:
    """閉運算 (Closing)"""
    if kernel is None:
        kernel = np.ones((5, 5), np.uint8)  # 默認為 5x5 的正方形內核
    return cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

def open(image: np.ndarray, kernel: np.ndarray = None) -> np.ndarray:
    """開運算 (Opening)"""
    if kernel is None:
        kernel = np.ones((5, 5), np.uint8)  # 默認為 5x5 的正方形內核
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

def gradient(image: np.ndarray, kernel: np.ndarray = None) -> np.ndarray:
    """形態學梯度 (Morphological Gradient)"""
    if kernel is None:
        kernel = np.ones((5, 5), np.uint8)  # 默認為 5x5 的正方形內核
    return cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel)

def tophat(image: np.ndarray, kernel: np.ndarray = None) -> np.ndarray:
    """頂帽運算 (Top-Hat)"""
    if kernel is None:
        kernel = np.ones((5, 5), np.uint8)  # 默認為 5x5 的正方形內核
    return cv2.morphologyEx(image, cv2.MORPH_TOPHAT, kernel)

def blackhat(image: np.ndarray, kernel: np.ndarray = None) -> np.ndarray:
    """黑帽運算 (Black-Hat)"""
    if kernel is None:
        kernel = np.ones((5, 5), np.uint8)  # 默認為 5x5 的正方形內核
    return cv2.morphologyEx(image, cv2.MORPH_BLACKHAT, kernel)

def hit_or_miss(image: np.ndarray, kernel: np.ndarray = None) -> np.ndarray:
    """擊中或擊不中操作 (Hit-or-Miss)"""
    if kernel is None:
        kernel = np.array([[0, 1, 0], [1, -1, 1], [0, 1, 0]], np.int8)  # 自定內核
    processed_image = cv2.morphologyEx(image, cv2.MORPH_HITMISS, kernel)
    return processed_image

def skeletonize(image: np.ndarray) -> np.ndarray:
    """骨架化操作 (Skeletonization)"""
    size = np.size(image)
    skel = np.zeros(image.shape, np.uint8)
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
    while True:
        eroded = cv2.erode(image, kernel)
        temp = cv2.dilate(eroded, kernel)
        temp = cv2.subtract(image, temp)
        skel = cv2.bitwise_or(skel, temp)
        image = eroded.copy()
        if cv2.countNonZero(image) == 0:
            break
    return skel

def thinning(image: np.ndarray) -> np.ndarray:
    """細化操作 (Thinning)"""
    return cv2.ximgproc.thinning(image)  # 使用 OpenCV 額外模組進行細化

def thickening(image: np.ndarray, kernel: np.ndarray = None) -> np.ndarray:
    """加粗操作 (Thickening)"""
    if kernel is None:
        kernel = np.ones((3, 3), np.uint8)
    thick = cv2.morphologyEx(cv2.bitwise_not(image), cv2.MORPH_OPEN, kernel)
    processed_image = cv2.bitwise_not(thick)
    return processed_image

def convex_hull(image: np.ndarray) -> np.ndarray:
    """凸包操作 (Convex Hull)"""
    contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    hull = [cv2.convexHull(c) for c in contours]
    hull_image = np.zeros(image.shape, np.uint8)
    cv2.drawContours(hull_image, hull, -1, (255, 255, 255), 1)
    return hull_image

def remove_small_objects(image: np.ndarray, min_size: int) -> np.ndarray:
    """移除小物件 (Remove Small Objects)"""
    contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    mask = np.zeros(image.shape, np.uint8)
    for contour in contours:
        if cv2.contourArea(contour) >= min_size:
            cv2.drawContours(mask, [contour], -1, 255, thickness=cv2.FILLED)
    return mask

def remove_large_objects(image: np.ndarray, max_size: int) -> np.ndarray:
    """移除大物件 (Remove Large Objects)"""
    contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    mask = np.zeros(image.shape, np.uint8)
    for contour in contours:
        if cv2.contourArea(contour) <= max_size:
            cv2.drawContours(mask, [contour], -1, 255, thickness=cv2.FILLED)
    return mask

def watershed_segmentation(image: np.ndarray) -> np.ndarray:
    """分水嶺分割 (Watershed Segmentation)"""
    ret, thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    kernel = np.ones((3, 3), np.uint8)
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
    sure_bg = cv2.dilate(opening, kernel, iterations=3)
    dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
    ret, sure_fg = cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)
    sure_fg = np.uint8(sure_fg)
    unknown = cv2.subtract(sure_bg, sure_fg)
    ret, markers = cv2.connectedComponents(sure_fg)
    markers = markers + 1
    markers[unknown == 255] = 0
    processed_image = cv2.watershed(cv2.cvtColor(image, cv2.COLOR_GRAY2BGR), markers)
    return processed_image

def boundary_extraction(image: np.ndarray) -> np.ndarray:
    """邊界提取 (Boundary Extraction)"""
    eroded_image = cv2.erode(image, np.ones((3, 3), np.uint8))
    processed_image = cv2.subtract(image, eroded_image)
    return processed_image


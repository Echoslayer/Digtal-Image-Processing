import cv2

def nonLocalMeansFilter(image, h=30, templateWindowSize=7, searchWindowSize=21):
    """非局部均值濾波器 (Non-Local Means Filter)"""
    return cv2.fastNlMeansDenoising(image, None, h, templateWindowSize, searchWindowSize)

def bilateralFilter(image, d=9, sigmaColor=75, sigmaSpace=75):
    """雙邊濾波器 (Bilateral Filter)"""
    return cv2.bilateralFilter(image, d, sigmaColor, sigmaSpace)

def sideWindowFilter(image, kernel=3, mode='mean'):
    """Side Window Filtering (SWF) 濾波器"""
    try:
        from Code.Notebooks.mymodules.filter.swf_filter import SideWindowFiltering
    except ImportError:
        from Code.Notebooks.mymodules.filter.swf_filter import SideWindowFiltering
    return SideWindowFiltering(img=image, kernel=kernel, mode=mode)
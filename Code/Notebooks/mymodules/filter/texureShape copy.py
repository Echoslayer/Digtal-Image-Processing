import cv2

def gaborFilter(image, ksize=31, sigma=4.0, theta=0, lambd=10.0, gamma=0.5, psi=0):
    """Gabor 濾波器 (Gabor Filter)"""
    kernel = cv2.getGaborKernel((ksize, ksize), sigma, theta, lambd, gamma, psi)
    return cv2.filter2D(image, cv2.CV_8UC3, kernel)

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
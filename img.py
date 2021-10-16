import cv2
''' 
    함수) 이미지를 더 선명하게 Contrast(대조) 기법을 적용시킴. 
    param : 컬러 이미지 
    return : 대조된 이미지 
'''
def img_Contrast(img):
    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    cl = clahe.apply(l)
    limg = cv2.merge((cl, a, b))
    final = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)

    return final
import cv2
import numpy as np

from PIL import Image
from PIL import ImageEnhance
 

def adjust_contrast(input_image, output_image, factor):
    image = Image.open(input_image)
    enhancer_object = ImageEnhance.Contrast(image)
    out = enhancer_object.enhance(factor)
    out.save(output_image)
 
if __name__ == '__main__':
    adjust_contrast('newKF11.jpg',
                    'finalKF11.jpg',
                    2)

    
img = cv2.imread("finalKF00.jpg")
 


cv2.imshow("Cartoon", img)

cv2.waitKey(0)
cv2.destroyAllWindows()



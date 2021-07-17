import numpy as np
from PIL import ImageGrab, Image
import cv2
import pytesseract

class screenCap:

    def __init__(self, array):
        self.lx = array[0]
        self.ty = array[1]
        self.rx = array[2]
        self.by = array[3]

    def screen_record(self):
        # bounding box is left x, top y, right x, bottom y
        capture = ImageGrab.grab(bbox=(self.lx, self.ty, self.rx, self.by))
        color =  np.array(capture)
        bw = cv2.cvtColor(color, cv2.COLOR_BGR2GRAY)
        cv2.imshow('window',bw)
        
        return bw
            


class ocr:
    def imgtostring(self, img):
        number = pytesseract.image_to_string(img, config='--psm 6 tessedit_char_whitelist=0123456789')
        return number
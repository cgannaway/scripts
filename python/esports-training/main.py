  
import numpy as np
import time
import capture
import cv2


#accuracy windowed - 1920x1080
accu1 = np.array([1115,120,1170,160])

def mainLoop():
    last_time = time.time()
    while True:
        img = screencapture.screen_record()
        num = recognition.imgtostring(img)
        
        print('loop took {} seconds. health: '.format(time.time()-last_time) + num )
        last_time = time.time()

        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

if __name__ == "__main__":
    screencapture = capture.screenCap(accu1)
    recognition = capture.ocr()
    mainLoop()
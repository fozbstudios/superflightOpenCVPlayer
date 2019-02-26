import mss
sct = mss.mss()
import numpy as np
import cv2
cv2.imshow("img",cv2.cvtColor(np.array(sct.grab(sct.monitors[0])),cv2.COLOR_BGRA2GRAY))
cv2.waitKey(10000)

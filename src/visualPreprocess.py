import time
import pdb
import cv2
import mss
import numpy
import i3ipc
#get i3 obj
i3 = i3ipc.Connection()
# pdb.set_trace()
with mss.mss() as sct:
    while "Screen capturing":
        last_time = time.time()
        tree=i3.get_tree() #this line must be in the loop for us to approppriately react to widnow size changes
        print(sct.monitors)
        wind=tree.find_named("VLC")
        #use absolute rather than relative cordinates
        # windAbs = {"top": 90000, "left": wind[0].rect.x, "width": wind[0].rect.width, "height": wind[0].rect.height}
        windAbs = {"top": wind[0].rect.y, "left": wind[0].rect.x, "width": wind[0].rect.width, "height": wind[0].rect.height}
        img =None
        try:
            img = numpy.array(sct.grab(windAbs))
        # except:
        except mss.exception.ScreenShotError:
            details = sct.get_error_details()
            print("error! Quiting")
            print(details)
            quit()
        cv2.imshow('windAbs', cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY))
        print(windAbs)
        print("----------------------------")
        print("fps: {}".format(1 / (time.time() - last_time)))
        # Press "q" to quit
        if cv2.waitKey(1) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break

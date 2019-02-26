import time
import cv2
import mss
import numpy
import i3ipc
#get i3 obj
i3 = i3ipc.Connection()
tree=i3.get_tree()



with mss.mss() as sct:
    # Part of the screen to capture

    while "Screen capturing":
        last_time = time.time()

        wind=tree.find_named(".*uTube.*")
        windAbs = {"top": wind[0].rect.x, "left": wind[0].rect.y, "width": wind[0].rect.width, "height": wind[0].rect.height}
        windRel = {"top": wind[0].window_rect.x, "left": wind[0].window_rect.y, "width": wind[0].window_rect.width, "height": wind[0].window_rect.height}
        treeAbs = {"top": tree.rect.x, "left": tree.rect.y, "width": tree.rect.width, "height": tree.rect.height}
        treeRel = {"top": tree.window_rect.x, "left": tree.window_rect.y, "width": tree.window_rect.width, "height": tree.window_rect.height}
        print(wind[0].name)
        print(wind[0].id)
        print(windAbs)
        print(windRel)
        print(treeAbs)
        print(treeRel)
        # Get raw pixels from the screen, save it to a Numpy array
        img = numpy.array(sct.grab(windAbs))

        # Display the picture
        # cv2.imshow("OpenCV/Numpy normal", img)

        # Display the picture in grayscale
        cv2.imshow('OpenCV/Numpy grayscale', cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY))

        print("fps: {}".format(1 / (time.time() - last_time)))

        # Press "q" to quit
        if cv2.waitKey(0) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break

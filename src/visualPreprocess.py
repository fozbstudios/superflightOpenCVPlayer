import time
import pdb
import cv2
import mss
import numpy
import i3ipc
#get i3 obj
i3 = i3ipc.Connection()
tree=i3.get_tree()


# pdb.set_trace()
with mss.mss() as sct:
    # Part of the screen to capture

    while "Screen capturing":
        last_time = time.time()
        print(sct.monitors)
        # wind=tree.find_named("VLC")
        wind=tree.find_named("AUR")
        windRel = {"top": wind[0].window_rect.y, "left": wind[0].window_rect.x, "width": wind[0].window_rect.width, "height": wind[0].window_rect.height}
        treeAbs = {"top": tree.rect.x, "left": tree.rect.y, "width": tree.rect.width, "height": tree.rect.height}
        windAbs = {"top": wind[0].rect.y, "left": wind[0].rect.x, "width": wind[0].rect.width, "height": wind[0].rect.height}
        treeRel = {"top": tree.window_rect.x, "left": tree.window_rect.y, "width": tree.window_rect.width, "height": tree.window_rect.height}
        # print(wind[0].parent)
        # print(wind[0].id)
        # print(windAbs)
        # print(windRel)
        parent=wind[0].parent
        # print(treeAbs)
        # print(treeRel)
        # Get raw pixels from the screen, save it to a Numpy array
        parAbs = {"top": parent.rect.x, "left": parent.rect.y, "width": parent.rect.width, "height": parent.rect.height}
        parRel = {"top": parent.window_rect.x, "left": parent.window_rect.y, "width": parent.window_rect.width, "height": parent.window_rect.height}
        # treeAbs = {"top": tree.rect.x, "left": tree.rect.y, "width": tree.rect.width, "height": tree.rect.height}
        # treeRel = {"top": tree.window_rect.x, "left": tree.window_rect.y, "width": tree.window_rect.width, "height": tree.window_rect.height}
        img = numpy.array(sct.grab(windAbs))
        try:
            img = numpy.array(sct.grab(windAbs))
        except:
        # except ScreenShotError:
            details = sct.get_error_details()
            print(details)
        img2 = numpy.array(sct.grab(windRel))
        # img3 = numpy.array(sct.grab(treeAbs))
        # img4 = numpy.array(sct.grab(treeRel))

        # Display the picture
        # cv2.imshow("OpenCV/Numpy normal", img)
        pImg=numpy.array(sct.grab(parAbs))
        # pImg2=numpy.array(sct.grab(parRel))
        # Display the picture in grayscale
        print(windAbs)
        # cv2.imshow('windAbs', cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY))
        cv2.imshow('windRel', cv2.cvtColor(img2, cv2.COLOR_BGRA2GRAY))
        # cv2.imshow('treeAbs', cv2.cvtColor(img3, cv2.COLOR_BGRA2GRAY))
        # cv2.imshow('treeRel', cv2.cvtColor(img4, cv2.COLOR_BGRA2GRAY))

        # cv2.imshow('parAbs', cv2.cvtColor(pImg, cv2.COLOR_BGRA2GRAY))
        # cv2.imshow('parRel', cv2.cvtColor(pImg2, cv2.COLOR_BGRA2GRAY))

        print("fps: {}".format(1 / (time.time() - last_time)))
        print("----------------------------")
        print(windRel)
        print(windAbs)
        print(parRel)
        print(parAbs)
        # print(pImg2)
        # Press "q" to quit
        if cv2.waitKey(1) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break

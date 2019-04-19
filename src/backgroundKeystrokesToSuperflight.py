import time

from pywinauto import application, keyboard 
appl=application.Application()
app = appl.connect(process=19364)
app.top_window().type_keys("k")
# time.sleep(15)
# print("sending keys to superflight in 15 seconds! alt tab now")

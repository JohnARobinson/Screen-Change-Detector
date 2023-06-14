from PIL import ImageGrab
import pyautogui as pg
from PIL import Image
from PIL import ImageChops
import pyscreenshot
import time


refreshClicked = 0

#mouse locator 1
#for i in range(10000):
#    x = pg.position()
#   print(x[0], x[1])

#mouse locator 2 (Better version
"""
try:
   while True:
        x = pg.position()
        print(x[0], x[1],end="\r", flush=True)
        #press ctrl c to exit
except KeyboardInterrupt:
    pass
"""

#for clicking the refresh button
#pg.click(84,50)
         #x , y
time.sleep(10)

#bbox (starting location, size)
#screen capture 1
#image = ImageGrab.grab(bbox=(480,206,1000,500))
#image.show()
#image.save('sc.png')   

#screen capture 2
#pic = pyscreenshot.grab(bbox=(200, 300, 1500, 1000))
#pic.show()
#pic.save("sc.png")

#test, creates second image
#pic = pyscreenshot.grab(bbox=(200, 300, 1500, 1000))
#pic.show()
#pic.save("sc_test.png")

#im1 = Image.open("sc.png")
#im2 = Image.open("sc_test.png")
#diff = ImageChops.difference(im2, im1)
#if diff.getbbox():
#    print("images are different")
#else:
#   print("images are the same")
#diff.show()
from PIL import ImageGrab
import pyautogui as pg
from PIL import Image
from PIL import ImageChops
import pyscreenshot
import time
import mouse


refreshClicked = 0

#seconds
timeBetweenCheck = 300

def refresh():
    #for clicking the refresh button
    pg.click(84,50)
             #x , y   
def initialCheck():
    pic = pyscreenshot.grab(bbox=(120, 360, 1660, 900))
    #pic.show()
    pic.save("sc.png")
    
def reCenter():
    #scroll after refresh to insure correct calender location
    pg.click(0, 200)
    mouse.wheel(-20)
def nextMonth():
    #click right most icon moving calender foward a month
    pg.click(0, 200)
    mouse.wheel(20)
    time.sleep(10)
    #pg.moveTo(1215, 410)
    pg.click(1215, 410)



#save image for first 3 months  
def imageCheckMonth1():
    pic = pyscreenshot.grab(bbox=(120, 360, 1660, 900))
    #pic.show()
    pic.save("sc1.png")
def imageCheckMonth2():
    pic = pyscreenshot.grab(bbox=(120, 360, 1660, 900))
    #pic.show()
    pic.save("sc2.png")
def imageCheckMonth3():
    pic = pyscreenshot.grab(bbox=(120, 360, 1660, 900))
    #pic.show()
    pic.save("sc3.png")

#test image for first 3 months    
def imageTestMonth1():
    pic = pyscreenshot.grab(bbox=(120, 360, 1660, 900))
    #pic.show()
    pic.save("sc1_test.png")
def imageTestMonth2():
    pic = pyscreenshot.grab(bbox=(120, 360, 1660, 900))
    #pic.show()
    pic.save("sc2_test.png")
def imageTestMonth3():
    pic = pyscreenshot.grab(bbox=(120, 360, 1660, 900))
    #pic.show()
    pic.save("sc3_test.png")
    
#compare 3 months of the calender for changes
def imageCmpMonth1():
    im1 = Image.open("sc1.png")
    im2 = Image.open("sc1_test.png")
    diff = ImageChops.difference(im2, im1)
    if diff.getbbox():
        print("month 1 is different")
    else:
       print("month 1 is the same")
    #diff.show()
    
def imageCmpMonth2():
    im1 = Image.open("sc2.png")
    im2 = Image.open("sc2_test.png")
    diff = ImageChops.difference(im2, im1)
    if diff.getbbox():
        print("month 2 is different")
    else:
       print("month 2 is the same")
    #diff.show()
def imageCmpMonth3():
    im1 = Image.open("sc3.png")
    im2 = Image.open("sc3_test.png")
    diff = ImageChops.difference(im2, im1)
    if diff.getbbox():
        print("month 3 is different")
    else:
       print("month 3 is the same")
    #diff.show()

def mouseLocator():
    try:
        while True:
            x = pg.position()
            print(x[0], x[1],end="\r", flush=True)
            #press ctrl c to exit
    except KeyboardInterrupt:
        pass


#initial test

reCenter()
time.sleep(10)
imageCheckMonth1()
#wait 1 min
time.sleep(30)
refresh()
time.sleep(10)
reCenter()
time.sleep(10)
imageTestMonth1()
imageCmpMonth1()

time.sleep(20)
nextMonth()
time.sleep(10)

reCenter()
time.sleep(10)
imageCheckMonth2()
#wait 1 min
time.sleep(30)
refresh()
time.sleep(10)
reCenter()
time.sleep(10)
imageTestMonth2()
imageCmpMonth2()

#planned 3 month test
"""
#month 1
reCenter()
time.sleep(10)
imageCheckMonth1()
time.sleep(10)
nextMonth()
time.sleep(10)

#month 2
reCenter()
time.sleep(10)
imageCheckMonth2()
time.sleep(10)
nextMonth()
time.sleep(10)

#month 3
reCenter()
time.sleep(10)
imageCheckMonth3()
time.sleep(10)
nextMonth()
time.sleep(10)

#wait time between checks currently 5min
time.sleep(timeBetweenCheck)

#month 1
refresh()
time.sleep(10)
reCenter()
time.sleep(10)
imageTestMonth1()
imageCmpMonth1()
time.sleep(10)
nextMonth()
time.sleep(10)

reCenter()
time.sleep(10)
imageTestMonth2()
imageCmpMonth2()
time.sleep(10)
nextMonth()
time.sleep(10)

time.sleep(10)
imageTestMonth3()
imageCmpMonth3()
time.sleep(10)
nextMonth()
time.sleep(10)
"""

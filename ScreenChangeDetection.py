from PIL import ImageGrab
import pyautogui as pg
from PIL import Image
from PIL import ImageChops
import pyscreenshot
import time
import mouse

import smtplib
import ssl
from email.message import EmailMessage
from pygame import mixer
from datetime import datetime

import os



onediff = 0
twodiff = 0

#seconds
timeBetweenCheck = 60

# 8hrs
t_end = time.time() + 60 * 480

def sound():
    mixer.init()
    mixer.music.load("tts_appointment.mp3")
    mixer.music.play()

    while mixer.music.get_busy():  
        time.sleep(1)

def refresh():
    #for clicking the refresh button
    #pg.click(84,50)
    pg.click(84,55)
             #x , y   
def initialCheck():
    pic = pyscreenshot.grab(bbox=(120, 360, 1660, 900))
    #pic.show()
    pic.save("sc.png")
    
def reCenter():
    #scroll after refresh to insure correct calender location
    pg.click(10, 200)
    #mouse.wheel(-20)
    mouse.wheel(20)
def nextMonth():
    #click right most icon moving calender foward a month
    pg.click(0, 200)
    mouse.wheel(20)
    time.sleep(10)
    #pg.moveTo(1215, 410)
    #pg.click(1215, 435)
    pg.click(605, 285)



#save image for first 3 months  
def imageCheckMonth1():
    #pic = pyscreenshot.grab(bbox=(120, 300, 1660, 900))
    pic = pyscreenshot.grab(bbox=(60, 300, 900, 1000))
    #pic.show()
    time.sleep(15)
    pic.save("sc1.png")
    time.sleep(15)
def imageCheckMonth2():
    pic = pyscreenshot.grab(bbox=(60, 300, 900, 1000))
    #pic.show()
    time.sleep(15)
    pic.save("sc2.png")
    time.sleep(15)
def imageCheckMonth3():
    pic = pyscreenshot.grab(bbox=(60, 300, 900, 1000))
    #pic.show()
    pic.save("sc3.png")

#test image for first 3 months    
def imageTestMonth1():
    pic = pyscreenshot.grab(bbox=(60, 300, 900, 1000))
    #pic.show()
    time.sleep(15)
    pic.save("sc1_test.png")
    time.sleep(15)
def imageTestMonth2():
    pic = pyscreenshot.grab(bbox=(60, 300, 900, 1000))
    #pic.show()
    time.sleep(15)
    pic.save("sc2_test.png")
    time.sleep(15)
def imageTestMonth3():
    pic = pyscreenshot.grab(bbox=(60, 300, 900, 1000))
    #pic.show()
    pic.save("sc3_test.png")
    
#compare 3 months of the calender for changes
def imageCmpMonth1():
    im1 = Image.open("sc1.png")
    im2 = Image.open("sc1_test.png")
    diff = ImageChops.difference(im2, im1)
    if diff.getbbox():
        print("month 1 is different##########################")

        sound()
        
        #os.remove("sc1.png")
        #os.remove("sc1_test.png")
        onediff = 1
        time.sleep(5)
        emailUpdateL()
        emailUpdateJ()
        onediff = 0
    else:
       print("month 1 is the same")
    #diff.show()
    
def imageCmpMonth2():
    im1 = Image.open("sc2.png")
    im2 = Image.open("sc2_test.png")
    diff = ImageChops.difference(im2, im1)
    if diff.getbbox():
        print("month 2 is different ########################")

        #play sound
        
        sound()
        

        twodiff = 1
        time.sleep(5)
        emailUpdateL()
        emailUpdateJ()
        twodiff = 0
    else:
       print("month 2 is the same")
    #diff.show()
def imageCmpMonth3():
    im1 = Image.open("sc3.png")
    im2 = Image.open("sc3_test.png")
    diff = ImageChops.difference(im2, im1)
    if diff.getbbox():
        print("month 3 is different")
        sound()
        emailUpdateL()
        emailUpdateJ()
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

def emailUpdateL():
    email_address = 'jbotnotification@gmail.com'
    email_password = 'sbmmsinptntqbumf'
    email_receiver = 'globalpartners@verizon.net'
    
    subject = 'New Elisa Appointment Available!'
    body = """
    New Elisa Appointment Available!
    https://www.sosi1.com/login

    """
    em = EmailMessage()
    em['From'] = email_address
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_address, email_password)
        smtp.sendmail(email_address, email_receiver, em.as_string())


def emailUpdateJ():
    email_address = 'jbotnotification@gmail.com'
    email_password = 'sbmmsinptntqbumf'
    email_receiver = 'jrobinson843@gmail.com'
    
    subject = 'New Elisa Appointment Available!'
    body = """
    New Elisa Appointment Available!
    https://www.sosi1.com/login
    
    
    """
    em = EmailMessage()
    em['From'] = email_address
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body) 
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_address, email_password)
        smtp.sendmail(email_address, email_receiver, em.as_string())


def updateTime():
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    return(current_time)


#////////////////////////
#test area

#refresh()

#zoom out to 50%

#imageCheckMonth1()
#imageTestMonth1()
#imageCmpMonth1()



#///////////////////////

while time.time() < t_end:
    current_time = 0
#month 1

    current_time = updateTime()
    print("Status: Starting...")
    current_time = updateTime()
    print("Status: ",current_time,": click & recenter")
    time.sleep(5)
    reCenter()
    time.sleep(25)
    current_time = updateTime()
    print("Status: ",current_time,": Image Check 1")
    imageCheckMonth1()

    time.sleep(15)
    current_time = updateTime()
    print("Status: ", current_time, ": Switch Month")
    nextMonth()
    time.sleep(15)

    #month 2
    current_time = updateTime()
    print("Status: ", current_time, ": click & recenter")
    time.sleep(5)
    reCenter()
    time.sleep(25)
    current_time = updateTime()
    print("Status: ", current_time, ": Image Check 2")
    imageCheckMonth2()
    time.sleep(15)

    #wait time between checks currently 5min
    current_time = updateTime()
    print("Status: ",current_time,": Waiting for: ")
    print(timeBetweenCheck / 60)
    print("minutes")
    time.sleep(timeBetweenCheck)

    #month 1
    current_time = updateTime()
    print("Status: ", current_time, ": click & refresh")
    refresh()
    time.sleep(20)
    current_time = updateTime()
    print("Status: ", current_time, ": click & recenter")
    reCenter()
    time.sleep(25)
    current_time = updateTime()
    print("Status: ", current_time, ": Image Test Check 1")
    imageTestMonth1()
    time.sleep(15)
    current_time = updateTime()
    print("Status: ", current_time, ": Image Compare 1")
    imageCmpMonth1()
    
    time.sleep(15)
    current_time = updateTime()
    print("Status: ", current_time, ": Switch Month")
    nextMonth()
    time.sleep(30)
    
    #month 2
    reCenter()
    current_time = updateTime()
    print("Status: ", current_time, ": click & recenter")
    time.sleep(20)
    current_time = updateTime()
    print("Status: ", current_time, ": Image Test Check 2")
    imageTestMonth2()
    time.sleep(15)
    current_time = updateTime()
    print("Status: ", current_time, ": Image Compare 2")
    imageCmpMonth2()
    
    current_time = updateTime()
    print("Status: ", current_time, ": click & refresh, Starting Cycle Again!")
    refresh()

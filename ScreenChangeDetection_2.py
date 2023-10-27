import time

#mouse clicking imports
import pyautogui as pg
import mouse

#screen capture import
import pyscreenshot

#email imports
import smtplib
import ssl
from email.message import EmailMessage
from datetime import datetime

#cv2 computer vision
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
import numpy as np
import cv2

#page Loading Status
page_Load = 0

#seconds
timeBetweenCheck = 30

# 8hrs
t_end = time.time() + 60 * 480

# state update for prints
def stateUpdate(current_time, state):
    """
    0: start
    1: recenter
    2: refresh
    3: switch month
    4: image Check 1
    5: image Check 2
    6: image Test 1
    7: image Test 2
    8: Image Compare 1
    9: Image Compare 1
    10: wait
    11: end
    """
    current_time = updateTime()
    if(state == 0):
        print("Status: Starting...")
    if(state == 1):
        print("Status: ",current_time,": click & recenter")
    if(state == 2):
        print("Status: ", current_time, ": click & refresh")
    if(state == 3):
        print("Status: ", current_time, ": Switch Month")
    if(state == 4):
        print("Status: ",current_time,": Image Check 1")
    if(state == 5):
        print("Status: ",current_time,": Image Check 2")
    if(state == 6):
        print("Status: ",current_time,": Image Test 1")
    if(state == 7):
        print("Status: ",current_time,": Image Test 2")
    if(state == 8):
        print("Status: ",current_time,": Image Compare 1")
    if(state == 9):
        print("Status: ",current_time,": Image Compare 2")
    if(state == 10):
        print("Status: ",current_time,": Waiting for: ",timeBetweenCheck)
    if(state == 11):
        print("Status: ", current_time, ": click & refresh, Starting Cycle Again!")
    if(state == 12):
        print("Status: ",current_time,": ##### Appointment Found #####")
    if(state == 13):
        print("Status: ",current_time,": No Appointment Found ")
    if(state == 14):
        print("Status: ",current_time,": Successful Load")
    if(state == 15):
        print("Status: ",current_time,": Unsuccessful Load, Reloading...")

#for clicking the refresh button
def refresh():
    image = cv2.imread("sc1.png")
    template = cv2.imread("refresh.png")
    heat_map = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
    h, w, _ = template.shape
    y, x = np.unravel_index(np.argmax(heat_map), heat_map.shape)
    cv2.rectangle(image, (x,y), (x+w, y+h), (0,0,255), 5)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    #click spot
    click(x+23, y+55)
    time.sleep(5)

#scroll after refresh to insure correct calender location  
def reCenter(time):
    stateUpdate(time, 1)
    pg.click(10, 200)
    #mouse.wheel(-20)
    mouse.wheel(20)

#check appointment
def imageScreenShot1(startX, startY, height, width):
    pic = pyscreenshot.grab(bbox=(startX, startY, height, width))
    time.sleep(5)
    pic.save("sc1.png")
    time.sleep(5)
    return 1
def imageScreenShot2(startX, startY, height, width):
    pic = pyscreenshot.grab(bbox=(startX, startY, height, width))
    time.sleep(5)
    pic.save("sc2.png")
    time.sleep(5)

# testing method
def mouseLocator():
    try:
        while True:
            x = pg.position()
            print(x[0], x[1],end="\r", flush=True)
            #press ctrl c to exit
    except KeyboardInterrupt:
        pass

#email function
def emailUpdateL():
    email_address = '*************************'
    email_password = '*************************'
    email_receiver = '*************************'
    
    subject = 'New Appointment Available!'
    body = """
    New Appointment Available!
    *************************

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
    email_address = '*************************'
    email_password = '*************************'
    email_receiver = '*************************'
    
    subject = 'New Appointment Available!'
    body = """
    New Appointment Available!
    *************************
    
    
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

#simple wait
def wait(timeAmount):
    time.sleep(timeAmount)

def start(time):
    stateUpdate(time, 0)
    return 1

#loop time update
def updateTime():
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    return(current_time)

#click location
def click(x,y):
    pg.click(x, y)

#find next month and click button
def findNextMonth():
    image = cv2.imread("sc1.png")
    template = cv2.imread("leftArrow2.png")
    heat_map = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
    h, w, _ = template.shape
    y, x = np.unravel_index(np.argmax(heat_map), heat_map.shape)
    #cv2.rectangle(image, (x,y), (x+w, y+h), (0,0,255), 5)
    #plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    #click spot
    click(x+23, y+55)
    time.sleep(15)

#detect new appointments
def detectNewAppointment1(imageToScan):
    
    image = cv2.imread(imageToScan)
    template = cv2.imread("newAppointmentSquare4.png")

    result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.9
    flag = False
    if np.amax(result) > threshold:
        flag = True
    return flag
def detectNewAppointment2(imageToScan):
    
    image = cv2.imread(imageToScan)
    template = cv2.imread("newAppointmentSquare5.png")

    result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.9
    flag = False
    if np.amax(result) > threshold:
        flag = True
    return flag

#detecting if web browser loaded
def loadStatus():
    wait(10)
    image = cv2.imread("sc1.png")
    template = cv2.imread("availableStatusButton.png")
    result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.9
    flag = False
    if np.amax(result) > threshold:
        stateUpdate(current_time, 14)
        flag = True
        return 1
    else:
        stateUpdate(current_time, 15)
        return 0

##############################################################
#overall state
startState = 0

# all 0,1 or 2
pictureState = 0

current_time = 0

#loadStatus()

#    0: start
#    1: recenter
#    2: refresh
#    3: switch month
#    4: image Check 1
#    5: image Check 2
#    6: image Test 1
#    7: image Test 2
#    8: Image Compare 1
#    9: Image Compare 1
#    10: wait
#    11: end

while time.time() < t_end:
    #time tracker
    current_time = 0

    #0-2 pre and end loop checks state
    loopState = 1

    #overall state
    startState = 0

    # all 0,1 or 2
    pictureState = 0

    img1_Appointment_Status1 = False
    img1_Appointment_Status2 = False
    img2_Appointment_Status1 = False
    img2_Appointment_Status2 = False

    totalMonthCount = 6
    totalMonthCheck = 0

    #do later
    #pre loop
    """
    if loopState == 0:

        while(totalMonthCheck < totalMonthCount):
            


            if(startState == 0):
                startState = start(current_time)
            totalMonthCheck = totalMonthCheck + 1

    """
    #main loop
    if loopState == 1:
        while(1):

            #update time
            current_time = updateTime()

            if(startState == 4):
                while(1):
                    reCenter(current_time)
                    refresh()
                    imageScreenShot1(20, 50, 950, 1000)
                    if loadStatus() == 1:
                        break
                    if loadStatus() == 0:
                       continue
                
                stateUpdate(current_time, 11)
                startState = 0
                pictureState = 0
                break
            #wait
            if(startState == 3):
                stateUpdate(current_time, 10)
                startState = 4
                wait(timeBetweenCheck)

            #check month 1 & 2#########################################
            if(startState == 2):
                #check month 1
                if(pictureState == 0):
                    pictureState = imageScreenShot1(20, 50, 950, 1000)
                    image1 = ("sc1.png")
                    img1_Appointment_Status1 = detectNewAppointment1(image1)
                    img1_Appointment_Status2 = detectNewAppointment2(image1)
                    #print(img1_Appointment_Status2, img1_Appointment_Status1)
                    if(img1_Appointment_Status1 == False and img1_Appointment_Status2 == False):
                        stateUpdate(current_time, 13)
                    if(img1_Appointment_Status1 == True or img1_Appointment_Status2 == True):
                        stateUpdate(current_time, 12)
                        #emailUpdateL()
                        #emailUpdateJ()
                #swap month
                if(pictureState == 1):
                    while(1):
                        reCenter(current_time)
                        imageScreenShot1(20, 50, 950, 1000)
                        findNextMonth()
                        if loadStatus() == 1:
                            break
                        if loadStatus() == 0:
                            refresh()
                    pictureState = pictureState + 1
                    stateUpdate(current_time, 3)

                #check month 2
                if(pictureState == 2):
                    imageScreenShot2(20, 50, 950, 1000)
                    image2 = ("sc2.png")
                    img2_Appointment_Status1 = detectNewAppointment1(image2)
                    img2_Appointment_Status2 = detectNewAppointment2(image2)
                    if(img2_Appointment_Status1 == False and img2_Appointment_Status2 == False):
                        stateUpdate(current_time, 13)
                    if(img2_Appointment_Status1 == True or img2_Appointment_Status2 == True):
                        stateUpdate(current_time, 12)
                        #emailUpdateL()
                        #emailUpdateJ()
                    startState = 3

            #recenter 1st
            if(startState == 1):
                reCenter(current_time)
                startState = 2

            #start
            if(startState == 0):
                startState = start(current_time)

        #do later
        #end loop check
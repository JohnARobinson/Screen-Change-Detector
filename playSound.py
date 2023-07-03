import time
from pygame import mixer


mixer.init()
mixer.music.load("tts_appointment.mp3")
mixer.music.play()

while mixer.music.get_busy():  
    time.sleep(1)
# wait for music to finish playing
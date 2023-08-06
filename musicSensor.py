from gpiozero import MotionSensor
from time import sleep
import pygame
import os
import random
from threading import Thread, Event
 
pir = MotionSensor(4)
songsFilePath = "/home/myFiles/Music/"
pygame.init()
pygame.mixer.init()


class TimerThread(Thread):
    def __init__(self):
        super(TimerThread, self).__init__()
        self.timer = 0
        
        self.daemon = True
        
    def run(self):
        while True:
            if self.timer == 1:
                sleep(1)
                pygame.mixer.music.stop()
                self.timer = 0
            elif self.timer == 0:
                sleep(1)
            else:
                self.timer -= 1
                sleep(1)

        

#30 second buffer after turned on and set up
sleep(30)
t = TimerThread()
t.start()
while True: 
    pir.wait_for_motion()
    if not pygame.mixer.music.get_busy():
        songFile = os.path.join(songsFilePath, random.choice(os.listdir(songsFilePath)))
        pygame.mixer.music.load(songFile)
        pygame.mixer.music.play()
        sleep(60)
        
    pir.wait_for_no_motion()
    t.timer = 30
 
    

"""
this is all the code I have done for my code. I am useing rover number 1.
"""

import RPi.GPIO as GPIO
from time import sleep
import random

GPIO.setmode(GPIO.BCM)

GPIO.setup(24, GPIO.OUT)
GPIO.setup(23, GPIO.OUT) 
GPIO.setup(27, GPIO.OUT) 
GPIO.setup(17, GPIO.OUT)
GPIO.setup(13, GPIO.IN)                

while True:
    i=GPIO.input(13)

    GPIO.output(24, GPIO.HIGH)
    GPIO.output(27, GPIO.HIGH)


              
    if i==1:
        print("CLEAR")

    elif i==0:
        GPIO.output(24, GPIO.LOW)
        GPIO.output(27, GPIO.LOW)
            
        GPIO.output(23, GPIO.HIGH)
        GPIO.output(17, GPIO.HIGH)
        sleep(1)
        GPIO.output(17, GPIO.LOW)
        GPIO.output(17, GPIO.LOW)
        sleep(1)
        number=random.random()
        number=10*number 

        if number > 5:
            GPIO.output(27, GPIO.HIGH)
            sleep(1)
            GPIO.output(27, GPIO.LOW)

        elif number < 5:
            GPIO.output(24, GPIO.HIGH)
            sleep(1)
            GPIO.output(24, GPIO.LOW)
 
                     




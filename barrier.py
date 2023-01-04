import RPi.GPIO as GPIO
import time

class Barrier:

    def __init__(self) :
        # Set GPIO numbering mode
        GPIO.setmode(GPIO.BOARD)

        # Set pin 11 as an output, and set servo1 as pin 11 as PWM
        GPIO.setup(11,GPIO.OUT)
        self.servo1 = GPIO.PWM(11,50) # Note 11 is pin, 50 = 50Hz pulse
        self.servo1.start(0)
        self.duty = 2
        #start PWM running, but wit

    def open_barrier(self):
        print ("Turning back to 90 degrees for 2 seconds")
        self.servo1.ChangeDutyCycle(7)

    def close_barrier(self):
        print ("Turning back to 0 degrees")
        self.servo1.ChangeDutyCycle(2)
        time.sleep(0.5)
        self.servo1.ChangeDutyCycle(0)
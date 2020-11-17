from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while(1):
    if GPIO.input(21) == 0:
        print "Tank 1 needs more water"
        sleep(5)
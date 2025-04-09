import RPi.GPIO as GPIO
import time
dac = [8, 11, 7, 1, 0, 5, 12, 6]
n = [[1,1,1,1,1,1,1,1], #255 
      [0,1,1,1,1,1,1,1], #127
      [0,1,0,0,0,0,0,0], #64
      [0,0,1,0,0,0,0,0], #32
      [0,0,0,0,0,1,0,1], #5
      [0,0,0,0,0,0,0,0]  #0
      ] 

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

for i in range(len(n)):
    GPIO.output(dac, n[i])
    time.sleep(15)
    GPIO.output(dac, 0)

GPIO.cleanup()

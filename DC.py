import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

outpin = 7
frequency = 100

GPIO.setup(outpin,GPIO.OUT)

p=GPIO.PWM(outpin,frequency)
p.start(0)
p.ChangeDutyCycle(80)

try:
	while True:
		for i in range(100):
#			p.ChangeDutyCycle(i)
			time.sleep(0.02)
		for i in range(100):
#			p.ChangeDutyCycle(100-i)
			time.sleep(0.02)
except KeyboardInterrupt:
	p.stop()
	GPIO.cleanup()	
	print "stopped"

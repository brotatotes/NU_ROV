import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

def forward():
	GPIO.output(forwardpin, 1)              #sets pin to high
	GPIO.output(backwardpin,0)              #sets pin to low

def backward():
	GPIO.output(forwardpin, 0)              #sets pin to low
	GPIO.output(backwardpin,1)              #sets pin to high

def stop():
        p.ChangeDutyCycle(0)                   #0% duty cycle

def speedUp(speed):
        p.ChangeDutyCycle(speed)                

def slowDown(speed):
	p.ChangeDutyCycle(speed)

def main(): 
	forwardpin = 11                         #11 high is forward
	backwardpin = 13                        #13 low is forward
	
	outpin = 7                              #PWM output pin is GPIO pin 7
	frequency = 100                         #frequency is 100 Hz

	current_speed = 0			#keeps track of the current speed(duty cycle) of the RC car

	GPIO.setup(outpin,GPIO.OUT)             #sets up the pin for GPIO output
	GPIO.setup(forwardpin,GPIO.OUT)
	GPIO.setup(backwardpin,GPIO.OUT)

	p=GPIO.PWM(outpin,frequency)            #configures the pin for pwm output
        p.start(0)
        p.ChangeDutyCycle(0)                   #starts with 0% duty cycle

	try:
                while True:
                        time.sleep(0.02)		# add in continuous keyboard reading here, call appropriate functions

        except KeyboardInterrupt:
                p.stop()
                GPIO.cleanup()
                print "stopped"

main()



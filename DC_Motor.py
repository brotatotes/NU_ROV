import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

def forward(forwardpin,backwardpin):
	GPIO.output(forwardpin, 1)              #sets pin to high
	GPIO.output(backwardpin,0)              #sets pin to low
	print "forward"

def backward(forwardpin,backwardpin):
	GPIO.output(forwardpin, 0)              #sets pin to low
	GPIO.output(backwardpin,1)              #sets pin to high
	print "backward"

def stop(p):
        p.ChangeDutyCycle(0)                   #0% duty cycle
	print "stop"

def speedUp(speed):
        p.ChangeDutyCycle(speed)                

def slowDown(speed):
	p.ChangeDutyCycle(speed)

def turnLeft(leftpin,rightpin):
	GPIO.output(leftpin,1)
	GPIO.output(rightpin,0)

def turnRight(leftpin,rightpin):
	GPIO.output(leftpin,0)
	GPIO.output(rightpin,1)





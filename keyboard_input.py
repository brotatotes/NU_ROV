import pygame, sys
import DC_Motor as dc
import RPi.GPIO as GPIO
pygame.init()

size = width, height = 320,240

screen = pygame.display.set_mode(size)


forwardpin = 11                         #11 high is forward
backwardpin = 13                        #13 low is forward
leftpin = 12
rightpin = 15
highpin = 22

outpin = 7                              #PWM output pin is GPIO pin 7
frequency = 100	                         #frequency is 100 Hz

current_speed = 0 
base_speed = 75
turbo_speed = 100
snail_speed = 50

GPIO.setup(outpin,GPIO.OUT)             #sets up the pin for GPIO output
GPIO.setup(forwardpin,GPIO.OUT)
GPIO.setup(backwardpin,GPIO.OUT)
GPIO.setup(leftpin,GPIO.OUT)
GPIO.setup(rightpin,GPIO.OUT)
GPIO.setup(highpin, GPIO.OUT)

#GPIO.output(highpin,1)
GPIO.output(forwardpin, 1)              #sets pin to high
GPIO.output(backwardpin,0)
GPIO.output(leftpin, 0)              #sets pin to low
GPIO.output(rightpin,0)		     #sets pin to low

high = GPIO.PWM(highpin,frequency)
high.start(0)
p=GPIO.PWM(outpin,frequency)            #configures the pin for pwm output
p.start(0)


while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
	state = pygame.key.get_pressed()
	w = state[pygame.K_w]
	a = state[pygame.K_a]
	s = state[pygame.K_s]
	d = state[pygame.K_d]
	q = state[pygame.K_q]
	x = state[pygame.K_x]
	z = state[pygame.K_z]
	# print "W:" + str(state[pygame.K_w]) + " S:" + str(state[pygame.K_s]) + " A:" + str(state[pygame.K_a]) + " D:" + str(state[pygame.K_d])
	if w:
		p.ChangeDutyCycle(current_speed)
		dc.forward(forwardpin,backwardpin)
		print "forward"
	elif s:
		p.ChangeDutyCycle(current_speed)
		dc.backward(forwardpin,backwardpin)
		print "backward"
	elif a:
		print "left"
		high.ChangeDutyCycle(75) #added
		dc.turnLeft(leftpin,rightpin)
		pass
	elif d:
		print "right"
		high.ChangeDutyCycle(75) #added
		dc.turnRight(leftpin,rightpin)
		pass
	elif q:
		p.stop()
		high.stop()
		GPIO.cleanup()
		print "exiting"
		sys.exit()
	if (w+s) == 0:
		p.ChangeDutyCycle(0)

	if (a+d) == 0:
		high.ChangeDutyCycle(0)

	if z and (w or s):
		current_speed = snail_speed
		print "slow down"
		print current_speed
	if x and (w or s):
		current_speed = turbo_speed
		print "speed up"
		print current_speed
	if not x and not z:
		current_speed = base_speed




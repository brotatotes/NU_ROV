import pygame, sys
import DC_Motor as dc
import RPi.GPIO as GPIO
pygame.init()

size = width, height = 320,240

screen = pygame.display.set_mode(size)


forwardpin = 11                         #11 high is forward
backwardpin = 13                        #13 low is forward

outpin = 7                              #PWM output pin is GPIO pin 7
frequency = 100	                         #frequency is 100 Hz

current_speed = 0                       #keeps track of the current speed(duty cycle) of the RC car

GPIO.setup(outpin,GPIO.OUT)             #sets up the pin for GPIO output
GPIO.setup(forwardpin,GPIO.OUT)
GPIO.setup(backwardpin,GPIO.OUT)
GPIO.output(forwardpin, 1)              #sets pin to high
GPIO.output(backwardpin,0)

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
		pass
	elif d:
		pass
		print "right"
	elif x:
		if current_speed-10 >=0:
			current_speed-=10
			p.ChangeDutyCycle(current_speed)
		print "slow down"
	elif z:
		if current_speed+10 <=100:
			current_speed+=10
			p.ChangeDutyCycle(current_speed)
		print "speed up"
	elif q:
		p.stop()
		GPIO.cleanup()
		print "exiting"
		sys.exit()

	elif (w+a+s+d) == 0:
		p.ChangeDutyCycle(0)
		print "stop"



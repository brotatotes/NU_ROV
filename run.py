import Tkinter as tk
# import DC_Motor as dc
import DC_Motor as dc
import RPi.GPIO as GPIO
import os
import time

def onKeyPress(event):
	global forwardpin
	global backwardpin
	global p
	global current_speed
	key = event.char
	if key == 'w':
		# text.insert('end', 'You pressed %s\n' % key)
		p.ChangeDutyCycle(current_speed)
		dc.forward(forwardpin,backwardpin)
	elif key == 's':
		p.ChangeDutyCycle(current_speed)
		dc.backward(forwardpin,backwardpin)
	elif key == 'a':
		pass
	elif key == 'd':
		pass
	elif key == ' ':	
		pass
		#current_speed = 0
		#p.ChangeDutyCycle(current_speed)
	elif key == 'z':                #temp speed up key
		if current_speed+10 <=100:
			current_speed+=10
			p.ChangeDutyCycle(current_speed)
	elif key == 'x':                #temp speed down key
		if current_speed-10 >=0:
                	current_speed-=10
                	p.ChangeDutyCycle(current_speed)
	elif key == 'q':
		p.stop()
        	GPIO.cleanup()
        	print "exiting"
		os.system('xset r on')
		quit()

def onKeyRelease(event):
	#if timer == 0:
	print "stopping pwm"
	global p
	#dc.stop(p) 

os.system('xset r off')
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
#p.ChangeDutyCycle(50)                   #starts with 50% duty cycle

root = tk.Tk()
root.geometry('300x200')
text = tk.Text(root, background='black', foreground='white', font=('Comic Sans MS', 12))
text.pack()
button = tk.Button(root,text="W")
button.pack()
root.bind('<KeyPress>', onKeyPress)
root.bind("<KeyRelease>", onKeyRelease)
try:
       root.mainloop() 

except KeyboardInterrupt:
	p.stop()
        GPIO.cleanup()
        print "stopped"

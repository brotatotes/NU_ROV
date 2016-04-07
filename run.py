import Tkinter as tk
# import DC_Motor as dc
import fakedc as dc



def onKeyPress(event):
	key = event.char
	if key == 'w':
		# text.insert('end', 'You pressed %s\n' % key)
		dc.forward()
	elif key == 's':
		dc.backward()
	elif key == 'a':
		pass
	elif key == 'd':
		pass

def onKeyRelease(event):
	#if timer == 0:
	dc.stop() 


root = tk.Tk()
root.geometry('300x200')
text = tk.Text(root, background='black', foreground='white', font=('Comic Sans MS', 12))
text.pack()
button = tk.Button(root,text="W")
button.pack()
root.bind('<KeyPress>', onKeyPress)
root.bind("<KeyRelease>", onKeyRelease)
root.mainloop()
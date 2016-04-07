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
	else:
		dc.stop()

root = tk.Tk()
root.geometry('300x200')
text = tk.Text(root, background='black', foreground='white', font=('Comic Sans MS', 12))
text.pack()
root.bind('<KeyPress>', onKeyPress)
root.mainloop()
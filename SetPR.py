from tkinter import *
from tkinter import messagebox

def isprime(x):
	if x >= 2:
		for y in range(2,x):
			if not (x%y):
				return False
	else:
		return False
	return True

def isroot(y,p):
	a=[]
	for i in range(1,p-1):
		a.append((y**i) % p)
	if len(a) > len(set(a)):
   		return False
	else:
		return True

def setval(Main):


	p=Main.pentry.get()
	r=Main.rentry.get()
	if(len(p) == 0 or len(r) == 0):
		messagebox.showwarning("Inomplete Data", "Enter both Prime and Root!!")
	elif not isprime(int(p)):
		messagebox.showerror("Error", "Non Prime Entered!!")
	elif not isroot(int(r),int(p)):
		messagebox.showerror("Error", "Not a Primitive Root !")
	else:
		Main.status.configure(text=("prime=",p,"root=",r))
		Main.secretinbutton.config(state='active')


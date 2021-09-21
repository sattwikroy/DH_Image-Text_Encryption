from tkinter import *
from tkinter import messagebox
import math

def isprime(x):
	if x >= 2:
		for y in range(2,x):
			if not (x%y):
				return False
	else:
		return False
	return True

def isroot(y,x):

	if y not in x:
   		return False
	else:
		return True

def calroot(p):
	a=[]
	coprimes = {n for n in range(1, p) if math.gcd(n, p) == 1}
	return [g for g in range(1, p) if coprimes == {pow(g, pows, p) for pows in range(1, p)}]

def setP(Main):

	p=Main.pentry.get()
	if(len(p) == 0):
		messagebox.showwarning("Prime Missing","Please enter Prime To Continue")
	elif not isprime(int(p)):
		messagebox.showerror("Error", "Non Prime Entered!!")
	else:
		r=calroot(int(p))
		Main.rentry['values']= r
		Main.status.configure(text=("prime=",p))
		Main.setRbutton.config(state='active',command= lambda: setR(Main,r,p),fg='green',bg='white')
		

def setR(Main,rx,p):

	r=Main.rentry.get()
	if(len(r) == 0):
		messagebox.showwarning("Root Missing", "Please Enter the Root!!")
	elif not isroot(int(r),rx):
		messagebox.showerror("Error", "Not a Primitive Root !")	
	else:
		Main.status.configure(text=("prime=",p,"root=",r))
		Main.secretinbutton.config(state='active')




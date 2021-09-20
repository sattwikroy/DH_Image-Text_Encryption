from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from tkinter.ttk import Progressbar
import time
import math

def getkey(Main):

	u1sec = simpledialog.askstring(title="User 1 Input",prompt= "Enter the secrect number : ",show="*",parent=Main.parent)
	u2sec = simpledialog.askstring(title="User 2 Input",prompt= "Enter the secrect number : ",show="*",parent=Main.parent)
	Main.calcbutton.config(state='active',command=lambda: calkey(Main,int(u1sec),int(u2sec)))

def calkey(Main,u1,u2):
	global p,r
	p=int(Main.pentry.get())
	r=int(Main.rentry.get())
	label4=Label(Main.parent,text="Calculating..........",fg='white',bg='black').grid(row=6,column=6)
	load=Progressbar(Main.parent,orient='horizontal',length=100,mode='determinate')
	load.grid(row=7,column=6)
	for i in range(1,100):
		time.sleep(0.005)
		load["value"]=i
		Main.parent.update()
	u1pub = (r ** u1) % p
	label3=Label(Main.parent,text=("User 1 public key :",u1pub),fg='white',bg='black').grid(row=8,column=5)
	u2pub = (r ** u2) % p
	label4=Label(Main.parent,text=("User 2 public key :",u2pub),fg='white',bg='black').grid(row=8,column=7)
	Main.exhngbutton.config(state='active',command= lambda: exkey(u1,u2,u1pub,u2pub))

def exkey(u1s,u2s,u1p,u2p):

	global p
	user1key = (u2p ** u1s) % p
	user2key = (u1p ** u2s) % p

	if not (user1key == user2key):
		messagebox.showerror("Error", "Keys Don't Match!!")
	else :
		print ("Error key's don't match!!")



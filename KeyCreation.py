from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
import img
import txt
import TextinImage as txtimg
import math


def getkey(Main):

	Main.txtbutton.config(state='disabled')
	Main.imgbutton.config(state='disabled')
	Main.txtimgbutton.config(state='disabled')

	u1sec = simpledialog.askstring(title="User 1 Input",prompt= "Enter the secrect number : ",show="*",parent=Main.parent)
	u2sec = simpledialog.askstring(title="User 2 Input",prompt= "Enter the secrect number : ",show="*",parent=Main.parent)

	if(u1sec==None or u2sec==None):
		messagebox.showwarning("Key Missing", "Enter both Keys")

	elif(u1sec.isdigit() and u2sec.isdigit()):
		global p,r
		p=int(Main.pentry.get())
		r=int(Main.rentry.get())
		u1=int(u1sec)
		u2=int(u2sec)
		u1pub = (r ** u1) % p
		label3=Label(Main.parent,text=("User 1 public key :",u1pub),fg='white',bg='black').grid(row=5,column=3)
		u2pub = (r ** u2) % p
		label4=Label(Main.parent,text=("User 2 public key :",u2pub),fg='white',bg='black').grid(row=5,column=5)
		Main.createbutton.config(state='active',command= lambda: exkey(Main,u1,u2,u1pub,u2pub))
	elif(u1sec=="" or u2sec==""):
		messagebox.showwarning("Key not Entered", "Key was left empty")

	else:
		messagebox.showwarning("Type Error", "Enter numeric Keys")


def exkey(Main,u1s,u2s,u1p,u2p):

	global p
	u1k = (u2p ** u1s) % p
	u2k = (u1p ** u2s) % p

	if not (u1k == u2k):
		messagebox.showerror("Error", "Keys Don't Match!!")
	else :
		label5=Label(Main.parent,text=("Key Creation Sucessful!!"),fg='white',bg='black').grid(row=7,column=4)		
		Main.txtbutton.config(state='active',command=lambda: txt.encrypt(Main,u1k,u2k),fg='black',bg='orange')
		Main.imgbutton.config(state='active',command=lambda: img.encrypt(Main,u1k,u2k),fg='black',bg='purple')
		Main.txtimgbutton.config(state='active',command=lambda: txtimg.encode(Main,u1k,u2k),fg='black',bg='blue')



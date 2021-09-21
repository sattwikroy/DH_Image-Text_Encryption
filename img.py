from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Progressbar
import png
import imageio
import os
import numpy as np


def encrypt(Main,k,k2):

	iload = filedialog.askopenfilename(parent=Main,initialdir=os.getcwd(),title="Please select a file:",filetypes = [("PNG files","*.png")])
	if(iload==()):
		messagebox.showwarning("Image not selected", "Incomplete Operaion")
	elif(iload==""):
		messagebox.showwarning("Image not selected", "Operation Cancelled")
	else:
		im=imageio.imread(iload,format='PNG-FI')
		im = im.astype(np.uint16)
		print("Orinigal Image : ",im)
		im = im.tolist()
		Main.labelen=Label(Main.parent,text=("Encrypting..."),fg='white',bg='black')
		Main.labelen.grid(row=9,column=2,pady=8)
		load=Progressbar(Main.parent,orient='horizontal',maximum=100,length=250,mode='determinate')
		load.grid(row=10,column=2)
		k*=128
		if(k>255):
			k%=250
		print(k,k2)

		for l in range(len(im)):
			for j in range(len(im[l])):

				if(j%5==0):
					a=52*k
					b=-97*k
					c=35*k
				elif(j%3==0):
					a=34*k
					b=67*k
					c=-72*k
				else:
					a=-93*k
					b=22*k
					c=42*k

				im[l][j][0]=im[l][j][0]*k+a
				im[l][j][1]=im[l][j][1]*k+b
				im[l][j][2]=im[l][j][2]*k+c

			y=l%250
			load["value"]=y
			load.update()
		load.grid_remove()

		im=np.array(im).astype(np.uint16)
		print("Encrypted Image : ",im)
		imageio.imwrite("encrypted.png",im,format='PNG-FI')
		Main.decryptbutton=Button(Main.parent,text="Decrypt Image", command=lambda: decrypt(Main,k2),fg='black',bg='white',highlightthickness=0)
		Main.decryptbutton.grid(row=11,column=2,pady=8)
		Main.labelen.configure(text="Ecrypted!",fg='white',bg='black')

def decrypt(Main,k):

	iload = filedialog.askopenfilename(parent=Main,initialdir=os.getcwd(),title="Please select a file:",filetypes = [("PNG files","*.png")])
	if(iload==()):
		messagebox.showwarning("Image Not Selected", "Please try again")
	elif(iload==""):
		messagebox.showwarning("No Image Found", "Try Again")
	else:
		im=imageio.imread(iload,format='PNG-FI')
		print("Original Image : ",im)
		im = im.astype(np.uint16)
		im = im.tolist()
		Main.labelde=Label(Main.parent,text=("Decrypting..."),fg='white',bg='black')
		Main.labelde.grid(row=12,column=2,pady=8)
		load=Progressbar(Main.parent,orient='horizontal',length=250,maximum=100,mode='determinate')
		load.grid(row=13,column=2)
		k*=128
		if(k>255):
			k%=250
		print(k)

		for l in range(len(im)):
			for j in range(len(im[l])):
				
				if(j%5==0):
					a=52*k
					b=-97*k
					c=35*k
				elif(j%3==0):
					a=34*k
					b=67*k
					c=-72*k
				else:
					a=-93*k
					b=22*k
					c=42*k
				
				im[l][j][0]=(im[l][j][0]-a)/k
				im[l][j][1]=(im[l][j][1]-b)/k
				im[l][j][2]=(im[l][j][2]-c)/k

			y=l%250
			load["value"]=y
			Main.parent.update()
	load.grid_remove()
	im=np.array(im).astype(np.uint8)
	print("Decrypted Image : ",im)
	imageio.imwrite("decrypted.png",im,format='PNG-FI')
	Main.labelde.configure(text=("Decrypted!"),fg='white',bg='black')




import PIL.Image
from tkinter import simpledialog
from tkinter import *
import os

def genData(data): 

	newd = []  
	for i in data: 
		newd.append(format(ord(i), '08b')) 
	return newd 

def modPix(pix, data): 

	datalist = genData(data)
	lendata = len(datalist)
	imdata = iter(pix)

	for i in range(lendata): 
		pix = [value for value in imdata.__next__()[:3] + imdata.__next__()[:3] + imdata.__next__()[:3]] 

		for j in range(0, 8): 
			if (datalist[i][j]=='0') and (pix[j]% 2 != 0): 
				if (pix[j]% 2 != 0): 
					pix[j] -= 1
			elif (datalist[i][j] == '1') and (pix[j] % 2 == 0): 
					pix[j] -= 1

		if (i == lendata - 1): 
			if (pix[-1] % 2 == 0): 
				pix[-1] -= 1
		else: 
			if (pix[-1] % 2 != 0): 
				pix[-1] -= 1

		pix = tuple(pix) 
		yield pix[0:3] 
		yield pix[3:6] 
		yield pix[6:9] 



def encode_enc(newimg, data): 

	w = newimg.size[0] 
	(x, y) = (0, 0) 

	for pixel in modPix(newimg.getdata(), data): 
		newimg.putpixel((x, y), pixel) 
		if (x == w - 1): 
			x = 0
			y += 1
		else: 
			x += 1

def encode(Main,k,k2):

	m = simpledialog.askstring(title="Message Input",prompt= "Enter the secrect message : ",show="*",parent=Main.parent)
	if(m==None):
		messagebox.showwarning("No String Entered", "Enter Message to Encrypt")
	elif(m==""):
		messagebox.showwarning("Empty String", "Enter the String to Encrypt")
	else:
		img = filedialog.askopenfilename(parent=Main,initialdir=os.getcwd(),title="Please select a file:",filetypes = (("jpeg files","*.jpg"),("PNG files","*.png"),("all files","*.*")))
		if(img==()):
			messagebox.showwarning("Image not selected", "Incomplete Operation")
		elif(img==""):
			messagebox.showwarning("Image not selected", "Operation Cancelled")
		else:
			image = PIL.Image.open(img, 'r') 
			if (len(m) == 0): 
				raise ValueError('Data is empty') 
			newimg = image.copy()
			en=''
			for i in m :
				en= en + chr(ord(i)+k)
			encode_enc(newimg, en) 
			newimg.save("encoded.png","PNG")
			Main.decodebutton=Button(Main.parent,text="Decode Message From Image", command=lambda: decode(Main,k2),fg='black',bg='white',highlightthickness=0)
			Main.decodebutton.grid(row=13,column=4)


def decode(Main,k):

	img = filedialog.askopenfilename(parent=Main,initialdir=os.getcwd(),title="Please select a file:",filetypes = (("PNG files","*.png"),("jpeg files","*.jpg"),("all files","*.*")))
	if(img==()):
		messagebox.showwarning("Image not selected", "Incomplet Operation")
	elif(img==""):
		messagebox.showwarning("Image not selected", "Operation Cancelled")
	else:
		image = PIL.Image.open(img, 'r') 
		m= '' 
		flag=0
		imgdata = iter(image.getdata()) 
		while (True): 
			pixels = [value for value in imgdata.__next__()[:3] + imgdata.__next__()[:3] + imgdata.__next__()[:3]]
			binstr = ''
			for i in pixels[:8]: 
				if (i % 2 == 0): 
					binstr += '0'
				else: 
					binstr += '1'
			m += chr(int(binstr, 2))
			if (pixels[-1] % 2 != 0):
				de=""
				for i in m :
					de= de + chr(ord(i)-k)
				Main.labelde=Label(Main.parent,text=("Decrypted Text : ",de),fg='white',bg='black').grid(row=14,column=4,pady=8)
				break

from tkinter import filedialog
from tkinter import *
from PIL import Image
import os
import numpy as np

def encrypt(m,k):
	en=np.array([])
	for i in m :
		x= i+k
		en=np.append(en,x)
	en=np.reshape(en,m.shape)
	return en


def decrypt(m,k):
	de=np.array([])
	for i in m :
		x= i-k
		de=np.append(de,x)
	de=np.reshape(de,m.shape)
	return de

A=Tk()

imgload = filedialog.askopenfilename(parent=A,initialdir=os.getcwd(),title="Please select a file:",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
img=Image.open(imgload)
imat=np.asarray(img)
print(imat,"_________________")
enmat=encrypt(imat,1)
print(enmat)
imgen=Image.fromarray(enmat)
imgen.show()
'''imatde=decrypt(imaten,3)
print("Decrypted Image : ",imatde)
imgde= Image.fromarray(imatde, 'RGB')
imgde.show()'''

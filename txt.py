from tkinter import *
def encrypt(Main,k,k2):
	m = simpledialog.askstring(title="Text Input",prompt= "Enter Text to Encrypt : ",parent=Main.parent)
	if(m==None):
		messagebox.showwarning("No String Entered", "Enter Message to Encrypt")
	elif(m==""):
		messagebox.showwarning("Empty String", "Enter the String to Encrypt")
	else:
		en=""
		for i in m :
			en= en + chr((ord(i)*k)+k)

		Main.labelen=Label(Main.parent,text=("Encrypted Text : ",en),fg='white',bg='black').grid(row=9,column=6,pady=8)
		Main.debutton=Button(Main.parent,text="Decrypt",command= lambda: decrypt(Main,en,k2),fg='black',bg='white',highlightthickness=0).grid(row=10,column=6)

def decrypt(Main,m,k):
	de=""
	for i in m :
		de= de + chr((ord(i)-k)//k)
	Main.labelde=Label(Main.parent,text=("Decrypted Text : ",de),fg='white',bg='black').grid(row=11,column=6,pady=8)


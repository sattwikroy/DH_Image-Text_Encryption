from tkinter import *
from tkinter import ttk
import SetPR as Set
import KeyCreation as Key


class MainUI(Frame):

	def __init__(self,parent,*args,**kwargs):
		Frame.__init__(self,parent)
		self.parent=parent

		#Status
		self.status=Label(parent,text="prime= root= ",fg='skyblue',bg='black',relief=RIDGE,anchor=E)
		#Prme & Root Entry
		self.label1=Label(parent,text="prime=",bg='black',fg='crimson',highlightthickness=0).grid(row=2,column=1)
		self.pentry= Entry(parent)
		self.label2=Label(parent,text="root=",bg='black',fg='lime',highlightthickness=0).grid(row=3,column=1)
		self.rentry=ttk.Combobox(parent,values=[])
		#Buttons
		self.setPbutton=Button(parent,text="Set Prime",command= lambda: Set.setP(self),fg='red',bg='white',highlightthickness=0)
		self.setRbutton=Button(parent,text="Set Root",state="disabled",fg='red',bg='grey',highlightthickness=0)
		self.secretinbutton=Button(parent,text="Enter Secret Keys",state='disabled',command= lambda: Key.getkey(self),fg='white',bg='red',highlightthickness=0)
		self.createbutton=Button(parent,text="Create Keys",state='disabled',fg='white',bg='green',highlightthickness=0)
		self.imgbutton=Button(parent,text="Image Encryption",state='disabled',fg='white',bg='black',highlightthickness=0)
		self.txtbutton=Button(parent,text="Text Encryption",state='disabled',fg='white',bg='black',highlightthickness=0)
		self.txtimgbutton=Button(parent,text="Encode Text in Image",state='disabled',fg='white',bg='black',highlightthickness=0)	

		self.status.grid(row=1,column=12)
		self.pentry.grid(row=2,column=2,padx=4)
		self.rentry.grid(row=3,column=2,padx=4)
		self.setPbutton.grid(row=2,column=3,pady=2)
		self.setRbutton.grid(row=3,column=3,pady=2)
		self.secretinbutton.grid(row=4,column=4,pady=4)
		self.createbutton.grid(row=6,column=4,pady=8)
		self.imgbutton.grid(row=8,column=2,pady=8,padx=8)
		self.txtbutton.grid(row=8,column=6,pady=8,padx=8)
		self.txtimgbutton.grid(row=8,column=4,pady=8,padx=8)


main=Tk()
main.minsize(800,500)
main.configure(background='black')
main.title("Encryption & Steganography using DH Algorithm")
MainUI(main).grid()
main.mainloop()

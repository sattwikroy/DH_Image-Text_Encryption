from tkinter import *
import SetPR as Set
import KeyCreation as Key

class MainUI(Frame):

	def __init__(self,parent,*args,**kwargs):
		Frame.__init__(self,parent)
		self.parent=parent
		#Status
		self.status=Label(parent,text="prime= root= ",fg='skyblue',bg='black',relief=RIDGE,anchor=E)
		#Prme & Root Entry
		self.label1=Label(parent,text="prime=",bg='black',fg='crimson',highlightthickness=0).grid(row=3,column=1)
		self.pentry= Entry(parent)
		self.label2=Label(parent,text="root=",bg='black',fg='lime',highlightthickness=0).grid(row=3,column=3)
		self.rentry= Entry(parent)
		#Buttons
		self.setbutton=Button(parent,text="Set",command= lambda: Set.setval(self),fg='red',bg='lime',highlightthickness=0)
		self.secretinbutton=Button(parent,text="Enter Secret Keys",command= lambda: Key.getkey(self),fg='white',bg='red',highlightthickness=0)
		self.calcbutton=Button(parent,text="Calculate Keys",state='disabled',fg='white',bg='blue',highlightthickness=0)
		self.exhngbutton=Button(parent,text="Exchange Keys",state='disabled',fg='white',bg='green',highlightthickness=0)

		self.status.grid(row=2,column=9)
		self.pentry.grid(row=3,column=2,padx=4)
		self.rentry.grid(row=3,column=4,padx=4)
		self.setbutton.grid(row=3,column=5,pady=2)
		self.secretinbutton.grid(row=4,column=6,pady=4)
		self.calcbutton.grid(row=5,column=6,pady=4)
		self.exhngbutton.grid(row=9,column=6,pady=8)


main=Tk()
main.minsize(800,500)
main.configure(background='black')
MainUI(main).grid()
main.mainloop()

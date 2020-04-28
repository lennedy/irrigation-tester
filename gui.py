import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from ComunicationActuator import *
import os
import logging

class PhotoFrame(tk.Frame):
    
	def __init__(self, master, img1, img2, name="my_frame"):

		tk.Frame.__init__(self, master, relief='ridge', bd=2, borderwidth = 0)
		self.updated = False
		self.updatedByGui = False
		self.img1_file= img1
		self.img2_file= img2
		#        self.button_widget()
		self.loadImage()
		self.open = False

	def label_widget(self, s):
		self.title_label = tk.Label(self,text=s)  # Or Frame 1, 2 etc.
		self.title_label.grid(row=0, column=0, columnspan=1, pady=5)

	def loadImage(self, open=False):
		if(open):
			self.img = tk.Label(self, image = self.img1_file)
			self.open = True
		else:
			self.img = tk.Label(self, image = self.img2_file)
			self.open = False
		self.updated = True
#		print(self.updated)
		self.img.grid(row=3, column=2, columnspan=4, pady=5)
		self.img.bind('<Double-1>', self.double_click)

	def button_widget(self):
		self.button = tk.Button(self,text="Open", command = self.updateOpen)
		self.button.grid(row=0, column=2, columnspan=4)
		self.button = tk.Button(self,text="Close", command = self.updateClose)
		self.button.grid(row=2, column=2, columnspan=4)
	
	def pressedButton(self, open=False):
		self.updatedByGui=True
		self.loadImage(open)

	def double_click(self, event):
		self.updatedByGui=True
		if self.open:
			self.loadImage(False)
		else:
			self.loadImage(True)
 

	def updateOpen(self):
		self.loadImage(True)

	def updateClose(self):
		self.loadImage(False)

	def wasItUpdated(self):
		updated=False
		updatedByGui = False

		if (self.updated == True):
			updated=True
		if (self.updatedByGui == True):
			updatedByGui=True
		  
		self.updated=False
		self.updatedByGui = False

		return updatedByGui
    
	def isActive(self):
		return self.open 

	def changeValveState(self, open=False):
		self.loadImage(open)

class RadioFrame(tk.Frame):
	def __init__(self, master, name="my_frame"):
		tk.Frame.__init__(self, master, relief='ridge', bd=2)

		self.automatic = IntVar()
		self.r1 = Radiobutton(self, text="Automático", variable=self.automatic, value=1, command=self.changed)
		self.r2 = Radiobutton(self, text="Manutal", variable=self.automatic, value=0, command=self.changed)
		self.r1.grid(row=1, column=1, columnspan=10)
		self.r2.grid(row=2, column=1, columnspan=1)
		self.itWasUpdated=False

	def isItAutomatic(self):
		return ( self.automatic.get()==1 )

	def changed(self):
		self.itWasUpdated=True

	def wasItUpdated(self):
		itWasUpdated = self.itWasUpdated
		self.itWasUpdated =  False
		return itWasUpdated

	def changeState(self, state=False):
		self.automatic.set((state))

class ButtonFrame(tk.Frame):

	def __init__(self, master, c, name="button_frame"):

		tk.Frame.__init__(self, master, relief='ridge', bd=2)
		self.label_widget(name)
		self.command=c

		self.button = tk.Button(self,text="Open", command = self.updateOpen)
		self.button.grid(row=2, column=2, columnspan=4)
		self.button = tk.Button(self,text="Close", command = self.updateClose)
		self.button.grid(row=4, column=2, columnspan=4)

	def label_widget(self, s):
		self.title_label = tk.Label(self,text=s)  # Or Frame 1, 2 etc.
		self.title_label.grid(row=0, column=2, columnspan=4, pady=5)

	def updateOpen(self):
		self.command(True)

	def updateClose(self):
		self.command(False)

class SetButtonFrame(tk.Frame):

	def __init__(self, master, c1, c2, c3, name="set_buttons"):
		tk.Frame.__init__(self, master, relief='ridge', bd=2)
		self.commad1=c1
		self.commad2=c2
		self.commad3=c3

		self.buttonFrame1 = ButtonFrame(self, c1, name="Valv1")
		self.buttonFrame1.grid(row=0, column=2, columnspan=1)
		self.buttonFrame2 = ButtonFrame(self, c2, name="Valv2")
		self.buttonFrame2.grid(row=0, column=8, columnspan=1)
		self.buttonFrame3 = ButtonFrame(self, c3, name="Valv3")
		self.buttonFrame3.grid(row=0, column=12, columnspan=1)
		self.buttonFrame4 = ButtonFrame(self, self.changeAllStates, name="All Valv")
		self.buttonFrame4.grid(row=0, column=0, columnspan=1)

		self.radioFrame = RadioFrame(self, name)
		self.radioFrame.grid(row=0, column=14)



	def changeAllStates(self, state):
		self.commad1(state)
		self.commad2(state)
		self.commad3(state)

	def isItAutomatic(self):
		return self.radioFrame.isItAutomatic()

	def wasItUpdated(self):
		return self.radioFrame.wasItUpdated()

	def changeRadioState(self, state):
		self.radioFrame.changeState(state);

class ImagesFrame(tk.Frame):

	def __init__(self, master):
		tk.Frame.__init__(self, master, relief='ridge', bd=2)
		image_size=70
		self.img1 = ImageTk.PhotoImage(Image.open("valv_abert.gif").resize((image_size+30, image_size)))
		self.img2 = ImageTk.PhotoImage(Image.open("valv_fechada.gif").resize((image_size+30, image_size)))

		self.imgBomba = ImageTk.PhotoImage(Image.open("bomba2_on.gif").resize((140+30, 140)))
		self.imgBomba2 = ImageTk.PhotoImage(Image.open("bomba2_off.gif").resize((140+30, 140)))

		self.T = ImageTk.PhotoImage(Image.open("T2.gif").resize((140+30, 140)))

		self.f1 = PhotoFrame(self, self.img1, self.img2, "f1")
		self.f1.grid(row=0, column=2)

		self.f2 = PhotoFrame(self, self.img1, self.img2, "f2")
		self.f2.grid(row=1, column=2)

		self.f3 = PhotoFrame(self, self.img1, self.img2, "f3")
		self.f3.grid(row=2, column=2)

		self.f4 = PhotoFrame(self, self.imgBomba2, self.imgBomba, "f4")
		self.f4.grid(row=1, column=0)

		self.f5 = PhotoFrame(self, self.T, self.T, "f5")
		self.f5.grid(row=1, column=1)



	def wasItUpdated(self):
		aFrameWasUpdated=False
		if( self.f1.wasItUpdated() ):
			aFrameWasUpdated=True
		if( self.f2.wasItUpdated() ):
			aFrameWasUpdated=True
		if( self.f3.wasItUpdated() ):
			aFrameWasUpdated=True
		
		return aFrameWasUpdated


class App():

	def __init__(self):
		self.comunication = ComunicationActuator()
		self.root = Tk()
		self.root.title("Simulador de Irrigacao")

		self.imgsFrame = ImagesFrame(self.root)
		self.imgsFrame.pack( side = TOP)

		self.setButton = SetButtonFrame(self.root, self.imgsFrame.f1.pressedButton, self.imgsFrame.f2.pressedButton, self.imgsFrame.f3.pressedButton)
		self.setButton.pack( side = BOTTOM )

		self.comunication.addValv( Valve(pin = -1, name =  "valve1") )
		self.comunication.addValv( Valve(pin = -1, name =  "valve2") )
		self.comunication.addValv( Valve(pin = -1, name =  "valve3") )

	def updateFromServer(self):
		automatic =  self.setButton.isItAutomatic()
		aFrameWasUpdated=False
		if( self.imgsFrame.wasItUpdated() ):
			aFrameWasUpdated=True
		if( self.setButton.wasItUpdated() ):
			aFrameWasUpdated=True


		self.comunication["valve1"] = self.imgsFrame.f1.isActive()
		self.comunication["valve2"] = self.imgsFrame.f2.isActive()
		self.comunication["valve3"] = self.imgsFrame.f3.isActive()
		self.comunication.updateAtomatic(automatic)
		print("Automatico: ",automatic)
		if( aFrameWasUpdated ):
			self.comunication.updateActuatorsInServer()

		self.comunication.getDataInServer()
		##self.comunication.update()

		self.imgsFrame.f1.changeValveState(self.comunication["valve1"])
		self.imgsFrame.f2.changeValveState(self.comunication["valve2"])
		self.imgsFrame.f3.changeValveState(self.comunication["valve3"])
		self.setButton.changeRadioState(self.comunication.getAutomatic())

		self.root.after(1000, self.updateFromServer) 


	def main(self):
		self.updateFromServer()
		self.root.mainloop()


app = App()

app.main()


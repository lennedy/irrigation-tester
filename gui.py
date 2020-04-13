import Tkinter as tk
from Tkinter import *
from PIL import ImageTk, Image
import os

class PhotoFrame(tk.Frame):
    
    def __init__(self, master, img1, img2, name="my_frame"):

        tk.Frame.__init__(self, master, relief='ridge', bd=2)
        self.img1_file= img1
        self.img2_file= img2
#        self.button_widget()
        self.loadImage()
        self.photo_widget()
        self.open = False


    def label_widget(self, s):
        self.title_label = tk.Label(self,text=s)  # Or Frame 1, 2 etc.
        self.title_label.grid(row=0, column=0, columnspan=1, pady=5)

    def loadImage(self, open=False):
        if open:
          self.img = tk.Label(self, image = self.img1_file)
          self.open = True
        else:
          self.img = tk.Label(self, image = self.img2_file)
          self.open = False

        self.img.grid(row=3, column=2, columnspan=4, pady=5)
        self.img.bind('<Double-1>', self.double_click)

    def button_widget(self):
        self.button = tk.Button(self,text="Open", command = self.updateOpen)
	self.button.grid(row=0, column=2, columnspan=4)
        self.button = tk.Button(self,text="Close", command = self.updateClose)
	self.button.grid(row=2, column=2, columnspan=4)

    def double_click(self, event):
        if self.open:
          self.loadImage(False)
        else:
          self.loadImage(True)

    def photo_widget(self):
      print ("hello1")
        # ... Your code here

    def Chk_Val(self):
      print ("hello3")

    def updateOpen(self):
      self.loadImage(True)

    def updateClose(self):
      self.loadImage(False)

    def getFromServer(self):
      print ("Teste1")
      self.after(1000, self.getFromServer) 

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


    def changeAllStates(self, state):
        self.commad1(state)
        self.commad2(state)
        self.commad3(state)


class App():

    def __init__(self):
      self.root = Tk()
      self.root.title("Simulador de Irrigacao")
      image_size=70
      self.img1 = ImageTk.PhotoImage(Image.open("valv_abert.gif").resize((image_size+30, image_size)))
      self.img2 = ImageTk.PhotoImage(Image.open("valv_fechada.gif").resize((image_size+30, image_size)))

      self.f1 = PhotoFrame(self.root, self.img1, self.img2, "f1")
      self.f1.pack( side = TOP )

      self.f2 = PhotoFrame(self.root, self.img1, self.img2, "f2")
      self.f2.pack( side = TOP )

      self.f3 = PhotoFrame(self.root, self.img1, self.img2, "f3")
      self.f3.pack( side = TOP )

      self.setButton = SetButtonFrame(self.root, self.f1.loadImage, self.f2.loadImage, self.f3.loadImage)
      self.setButton.pack( side = BOTTOM )

    def updateFromServer(self):
      print ("Teste0")
      self.root.after(1000, self.updateFromServer) 
	

    def main(self):
	self.updateFromServer()
	self.root.mainloop()



app = App()

app.main()


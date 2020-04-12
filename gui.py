import Tkinter as tk
from Tkinter import *
from PIL import ImageTk, Image
import os

class PhotoFrame(tk.Frame):
    
    def __init__(self, master, img1, img2, name="my_frame"):

        tk.Frame.__init__(self, master, relief='ridge', bd=2)
        self.img1_file= img1
        self.img2_file= img2

#        self.label_widget(name)
        self.button_widget()
        self.loadImage()
        self.photo_widget()


    def label_widget(self, s):
        self.title_label = tk.Label(self,text=s)  # Or Frame 1, 2 etc.
        self.title_label.grid(row=0, column=0, columnspan=1, pady=5)

    def loadImage(self, open=False):
        if open:
          self.img = tk.Label(self, image = self.img1_file)
        else:
          self.img = tk.Label(self, image = self.img2_file)

        self.img.grid(row=3, column=2, columnspan=4, pady=5)

    def button_widget(self):
        self.button = tk.Button(self,text="Open", command = self.updateOpen)
	self.button.grid(row=0, column=2, columnspan=4)
        self.button = tk.Button(self,text="Close", command = self.updateClose)
	self.button.grid(row=2, column=2, columnspan=4)


    def photo_widget(self):
      print ("hello1")
        # ... Your code here


    def Chk_Val(self):
      print ("hello3")
	# ...

    def updateOpen(self):
      self.loadImage(True)

    def updateClose(self):
      self.loadImage(False)

#frame1 = PhotoFrame(master)
#frame1.title_label.configure(text='Frame 1') 

root  = Tk()
root.title("Simulador de Irrigacao")

image_size=70
img1 = ImageTk.PhotoImage(Image.open("valv_abert.gif").resize((image_size+30, image_size)))
img2 = ImageTk.PhotoImage(Image.open("valv_fechada.gif").resize((image_size+30, image_size)))

f1= PhotoFrame(root, img1, img2, "f1")
f1.pack( side = TOP )

f2= PhotoFrame(root, img1, img2, "f2")
f2.pack( side = BOTTOM )

f3= PhotoFrame(root, img1, img2, "f3")
f3.pack( side = BOTTOM )


root.mainloop()






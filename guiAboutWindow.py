from tkinter import *
from PIL import ImageTk,Image

def About():
   
    windowA = Toplevel()
    windowA.title("About")
    windowA.resizable(width=False,height=False)
    
    img =Image.open("My project 6.png")
    bg = ImageTk.PhotoImage(img)

    windowA.geometry("425x490")

    l1 = Label(windowA, image=bg)
    l1.image = img
    l1.place(x = -2,y = 0)

    windowA.mainloop()







    








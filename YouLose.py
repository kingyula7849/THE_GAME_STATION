from tkinter import *
from PIL import ImageTk,Image
    
def YouLose():
    windowYL = Toplevel()
    windowYL.title("The End")
    windowYL.geometry("1080x720")
    windowYL.resizable(False,False)
    
    bg4=PhotoImage(file="YouLose.png")
    l1 = Label(windowYL, image = bg4)
    l1.place(x = -2, y = -1.5)

    def closeYL():
        windowYL.destroy()
        
    b1=Button(windowYL,text="CLOSE",
              font=("Megrim",20),command=closeYL,bg="#Fc6400",
              bd=3,relief = RAISED)
    b1.place(relx=0.45,rely=0.82)
    windowYL.mainloop()



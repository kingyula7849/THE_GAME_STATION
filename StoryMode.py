from tkinter import *
from PIL import ImageTk,Image
import FolderGUI as F
def StoryMode():

    windowSM = Toplevel()
    windowSM.title("Story Mode")
    windowSM.geometry("1080x720")
    windowSM.resizable(False,False)
    bg4=PhotoImage(file="storyline.png")
    l1 = Label(windowSM, image = bg4)
    l1.place(x = -2, y = -1.5)

    def openF():
        windowSM.destroy()
        F.FolderGUI()
          
    Next=Button(windowSM,text="         Next         ",
                font=("Megrim",20),bg="green",bd=5,command=openF)
    Next.place(relx=0.4,rely=0.88)
    
    windowSM.mainloop()





from tkinter import *
from PIL import ImageTk,Image
import StoryMode as SM
import PracticeModeWindow as PMW
import pickle

def PlayWindow():

    windowP = Toplevel()
    windowP.title("Play")
    windowP.geometry("1500x800")

    bg4=PhotoImage(file="My project (17).png")
    l1 = Label(windowP, image = bg4)
    l1.place(x = -65, y = -10)

    bg1=Image.open("storymode.png")
    smbg = ImageTk.PhotoImage(bg1)
    bg2=Image.open("practicemode.png")
    pmbg = ImageTk.PhotoImage(bg2)
    bg3=Image.open("Back.png")
    bbg = ImageTk.PhotoImage(bg3)

    def openStoryMode():
        windowP.destroy()
        SM.StoryMode()
        
    story=Button(windowP,text="Story Mode",image=smbg,bd=5,
                 command=openStoryMode)
    story.place(relx=0.4,rely=0.3)

    def openPracticeMode():
        windowP.destroy()
        PMW.PracticeMode()
        
    practice=Button(windowP,text="Practice Mode",image=pmbg,
                    bd=5,command=openPracticeMode)
    practice.place(relx=0.4,rely=0.52)

    def Back():
        windowP.destroy()
    back=Button(windowP,text="Back",image = bbg, bd=5,
                command=Back)
    back.place(relx=0.4,rely=0.74)


    windowP.mainloop()



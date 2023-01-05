from tkinter import *
from tkinter import ttk
import SnakeTEMP as SGP
import GuiRPS as RPS
import CupGame as CG
import GuessCodeP as GC
from tkinter import messagebox
def PracticeMode():
    windowPM = Toplevel()
    windowPM.title("Practice Mode")
    windowPM.geometry("1080x720")
    windowPM.resizable(False,False)

    bg4=PhotoImage(file="PM.png")
    l1 = Label(windowPM, image = bg4)
    l1.place(x = -2, y = -1.5)

    games=["Space Worm","Cup Game",
           "Guess The Code","Rock Paper Scissors"]

    gameSelected=StringVar() 
    gamescombo=ttk.Combobox(windowPM,width=27,values=games,
                            state="readonly",font=("Megrim",40),
                            textvariable=gameSelected)
    gamescombo.place(relx=0.12,rely=0.42)

    def GameOpen():
        if gameSelected.get() == "Space Worm":
            messagebox.showinfo("CONTROLS","Use 'w' , 'a' , 's' & 'd' to control the Space Worm") 
            windowPM.withdraw()
            SGP.OpenTEMP(windowPM)
            
        elif gameSelected.get() == "Rock Paper Scissors":
            windowPM.withdraw()
            RPS.RPS(windowPM)
        elif gameSelected.get() == "Cup Game":
            CG.CupGame()
        elif gameSelected.get() == "Guess The Code":
            windowPM.destroy()
            GC.GuessCode()
            
    
    openGame=Button(windowPM,text="       OPEN       ",command=GameOpen,
                    font=("Megrim",30),bg="black",fg= "white")
    openGame.place(relx=0.36,rely=0.67)

    def closePM():
        windowPM.destroy()
    back=Button(windowPM,text="       BACK       ",command=closePM,
                    font=("Megrim",30),bg="black",fg= "white")
    back.place(relx=0.36,rely=0.79)
    
    windowPM.mainloop()

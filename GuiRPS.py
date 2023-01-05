from tkinter import *
from tkinter import messagebox
import random

a1=0
b1=0
def RPS(parent):
    windowRPS=Toplevel()
    windowRPS.title("Rock Paper Scissors")
    windowRPS.geometry("1080x720")
    windowRPS.resizable(False,False)
    
    bg4=PhotoImage(file="RPS.png")
    l1 = Label(windowRPS, image = bg4)
    l1.place(x = -2, y = -1.5)

    move={}
    l1={1:"Rock",2:"Paper",3:"Scissors"}
    r = random.randint(1,3)
    move["comp"]=r
    def Rock():
        global a1,b1
        move["player"]=1
        if move["player"] == move["comp"]:
            messagebox.showinfo("I Chose Rock", "Its a tie.    ")
            windowRPS.deiconify()
            r = random.randint(1,3)
            move["comp"]=r
        elif move["comp"] == 2 :
            messagebox.showinfo("I Chose Paper", "you lose.    ")
            windowRPS.deiconify()
            a1+=1
            l2.config(text="LOST - "+str(a1)+"  |  "+"WON - "+str(b1))
            r = random.randint(1,3)
            move["comp"]=r
        elif move["comp"] == 3 :
            messagebox.showinfo("I Chose Scissors", "you win.    ")
            windowRPS.deiconify()
            b1+=1
            l2.config(text="LOST - "+str(a1)+"  |  "+"WON - "+str(b1))
            r = random.randint(1,3)
            move["comp"]=r
    def Paper():
        global a1,b1
        move["player"]=2
        if move["player"] == move["comp"]:
            messagebox.showinfo("I Chose Paper", "Its a tie.    ")
            windowRPS.deiconify()
            r = random.randint(1,3)
            move["comp"]=r
        elif move["comp"] == 3 :
            messagebox.showinfo("I Chose Scissors", "you lose.    ")
            windowRPS.deiconify()
            a1+=1
            l2.config(text="LOST - "+str(a1)+"  |  "+"WON - "+str(b1))
            r = random.randint(1,3)
            move["comp"]=r
        elif move["comp"] == 1 :
            messagebox.showinfo("I Chose Rock", "you win.    ")
            windowRPS.deiconify()
            b1+=1
            l2.config(text="LOST - "+str(a1)+"  |  "+"WON - "+str(b1))
            r = random.randint(1,3)
            move["comp"]=r
    def Scissors():
        global a1,b1
        move["player"]=3
        if move["player"] == move["comp"]:
            messagebox.showinfo("I Chose Scissors", "Its a tie.      ")
            windowRPS.deiconify()
            r = random.randint(1,3)
            move["comp"]=r
        elif move["comp"] == 1 :    
            messagebox.showinfo("I Chose Rock", "you lose.    ")
            windowRPS.deiconify()
            a1+=1
            l2.config(text="LOST - "+str(a1)+"  |  "+"WON - "+str(b1))
            r = random.randint(1,3)
            move["comp"]=r
        elif move["comp"] == 2 :
            messagebox.showinfo("I Chose Paper", "you win.    ")
            windowRPS.deiconify()
            b1+=1
            l2.config(text="LOST - "+str(a1)+"  |  "+"WON - "+str(b1))
            r = random.randint(1,3)
            move["comp"]=r

    p1= PhotoImage(file="rock.png")
    rock=Button(windowRPS,image=p1,command=Rock)
    rock.place(relx=0.06,rely=0.4)

    p2= PhotoImage(file="paper.png")
    paper=Button(windowRPS,image=p2,command=Paper)
    paper.place(relx=0.36,rely=0.4)

    p3= PhotoImage(file="scissor.png")
    scissors=Button(windowRPS,image=p3,command=Scissors)
    scissors.place(relx=0.66,rely=0.4)


    l1=Label(windowRPS,text="Choose your move",
         font=("Megrim",30), bg="black",
         fg="yellow")
    l1.place(relx=0.35,rely=0.3)

    l2=Label(windowRPS,text="Lost - "+str(a1)+"  |  "+"Won -  "+str(b1) ,
         font=("Megrim",30), bg="black",
         fg="yellow")
    l2.place(relx=0.35,rely=0.2)

    rules="""Hello Player. Let's play Rock Paper Scissors.
You know the rules right!
If your move counters my move, you win, or else you lose.
Good Luck."""

    showRules=Text(windowRPS,width=70,height=4,font=("Megrim",16))
    showRules.insert(INSERT,rules)
    showRules.config(state=DISABLED)
    showRules.place(relx=0.1,rely=0.8)

    def closeRPS():
        windowRPS.destroy()
        parent.deiconify()
    close = Button(windowRPS,text='CLOSE',command=closeRPS,
                   font=("Megrim",20),bg='red')
    close.place(relx=0.79,rely=0.225)
    windowRPS.mainloop()



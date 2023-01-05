from tkinter import *
from PIL import ImageTk,Image
import pickle
from tkinter import messagebox

def logout(parent):

    windowLO = Toplevel()
    windowLO.title("NOTICE")
    windowLO.resizable(width=False,height=False)
    
    windowLO.geometry("300x200")

    l1 = Label(windowLO,bg='#000000',width=300,height=200)
    l1.place(x = -1,y = -1)

    warning = Label(windowLO,bg='#FFFFFF',fg='#000000',font =("Megrim", 20,'bold'),
                    text='''ARE YOU SURE YOU
WANT TO LOG OUT?''',width=18)
    warning.place(relx=0.01,rely=0.01)

    yes=Button(windowLO,text='YES',font =("Megrim", 20,'bold'),
               command=lambda:[YES(windowLO,parent)])
    yes.place(relx=0.15,rely=0.55)
    no=Button(windowLO,text=' NO ',font =("Megrim", 20,'bold'),
              command=lambda:[windowLO.destroy()])
    no.place(relx=0.6,rely=0.55)
    
    windowLO.mainloop()

def YES(child,parent):
    action_file = open("action_file.dat",'wb')
    pickle.dump('logout',action_file)
    action_file.close()
    messagebox.showinfo("NOTICE","Refresh the page to Log Out.")
    child.destroy()
    parent.destroy()




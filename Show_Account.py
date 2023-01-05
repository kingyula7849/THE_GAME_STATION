from tkinter import *
from PIL import ImageTk,Image
import mysql.connector as mysc
import pickle
import Account_LogOut as ALO
from tkinter import messagebox

def Show():
    global pwstate
    windowSA = Toplevel()
    windowSA.title("ACCOUNT")
    windowSA.resizable(width=False,height=False)
    
#    img =Image.open("My project 6.png")
#    bg = ImageTk.PhotoImage(img)

    windowSA.geometry("425x490")

    l1 = Label(windowSA,bg='#1D00AE',width=425,height=490)
    l1.place(x = -1,y = -1)

    l2 = Label(windowSA,bg='#181818',width=10,height=1,text='USERNAME',
               font =("Megrim", 20,'bold'),fg='white')
    l2.place(relx=0.05,rely=0.2)
    t1 = Text(windowSA,bg='light blue',width=14,height=1,font = ("classic",20),
              fg = 'black')
    t1.place(relx=0.45,rely=0.2)

    l3 = Label(windowSA,bg='#181818',width=10,height=1,text='PASSWORD',
               font =("Megrim", 20,'bold'),fg='white')
    l3.place(relx=0.05,rely=0.4)
    t2 = Text(windowSA,bg='light blue',width=14,height=1,font = ('classic',20),
              fg='black')
    t2.place(relx=0.45,rely=0.4)
    pwButton = Button(windowSA,text='show',width=10,height=1)
    pwButton.place(relx=0.765,rely=0.475)

    logout = Button(windowSA,text='Log Out',width=15,height=1,
                    font =("Megrim", 15,'bold'),
                    command=lambda:[ALO.logout(windowSA)])
    logout.place(relx=0.3,rely=0.65)
    close = Button(windowSA,text='CLOSE',width=15,height=1,
                   font =("Megrim", 15,'bold'),
                   command=lambda:[windowSA.destroy()])
    close.place(relx=0.3,rely=0.8)

    #creating connection with the server
    con1 = mysc.connect(host='localhost',user='root',passwd='King@mysql7849',
                        database='The_Game_Station')
    crsr = con1.cursor()

    #taking input from action file
    action_file = open('action_file.dat','rb')
    action=pickle.load(action_file)
    action_file.close()

    if action == 'logout':
        messagebox.showinfo("NOTICE","You have Logged Out from your account.")
        windowSA.destroy()
    #importing data of user from the server
    crsr.execute('select * from account_details where Username = "{}"'.format(action[2]))
    details = crsr.fetchall()
    
    #placing data in the textbox
    try:
        t1.insert(END,details[0][0])
        passwd = "******"
        t2.insert(END,passwd)
        t1.config(state=DISABLED)
        t2.config(state=DISABLED)
        pwButton.config(command=lambda:[showPW(t2,pwButton,details[0][1])])
    except:
        z=-1
    
    
    
    windowSA.mainloop()

def showPW(textbox,button,password):
    passwd = "******"
    button.config(command=lambda:[hidePW(textbox,button,password,passwd)])   
    button.config(text='hide')
    textbox.config(state=NORMAL)
    textbox.delete("1.0", "end")
    textbox.insert(END,password)
    textbox.config(state=DISABLED)
def hidePW(textbox,button,password,passwd):
    button.config(command=lambda:[showPW(textbox,button,password)])
    button.config(text='show')
    textbox.config(state=NORMAL)
    textbox.delete("1.0", "end")
    textbox.insert(END,passwd)
    textbox.config(state=DISABLED)

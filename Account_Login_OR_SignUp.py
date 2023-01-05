from tkinter import *
from PIL import Image, ImageTk
import mysql.connector as mysc
import pickle
from tkinter import messagebox

 
def account_Login_or_signup():
    global clickedUN,clickedPW,defUN,defPW,e1,e2
    AccWindow=Tk()
    AccWindow.title("Sign Up / Login")
    AccWindow.geometry("500x500")

    Lbg = Label(AccWindow,bg='#181818',width=500,height=500)
    Lbg.place(x = -1, y = -1)

    clickedUN = False
    clickedPW = False
    
    heading = Label(AccWindow,text='ACCOUNT LOGIN / SIGN UP',font =("Megrim", 24,'bold'),
                    bg="#AF0C15")
    heading.place(relx=0.1,rely=0.07)
    l1=Label(AccWindow,text = "Username: ",font =("Megrim", 14),bg="#AF0C15")
    l1.place(relx=0.17,rely=0.2)
    defUN = StringVar()
    defUN.set('Username length <= 35')
    e1 = Entry(AccWindow,textvariable = defUN,width=30,bg='#1761B0',fg='black',
               state=DISABLED)
    e1.bind('<Button-1>',entryNormalUN)
    e1.place(relx=0.42,rely=0.21)

    l2=Label(AccWindow,text = "Password: ",font =("Megrim", 14),bg="#AF0C15")
    l2.place(relx=0.17,rely=0.3)
    defPW = StringVar()
    defPW.set('Password length <= 30')
    e2 = Entry(AccWindow,textvariable = defPW,width=30,bg='#1761B0',fg='black',
               state=DISABLED)
    e2.bind('<Button-1>',entryNormalPW)
    e2.place(relx=0.42,rely=0.31)

    Lbg.bind('<Button-1>',entryDisabled)

    note = """NOTE: -
    Username must start with a letter(a-z) and must 
    only contain special chareters: '_' & '-'
    Password must be atleast 8 charecters long and
    must contain:
    - 1 Uppercase letter
    - 1 lowercase letter
    - 1 special charecter
    - 1 digit (0-9)"""
    Linfo = Label(AccWindow,text=note,font =("Megrim", 12),bg="#1761B0",fg="black",justify= LEFT)
    Linfo.place(relx =0.1,rely=0.63)

    Lwarn = Label(AccWindow,text='                                                                           ',
                  font =("Megrim", 12),bg="#1761B0",fg="black")
    Lwarn.place(relx=0.1,rely = 0.4)


    try:
        con1 = mysc.connect(host='localhost',user='root',
                            passwd='King@mysql7849',database='The_Game_Station')
        crsr = con1.cursor()

    except:
        con1 = mysc.connect(host='localhost',user='root',
                            passwd='King@mysql7849')
        crsr = con1.cursor()
        crsr.execute('create database The_Game_Station')
        crsr.execute('use The_Game_Station')
        con1.commit()

    def SignUp():
        Username = e1.get()
        UNValid = UserNameCheck()
        Password = e2.get()
        PWValid = PassWordCheck()
        crsr.execute('select Username from account_details where Username = "{}"'.format(Username))
        if crsr.fetchall() != []:
            Lwarn.config(text = '         username already exists! Login instead.           ')
        elif UNValid == False and PWValid == False:
            Lwarn.config(text = '             both input are invalid! try again.              ')
        elif UNValid == False:
            Lwarn.config(text = '              username is invalid! try again.                ')
        elif PWValid == False:
            Lwarn.config(text = '              password is invalid! try again.                ')
        else:
            try:
                crsr.execute('insert into Account_Details values("{}","{}")'.format(Username,Password))
                con1.commit()
                Lwarn.config(text = '              account created for {}                '.format(Username))
                AccWindow.destroy()
                messagebox.showinfo("NOTICE","Refresh the page to Login.")
                action_file = open("action_file.dat",'wb')
                pickle.dump(['pass','login',Username],action_file)
                action_file.close()
            except :
                Lwarn.config(text = '              username already exists! try again.                ')

    def Login():
        Username = e1.get()
        Password = e2.get()
        crsr.execute("select * from account_details where Username = '{}'".format(Username))
        details = crsr.fetchall()
        if details == []:
            Lwarn.config(text = '         username Doesn`t exists! Sign Up instead.           ')
        elif details[0][1] == Password:
            con1.commit()
            Lwarn.config(text = '              Logged In as {}                '.format(Username))
            AccWindow.destroy()
            messagebox.showinfo("NOTICE","Refresh the page to Login.")
            action_file = open("action_file.dat",'wb')
            pickle.dump(['pass','login',Username],action_file)
            action_file.close()
            
        else:
            Lwarn.config(text = '              password is invalid! try again.                ')

    def cancel():
        AccWindow.destroy()
    SIGNUP=Button(AccWindow,text="SIGN UP",bd=4,command=SignUp,bg='#D2292D')
    SIGNUP.place(relx=0.3,rely=0.5)
    LOGIN=Button(AccWindow,text="LOGIN",command=Login,bd=4,bg='#D2292D')
    LOGIN.place(relx=0.45,rely=0.5)
    CANCEL=Button(AccWindow,text="CANCEL",command=cancel,bd=4,bg='#D2292D')
    CANCEL.place(relx=0.6,rely=0.5)
    
    AccWindow.mainloop()

def entryNormalUN(event):
    global clickedUN
    if clickedUN == False or e1.get()=='Username length <= 35':
        clickedUN = True
        defUN.set('')
    e1.config(state=NORMAL)
def entryNormalPW(event):
    global clickedPW
    if clickedPW == False or e2.get()=='Password length <= 30':
        clickedPW = True
        defPW.set('')
    e2.config(state=NORMAL)

def entryDisabled(event):
    if e1.get() == '' or e1.get() == 'Username length <= 35':
        defUN.set('Username length <= 35')
    if e2.get() == '' or e2.get() == 'Password length <= 30':
        defPW.set('Password length <= 30')
    e1.config(state=DISABLED)
    e2.config(state=DISABLED)

def UserNameCheck():
    un = e1.get()
    if un == 'Username length <= 35'or un == '':
        un = '$'
    if un[0].isalpha() == False:
        return False
    if len(un) > 35:
        return False
    for i in un:
        if i.isalnum() == True:
            z=-1
        elif i in '_-':
            z=-1
        else:
            return False
    return True

def PassWordCheck():
    pw = e2.get()
    if pw == 'Password length <= 30':
        pw=''
    tests = {'alpha lower':0,'alpha upper':0,'digits':0,'special chars':0}
    if len(pw) > 30 and len(pw) < 8:
        return False
    for i in pw:
        if i.isalpha() == True:
            if ord(i)>=95 and ord(i) <= 122:
                tests['alpha lower']+=1
            elif ord(i)>=65 and ord(i) <= 90:
                tests['alpha upper']+=1
        elif i.isdigit() == True:
            tests['digits']+=1
        elif i in '`~!@#$%^&*()_+-={}[]|\:;"'",./<>?":
            tests['special chars']+=1
    for i in tests:
        if tests[i] == 0:
            return False
    else:
        return True


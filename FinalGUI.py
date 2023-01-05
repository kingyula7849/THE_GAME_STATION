from tkinter import *
from PIL import Image, ImageTk
import guiAboutWindow as A
import guiReportWindow as Re
import guiRateWindow as Ra
import PlayWindow as P
import Account_Login_OR_SignUp as ALS
import Show_Account as SA
import pickle
import mysql.connector as mysc

def Main_Window():
    
    window=Tk()
    window.title("The Game Station")
    window.geometry("1500x800")


    bg=PhotoImage(file="MyProject4.png")
    l1 = Label(window, image = bg)
    l1.place(x = -2, y = -2)

    photo1= PhotoImage(file="play.png")
    photo2= PhotoImage(file="exit.png")
    photo3= PhotoImage(file="about.png")
    photo4= PhotoImage(file="report.png")
    photo5= PhotoImage(file="rate.png")

    action_file = open("action_file.dat",'wb')
    action_file.close()

    play=Button(window,text="PLAY", image=photo1,bd=5,
                command = lambda:[P.PlayWindow()])
    play.place(relx=0.38,rely=0.5)


    Exit=Button(window,text="EXIT", image=photo2,bd=5,
                command=lambda:window.destroy())
    Exit.place(relx=0.38,rely=0.7)

    rate=Button(window,text="*", image=photo5,bd=3,
                command=lambda:Ra.Rate())
    rate.place(relx=0.93,rely=0.875)


    report=Button(window,text="|^|", image=photo4,bd=3,
                  command=lambda:Re.Report())
    report.place(relx=0.875,rely=0.875)

    about=Button(window,text="?", image=photo3,bd=3,
                 command=lambda:A.About())
    about.place(relx=0.82,rely=0.875)


    AccSL=Button(window,text="SIGN UP / LOGIN",font =("Megrim",12, "bold"),
                 bg='#E2E2E2',width=21,height=2,bd=3,
                 command=lambda:ALS.account_Login_or_signup())
    AccSL.place(relx=0.82,rely=0.75)

    
    LBlabel = Label(window,text='LEADERBOARD',font =("Megrim",24),
                    justify=CENTER,width=18,bg='#e2e2e2')
    LBlabel.place(relx=0.01,rely=0.45)
    mylist = Listbox(window,width=18,height=8,bg='black',fg='#e2e2e2')
    mylist.place(relx=0.01,rely=0.5)
    LeaderBoard = Scrollbar(window,orient=VERTICAL,
                            command = mylist.yview)
    LeaderBoard.place(relx=0.25,rely=0.5,height=284)
    mylist.config(yscrollcommand = LeaderBoard.set,font =("Megrim",24),
                  justify=CENTER)

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

    query='select * from leaderboard order by snake_game_high_score desc'
    crsr.execute(query)

    
    for i in range(10):
        try:
            record = crsr.fetchone()
            mylist.insert(END, record[0]+ ' - ' + record[1])
        except:
            break
    crsr.fetchall()
    

    def refreshLeaderboard():
        con1 = mysc.connect(host='localhost',user='root',
                            passwd='King@mysql7849',database='The_Game_Station')
        crsr = con1.cursor()    
        query='select * from leaderboard order by snake_game_high_score desc'
        crsr.execute(query)
        mylist.delete(0,END)
        for i in range(10):
            try:
                record = crsr.fetchone()
                mylist.insert(END, record[0]+ ' - ' + record[1])
            except:
                break
        crsr.fetchall()

        
    def top5():
        con1 = mysc.connect(host='localhost',user='root',
                            passwd='King@mysql7849',database='The_Game_Station')
        crsr = con1.cursor() 
        query='select * from leaderboard order by snake_game_high_score desc'
        crsr.execute(query)
        mylist.delete(0,END)
        for i in range(5):
            try:
                record = crsr.fetchone()
                mylist.insert(END, record[0]+ ' - ' + record[1])
            except:
                break
        crsr.fetchall()
    TOP5 = Button(window,text="TOP 5",font =("Megrim",12, "bold"),
                      bg='#E2E2E2',width=7,height=1,bd=3,command=top5)
    TOP5.place(relx=0.01,rely=0.883)

    
    def top10():
        con1 = mysc.connect(host='localhost',user='root',
                            passwd='King@mysql7849',database='The_Game_Station')
        crsr = con1.cursor() 
        query='select * from leaderboard order by snake_game_high_score desc'
        crsr.execute(query)
        mylist.delete(0,END)
        for i in range(10):
            try:
                record = crsr.fetchone()
                mylist.insert(END, record[0]+ ' - ' + record[1])
            except:
                break
        crsr.fetchall()
    TOP10 = Button(window,text="TOP 10",font =("Megrim",12, "bold"),
                  bg='#E2E2E2',width=7,height=1,bd=3,command=top10)
    TOP10.place(relx=0.07,rely=0.883)


    def top20():
        con1 = mysc.connect(host='localhost',user='root',
                            passwd='King@mysql7849',database='The_Game_Station')
        crsr = con1.cursor() 
        query='select * from leaderboard order by snake_game_high_score desc'
        crsr.execute(query)
        mylist.delete(0,END)
        for i in range(20):
            try:
                record = crsr.fetchone()
                mylist.insert(END, record[0]+ ' - ' + record[1])
            except:
                break
        crsr.fetchall()            
    TOP20 = Button(window,text="TOP 20",font =("Megrim",12, "bold"),
                  bg='#E2E2E2',width=7,height=1,bd=3,command=top20)
    TOP20.place(relx=0.13,rely=0.883)


    def top50():
        con1 = mysc.connect(host='localhost',user='root',
                            passwd='King@mysql7849',database='The_Game_Station')
        crsr = con1.cursor() 
        query='select * from leaderboard order by snake_game_high_score desc'
        crsr.execute(query)
        mylist.delete(0,END)
        for i in range(50):
            try:
                record = crsr.fetchone()
                mylist.insert(END, record[0]+ ' - ' + record[1])
            except:
                break
        crsr.fetchall()
    TOP50 = Button(window,text="TOP 50",font =("Megrim",12, "bold"),
                  bg='#E2E2E2',width=7,height=1,bd=3,command=top50)
    TOP50.place(relx=0.19,rely=0.883)

    Refresh=Button(window,text="refresh",font =("Megrim",12, "bold"),
                 bg='#E2E2E2',width=21,height=1,bd=3,
                 command=lambda:[read_action(AccSL),refreshLeaderboard()])
    Refresh.place(relx=0.82,rely=0.82)


    window.mainloop()

def read_action(button):
    action_file = open('action_file.dat','rb')
    try:
        action=pickle.load(action_file)
        if action[0] == 'pass':
            button.config(text=action[2],command=lambda:[SA.Show()])
        elif action == 'logout':
            button.config(text="SIGN UP / LOGIN",
                          command=lambda:ALS.account_Login_or_signup())
        else:
            z=-1
    except:
        z=-1
    action_file.close()
    
    


Main_Window()



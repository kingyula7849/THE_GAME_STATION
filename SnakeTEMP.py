from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import SnakeGameP as SGP
import mysql.connector as mysc
import pickle


def OpenTEMP(parent):
    windowTEMP = Toplevel(parent)
    windowTEMP.title("Snake Game")
    windowTEMP.resizable(width=False,height=False)
    windowTEMP.geometry("425x490")

    bglabelTEMP = Label(windowTEMP,width=425,height=490,bg='#414C6B')
    bglabelTEMP.place(x = -1,y = -1)

    player = Label(windowTEMP,width=10,height=2,text='PLAYER: ',
              bg='#1E80C1',font=("Megrim",20),justify=LEFT)
    player.place(relx=0.1,rely=0.05)
    
    playerV = Label(windowTEMP,width=13,height=2,
                  bg='#A5DEF2',font=("Megrim",16),justify=LEFT)
    playerV.place(relx=0.55,rely=0.05)
    
    score = Label(windowTEMP,width=10,height=2,text='SCORE',
              bg='#1E80C1',font=("Megrim",20),justify=LEFT)
    score.place(relx=0.1,rely=0.2)
    
    Hscore = Label(windowTEMP,width=10,height=2,text='HIGH SCORE',
                  bg='#1E80C1',font=("Megrim",20),justify=LEFT)
    Hscore.place(relx=0.1,rely=0.35)
    
    scoreV = Label(windowTEMP,width=10,height=2,text='0',
                  bg='#A5DEF2',font=("Megrim",20),justify=LEFT)
    scoreV.place(relx=0.55,rely=0.2)
    
    HscoreV = Label(windowTEMP,width=10,height=2,text='0',
                  bg='#A5DEF2',font=("Megrim",20),justify=LEFT)
    HscoreV.place(relx=0.55,rely=0.35)


    con1 = mysc.connect(host='localhost',user='root',
                        passwd='King@mysql7849',database='The_Game_Station')
    crsr = con1.cursor()

    action_file = open('action_file.dat','rb')
    try:
        action=pickle.load(action_file)
        if action[0] == 'pass':
            username = action[2]
        elif action == 'logout':
            username = None
        else:
            username = None
    except:
        username = None
    action_file.close()

    if username == None:
        playerV.config(text='NOT LOOGED IN')
    else:
        playerV.config(text=username)
    def playF():
        windowTEMP.withdraw()
        highScore = int(HscoreV.cget("text"))
        scoreData = SGP.openSGP(windowTEMP,highScore)
        scoreV.config(text=str(scoreData[0]))
        HscoreV.config(text=str(scoreData[1]))
        
    play=Button(windowTEMP,text="PLAY",font=("Megrim",20),
                  bg ="#5BAEB7",width=15,command=playF)
    play.place(anchor = CENTER,relx=0.5,rely=0.6)
    
    def closeF():
        if username != None:
            HS=HscoreV.cget("text")
            query = 'select snake_game_high_score from leaderboard where username = "{}"'.format(username)
            crsr.execute(query)
            hsp = crsr.fetchone()
            if hsp == None:
                query = 'insert into leaderboard(Username,snake_game_high_score) values ("{}","{}")'.format(username,HS)
                crsr.execute(query)
                con1.commit()
            elif int(hsp[0]) < int(HS):
                query = 'update leaderboard SET snake_game_high_score = "{}" where username = "{}"'.format(HS,username)
                crsr.execute(query)
                con1.commit()
        windowTEMP.destroy()
        parent.deiconify()
    close=Button(windowTEMP,text="CLOSE",font=("Megrim",20),
                  bg ="#5BAEB7",width=15,command=lambda:[closeF()])
    close.place(anchor = CENTER,relx=0.5,rely=0.8)
    
    windowTEMP.mainloop()


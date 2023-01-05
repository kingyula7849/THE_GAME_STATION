from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pickle
import mysql.connector as mysc
def Rate():
    windowRa=Toplevel()
    windowRa.title("Rate")
    windowRa.geometry("425x490")
    windowRa.resizable(width=False,height=False)
    
    img =Image.open("bg rate.png")
    bg = ImageTk.PhotoImage(img)

    label = Label(windowRa, image=bg)
    label.image = img
    label.place(x = -2,y = -2)

    v1 = DoubleVar()


    def show1():
        a=str(int(v1.get()))
        if a =="1":
            sel = "You Rated = " + a + " Star "
        else:
            sel = "You Rated = " + a + " Stars "
        l1.config(text = sel, font =("Megrim", 14))  
      
  
    rating = Scale( windowRa , variable = v1, 
               from_ = 1, to = 5, 
               orient = HORIZONTAL,bg="purple",
                bd=0,font="Megrim",fg="#ffd700",
                troughcolor ="#C8A2C8")   

    b1 = Button(windowRa, text ="⭐ RATE ⭐", 
                command = show1, 
                bg = "#d522d7",font="megrim") 

    l1 = Label(windowRa,text = "You Rated =            ",
               font =("Megrim", 14))

    rating.place(anchor = CENTER,relx=0.5,rely=0.25)
    b1.place(anchor = CENTER,relx=0.5,rely=0.47)
    l1.place(relx=0.3,rely=0.335)

    l2=Label(windowRa,text = "         Give Your FeedBack         ",
               font =("Megrim", 14),
             bg="violet")
    l2.place(relx=0.17,rely=0.585)
    t1=Text(windowRa,width=35,height=7)
    t1.place(relx=0.17,rely=0.65)

    def Submit():
        #username
        username=None
        action_file = open('action_file.dat','rb')
        try:
            action=pickle.load(action_file)
            if action[0] == 'pass':
                username = action[2]
            else:
                username=None
        except:
            username=None
            
        #ratings
        ratings=rating.get()
        
        #feedback
        feedback = t1.get('1.0',END)
        feedback = feedback[:len(feedback)-1:]

        if username == None:
            messagebox.showinfo("NOTICE",
                                "login to give your feedback.")
            windowRa.deiconify()
        else:
            con1 = mysc.connect(host='localhost',user='root',passwd='King@mysql7849',
                                database='The_Game_Station')
            crsr = con1.cursor()
            rate = 'insert into ratings_and_feedbacks values("{}","{}","{}")'.format(username,ratings,feedback)
            crsr.execute(rate)
            con1.commit()
            windowRa.destroy()
            messagebox.showinfo("NOTICE", "Your Feedback is with us.")
    def Cancel():
        windowRa.destroy()
    submit=Button(windowRa,text="SUBMIT",font=("Megrim",10),
                  bg ="#b71db8",width=15,command=Submit)
    submit.place(anchor = CENTER,relx=0.35,rely=0.945)
    cancel=Button(windowRa,text="CANCEL",font=("Megrim",10),
                  bg ="#b71db8",width=15,command=Cancel)
    cancel.place(anchor = CENTER,relx=0.65,rely=0.945)
    windowRa.mainloop()



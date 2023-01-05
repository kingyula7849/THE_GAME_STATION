from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pickle
import mysql.connector as mysc

def Report():
    windowRe=Toplevel()
    windowRe.title("Report")
    windowRe.geometry("425x490")
    windowRe.resizable(width=False,height=False)

    img =Image.open("bg report.png")
    bg = ImageTk.PhotoImage(img)

    label = Label(windowRe, image=bg)
    label.image = img
    label.place(x = -2,y = -2)
    
    ch=StringVar(windowRe, "1")

    Radiobutton(windowRe,text="Glitch/Bug                               ",value="1",variable=ch,background ="#6441a4",font="Megrim").place(relx=0.2,rely=0.21)
    Radiobutton(windowRe,text="any improvement suggestions  ",
                value="2",variable=ch,background ="#6441a4",
                font="Megrim").place(relx=0.2,rely=0.27)
    Radiobutton(windowRe,text="Saw any Inappropriate Feature",
                value="3",variable=ch,background ="#6441a4",
                font="Megrim").place(relx=0.2,rely=0.33)
    
    l1=Label(windowRe,text="            Explain in Detail           ",bg="#66d8ff",pady=6,font="Megrim")
    l1.place(relx=0.2,rely=0.48)

    txtreport = Text(windowRe,height = 7, width = 30)
    txtreport.place(relx= 0.2,rely =0.56)

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
            
        #issue
        problem=ch.get()
        if problem=='1':
            issue='glitch/bug'
        elif problem=='2':
            issue='improvement suggestions'
        elif problem=='3':
            issue='saw an inappropriate feature'

        #details
        details = txtreport.get('1.0',END)
        details = details[:len(details)-1:]

        if username == None:
            messagebox.showinfo("NOTICE",
                                "login to report your problem.")
            windowRe.deiconify()
        else:
            con1 = mysc.connect(host='localhost',user='root',passwd='King@mysql7849',
                                database='The_Game_Station')
            crsr = con1.cursor()
            report = 'insert into reports_and_bugs values("{}","{}","{}")'.format(username,issue,details)
            crsr.execute(report)
            con1.commit()
            windowRe.destroy()
            messagebox.showinfo("NOTICE","""Thank You for reporting us.
We will try our best to fix the Problem.""")
    def Cancel():
        windowRe.destroy()

    submit=Button(windowRe,text="SUBMIT",font="Megrim",
                  command = Submit,bg="#f86e61",width =15)
    submit.place(relx=0.12,rely=0.85)
    cancel=Button(windowRe,text="CANCEL",font="Megrim",
                  command = Cancel,bg="#f86e61",width =15)
    cancel.place(relx=0.52,rely=0.85)

    windowRe.mainloop()




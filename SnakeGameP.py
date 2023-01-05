from turtle import *
import time
import random

def openSGP(parent,hs):
    try:
        TurtleScreen._RUNNING = True
        delay = 0.1
        bk = 0
        mbk = hs
        
        windowSGP = Screen()
        windowSGP.title("Snake Game")
        windowSGP.setup(width=1080,height=720)
        windowSGP.tracer(0)

        bgpic("snake game bg.png")

        worm = Turtle()
        addshape(name="worm head gif.gif",shape=None)
        addshape(name="body gif.gif",shape=None)
        worm.shape("worm head gif.gif")
        worm.penup()
        worm.goto(0, 0)
        worm.direction = "Stop"
        

        food = Turtle()
        addshape(name="food 1 gif.gif",shape=None)
        addshape(name="food 2 gif.gif",shape=None)
        addshape(name="food 3 gif.gif",shape=None)
        l1=["food 1 gif.gif","food 2 gif.gif","food 3 gif.gif"]
        r1=random.randint(0,2)
        fc=l1[r1]
        food.shape(fc)
        food.speed(0)
        food.penup()
        food.goto(0, 200)

        food2 = Turtle()
        addshape(name="food 1 gif.gif",shape=None)
        addshape(name="food 2 gif.gif",shape=None)
        addshape(name="food 3 gif.gif",shape=None)
        l1=["food 1 gif.gif","food 2 gif.gif","food 3 gif.gif"]
        r1=random.randint(0,2)
        fc=l1[r1]
        food2.shape(fc)
        food2.speed(0)
        food2.penup()
        food2.goto(30, 130)

        food3 = Turtle()
        addshape(name="food 1 gif.gif",shape=None)
        addshape(name="food 2 gif.gif",shape=None)
        addshape(name="food 3 gif.gif",shape=None)
        l1=["food 1 gif.gif","food 2 gif.gif","food 3 gif.gif"]
        r1=random.randint(0,2)
        fc=l1[r1]
        food3.shape(fc)
        food3.speed(0)
        food3.penup()
        food3.goto(-100, -100)
        

        pen = Turtle()
        pen.speed(0)
        pen.shape("square")
        pen.color("white")
        pen.penup()
        pen.hideturtle()
        pen.goto(0, 225)
        pen.write("Bugs Killed : 0  Highest Bugs Killed : {}".format(mbk),
                  align="center",font=("Megrim", 24, "bold"))



        def goup():
            if worm.direction != "dowindowSGP":
                worm.direction = "up"
         
         
        def godowindowSGP():
            if worm.direction != "up":
                worm.direction = "dowindowSGP"
         
         
        def goleft():
            if worm.direction != "right":
                worm.direction = "left"
         
         
        def goright():
            if worm.direction != "left":
                worm.direction = "right"
         
         
        def move():
            if worm.direction == "up":
                y = worm.ycor()
                
                worm.sety(y+20 + bk/50)
            if worm.direction == "dowindowSGP":
                y = worm.ycor()
                worm.sety(y-20 - bk/50)
            if worm.direction == "left":
                x = worm.xcor()
                worm.setx(x-20 - bk/50)
            if worm.direction == "right":
                x = worm.xcor()
                worm.setx(x+20 + bk/50)
         
         
        windowSGP.listen()
        windowSGP.onkeypress(goup, "w")
        windowSGP.onkeypress(godowindowSGP, "s")
        windowSGP.onkeypress(goleft, "a")
        windowSGP.onkeypress(goright, "d")


        s = []

        while True:
            windowSGP.update()
            if worm.xcor() > 510 or worm.xcor() < -520 or worm.ycor() > 340 or worm.ycor() < -330:
                if bk>mbk:
                    mbk=bk
                break
                #pen.write("Bugs Killed : {} Highest Bugs Killed : {} ".format(
                #    bk, mbk), align="center", font=("Megrim", 24, "bold"))
            if worm.distance(food) < 35:
                l1=["food 1 gif.gif","food 2 gif.gif","food 3 gif.gif"]
                r1=random.randint(0,2)
                fc=l1[r1]
                food.shape(fc)
                x = random.randint(-400, 400)
                y = random.randint(-320, 200)
                food.goto(x, y)
         
                body = Turtle()
                body.speed(0)
                body.shape("body gif.gif") 
                body.penup()
                s.append(body)
                delay -= 0.001
                bk += 10
                if bk > mbk:
                    mbk=bk
                pen.clear()
                pen.write("Bugs Killed : {} Highest Bugs Killed : {} ".format(
                    bk, mbk), align="center", font=("Megrim", 24, "bold"))

            if worm.distance(food2) < 35:
                l1=["food 1 gif.gif","food 2 gif.gif","food 3 gif.gif"]
                r1=random.randint(0,2)
                fc=l1[r1]
                food2.shape(fc)
                x = random.randint(-400, 400)
                y = random.randint(-320, 200)
                food2.goto(x, y)
             
                body = Turtle()
                body.speed(0)
                body.shape("body gif.gif") 
                body.penup()
                s.append(body)
                delay -= 0.001
                bk += 15
                if bk > mbk:
                    mbk=bk
                pen.clear()
                pen.write("Bugs Killed : {} Highest Bugs Killed : {} ".format(bk, mbk),
                          align="center", font=("Megrim", 24, "bold"))

            if worm.distance(food3) < 35:
                l1=["food 1 gif.gif","food 2 gif.gif","food 3 gif.gif"]
                r1=random.randint(0,2)
                fc=l1[r1]
                food3.shape(fc)
                x = random.randint(-400, 400)
                y = random.randint(-320, 200)
                food3.goto(x, y)
             
                body = Turtle()
                body.speed(0)
                body.shape("body gif.gif") 
                body.penup()
                s.append(body)
                delay -= 0.001
                bk += 20
                if bk > mbk:
                    mbk=bk
                pen.clear()
                pen.write("Bugs Killed : {} Highest Bugs Killed : {} ".format(bk, mbk),
                          align="center", font=("Megrim", 24, "bold"))    
            
            for index in range(len(s)-1, 0, -1):
                x = s[index-1].xcor()
                y = s[index-1].ycor()
                s[index].goto(x, y)
            if len(s) > 0:
                x = worm.xcor()
                y = worm.ycor()
                s[0].goto(x, y)
            move()
            for i1 in s:
                if i1.distance(worm) < 20:
                    break
                    #pen.write("Bugs Killed : {} Highest Bugs Killed : {} ".format(
                    #    bk, mbk), align="center", font=("Megrim", 24, "bold"))
            time.sleep(delay)
        #windowSGP.exitonclick()
        bye()
        parent.deiconify()
        return [bk,mbk]
    finally:
        Terminator()
    




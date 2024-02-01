import turtle
import math
import random

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Space Invaders")
turtle.shape("square")
turtle.shape("triangle")

score = 0
scpen = turtle.Turtle()
scpen.speed(0)
scpen.color("red")
scpen.penup()
scpen.setposition(-290, 280)
scorestring = "SCORE: %s" % score
scpen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
scpen.hideturtle()

plr = turtle.Turtle()
plr.color('yellow')
plr.shape("triangle")
plr.penup()
plr.speed(0)
plr.setposition(0, -250)
plr.setheading(90)

plrspeed = 25
emcount = 10
ems = []

for i in range(emcount):
    ems.append(turtle.Turtle())

for em in ems:
    em.color("Red")
    em.shape("square")
    em.penup()
    em.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    em.setposition(x, y)
emspeed = 7

blt = turtle.Turtle()
blt.color("white")
blt.shape("triangle")
blt.penup()
blt.speed(5)
blt.setheading(90)
blt.shapesize(0.5, 0.5)
blt.hideturtle()
bltspeed = 50
bltstate = "ready"

def move_left():
    x = plr.xcor()
    x -= plrspeed
    if x < -280:
        x = -280
    plr.setx(x)

def move_right():
    x = plr.xcor()
    x += plrspeed
    if x > 280:
        x = 280
    plr.setx(x)

def fire_blt():
    global bltstate
    if bltstate == "ready":
        bltstate = "fire"
        x = plr.xcor()
        y = plr.ycor() + 10
        blt.setposition(x, y)
        blt.showturtle()

def isCollision_em_blt(t1, t2):
    dst = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if dst < 25:
        return True
    else:
        return False

def isCollision_em_plr(t1, t2):
    dst = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if dst < 30:
        return True
    else:
        return False

turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_blt, "space")
Game_Over = False
missed_ems = 0
while True:
    for em in ems:
        x = em.xcor()
        x += emspeed
        em.setx(x)
        if em.xcor() > 270:
            for e in ems:
                y = e.ycor()
                y -= 40
                e.sety(y)
                if e.ycor() < -285 and Game_Over == False:
                    e.hideturtle()
                    missed_ems += 1
                    if missed_ems == 5:
                        Game_Over = True
                    x = random.randint(-200, 200)
                    y = random.randint(100, 250)
                    e.setposition(x, y)
                    e.showturtle()
            emspeed *= -1
        if em.xcor() < -270:
            for e in ems:
                y = e.ycor()
                y -= 40
                e.sety(y)
                if e.ycor() < -285 and Game_Over == False:
                    e.hideturtle()
                    missed_ems += 1
                    if missed_ems == 5:
                        Game_Over = True
                    x = random.randint(-200, 200)
                    y = random.randint(100, 250)
                    e.setposition(x, y)
                    e.showturtle()
            emspeed*=-1
        if isCollision_em_blt(blt, em):
            blt.hideturtle()
            bltstate = "ready"
            blt.setposition(0, -400)
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            em.setposition(x, y)
            emspeed += 0.5
            score += 10
            scorestring = "Score: %s" % score
            scpen.clear()
            scpen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
        if isCollision_em_plr(plr, em):
            Game_Over = True
        if Game_Over == True:
            plr.hideturtle()
            blt.hideturtle()
            for e in ems:
                e.hideturtle()
            screen.bgcolor("green")
            break
    if bltstate == "fire":
        y = blt.ycor()
        y += bltspeed
        blt.sety(y)
    if blt.ycor() > 275:
        blt.hideturtle()
        bltstate = "ready"
turtle.done()
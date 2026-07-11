import turtle

import time
t = turtle.Turtle()
ts = turtle.Screen()

ts.bgcolor("lightblue")

while True:
    turtle.tracer(0)

    t.shape('classic')
    t.pencolor('lightblue')
    t.fillcolor("gold")
    t.penup()
    t.speed(0)
    t.goto(0,100)
    t.pendown()
    t.pensize(4)
    t.begin_fill()


    t.circle(-100)
    t.end_fill()

    t.fillcolor("silver")
    t.penup()
    t.begin_fill()
    t.goto(93.9, 34.2)
    t.pendown()
    t.goto(200, 50)
    t.goto(76, 64)
    t.goto(93.9, 34.2)
    t.end_fill()

    t.penup()
    t.begin_fill()
    t.goto(-93.9, 34.2)
    t.pendown()
    t.goto(-200, 50)
    t.goto(-76, 64)
    t.goto(-93.9, 34.2)
    t.end_fill()
    t.penup()

    t.color("black")

    t.goto(-100, 0)
    t.pendown()
    t.goto(100, 0)
    t.penup()
    t.goto(-40, -15)
    t.write('I open at the close', ("Lucida Handwriting", 48, "normal"))

    turtle.tracer(0)

    t.hideturtle()
        
    ts.update()


"""t.penup()
t.goto(0,30)
t.pendown()
t.setheading(90)
t.pencolor('YellowGreen')
t.fillcolor('GhostWhite')
t.begin_fill()
t.circle(25)
t.circle(-25)
t.end_fill()
t.penup()
t.goto(-15, 30)
t.dot(20)
t.goto(15, 30)
t.dot(20)
t.goto(35, -20)
t.pencolor('violet')
t.pensize(8)
t.pendown()
t.setheading(-90)
t.circle(-35, 180)"""

t.hideturtle()
turtle.mainloop()
import turtle
t = turtle.Turtle()
ts=t.getscreen()



def draw_smiley(offset):
    ts.tracer(0)
    t.penup()
    t.pencolor('HotPink')
    t.fillcolor('firebrick1')
    t.goto(-100,100)
    t.pendown()
    t.pensize(9)
    t.begin_fill()
    t.goto(100,100)
    t.goto(100,-100)
    t.goto(-100,-100)
    t.goto(-100,100)
    t.end_fill()
    t.penup()
    t.goto(0,30)
    t.pendown()
    t.setheading(90)
    t.pencolor('black')
    t.fillcolor('GhostWhite')
    t.begin_fill()
    t.circle(25)
    t.circle(-25)
    t.end_fill()
    t.penup()
    t.goto(-30+offset, 30)
    t.dot(20)
    t.goto(15+offset, 30)
    t.dot(20)
    t.goto(35, -20)
    t.pencolor('dark red')
    t.pensize(8)
    t.pendown()
    t.setheading(-90)
    t.begin_fill()
    t.circle(-35, 180)
    t.goto(35, -20)
    t.end_fill()

ts.update()

offset=0
def animate_drawing():
    global offset
    if offset ==0:
        offset = 15
    else:
        offset = 0
    draw_smiley(offset)
    ts.ontimer(animate_drawing,500)


animate_drawing()
t.penup()
t.goto(-200,110)
t.write("Hello,My name is Happyman!", font=("Arial", 24, "normal")) 
t.hideturtle()
ts.update()

turtle.mainloop()
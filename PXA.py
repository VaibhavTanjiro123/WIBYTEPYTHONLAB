import turtle

t= turtle.Turtle()
ts=t.getscreen()
t.shape('classic')

def draw_line(x0,y0,x1,y1):
    t.penup()
    t.goto(x0,y0)
    t.pendown()
    t.goto(x1,y1)
def draw_rectangle(x0,y0,len,hgt, clr):
    t.fillcolor(clr)
    t.begin_fill()
    draw_line(x0,y0,x0+len,y0)
    draw_line(x0+len,y0,x0+len,y0+hgt)
    draw_line(x0+len,y0+hgt,x0,y0+hgt)
    draw_line(x0,y0+hgt,x0,y0)
    t.end_fill()
#random line
n_cols=30
x_val=-200
y_val=150
ts.tracer(0)
for kk in range(n_cols):
        if kk<5:
            draw_rectangle(x_val,y_val,15,15,'turquoise')
        elif kk>4 and kk<10:
            draw_rectangle(x_val,y_val,15,15,'magenta')
        elif kk>9 and kk<15:
                draw_rectangle(x_val,y_val,15,15,'gold')
        elif kk>14 and kk<20:
                draw_rectangle(x_val,y_val,15,15,'red')
        elif kk>19 and kk<25:
                draw_rectangle(x_val,y_val,15,15,'green')
        else:
                draw_rectangle(x_val,y_val,15,15,'blue')
        x_val=x_val+15
ts.update()

t.speed(9)
input()
n_rows=20
x_val=-200
y_val=150
n_cols=30
ts.tracer(0)
#artistic? patterns
for jj in range(n_rows):
    for kk in range(n_cols):
        if kk<5:
            draw_rectangle(x_val,y_val,15,15,'turquoise')
        elif kk>4 and kk<10:
            draw_rectangle(x_val,y_val,15,15,'magenta')
        elif kk>9 and kk<15:
                draw_rectangle(x_val,y_val,15,15,'gold')
        elif kk>14 and kk<20:
                draw_rectangle(x_val,y_val,15,15,'red')
        elif kk>19 and kk<25:
                draw_rectangle(x_val,y_val,15,15,'green')
        else:
                draw_rectangle(x_val,y_val,15,15,'blue')

        x_val=x_val+15
    x_val=-200
    y_val=y_val-15

t.hideturtle()
ts.update()
#Mario? I guess
input()
t.clear()
n_rows=19
x_val=-150
y_val=150
n_cols=20
ts.tracer(0)
for kk in range(n_rows):
    if kk==0 or kk==1:
        color_list = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    elif kk==2:
        color_list = [1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1]
    elif kk==3:
        color_list = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1]
    elif kk==4:
        color_list = [1, 1, 1, 1, 1, 1, 3, 3, 3, 4, 4, 5, 4, 1, 1, 1, 1, 1, 1, 1]
    elif kk==5:
        color_list = [1, 1, 1, 1, 1, 3, 4, 3, 4, 4, 4, 5, 4, 4, 4, 1, 1, 1, 1, 1]
    elif kk==6:
        color_list = [1, 1, 1, 1, 1, 3, 4, 3, 3, 4, 4, 4, 5, 4, 4, 4, 1, 1, 1, 1]
    elif kk==7:
        color_list = [1, 1, 1, 1, 1, 1, 3, 4, 4, 4, 4, 5, 5, 5, 5, 1, 1, 1, 1, 1]
    elif kk==8:
        color_list = [1, 1, 1, 1, 1, 1, 1, 4, 4, 4, 4, 4, 4, 1, 1, 1, 1, 1, 1, 1]
    elif kk==9:
        color_list = [1, 1, 1, 1, 1, 1, 2, 2, 6, 2, 2, 6, 2, 2, 1, 1, 1, 1, 1, 1]
    elif kk==10:
        color_list = [1, 1, 1, 1, 1, 2, 2, 2, 6, 2, 2, 6, 2, 2, 2, 1, 1, 1, 1, 1]
    elif kk==11:
        color_list = [1, 1, 1, 1, 2, 2, 2, 2, 6, 6, 6, 6, 2, 2, 2, 2, 1, 1, 1, 1]
    elif kk==12:
        color_list = [1, 1, 1, 1, 4, 4, 2, 6, 4, 6, 6, 4, 6, 2, 4, 4, 1, 1, 1, 1]
    elif kk==13:
        color_list = [1, 1, 1, 1, 4, 4, 4, 6, 6, 6, 6, 6, 6, 4, 4, 4, 1, 1, 1, 1]
    elif kk==14:
        color_list = [1, 1, 1, 1, 4, 4, 6, 6, 6, 6, 6, 6, 6, 6, 4, 4, 1, 1, 1, 1]
    elif kk==15:
        color_list = [1, 1, 1, 1, 1, 1, 6, 6, 6, 1, 1, 6, 6, 6, 1, 1, 1, 1, 1, 1]
    elif kk==16:
        color_list = [1, 1, 1, 1, 1, 3, 3, 3, 1, 1, 1, 1, 3, 3, 3, 1, 1, 1, 1, 1]
    elif kk==17:
        color_list = [1, 1, 1, 1, 3, 3, 3, 3, 1, 1, 1, 1, 3, 3, 3, 3, 1, 1, 1, 1]
    else:
        color_list = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

        
    for jj in range(n_cols):

        if color_list[jj]==1:
            draw_rectangle(x_val, y_val, 15,15, "white")
        elif color_list[jj]==2:
            draw_rectangle(x_val, y_val, 15,15, "red")
        elif color_list[jj]==3:
            draw_rectangle(x_val, y_val, 15,15, "brown")
        elif color_list[jj]==4:
            draw_rectangle(x_val, y_val, 15,15, "gold")
        elif color_list[jj]==5:
            draw_rectangle(x_val, y_val, 15,15, "black")
        else:
            draw_rectangle(x_val, y_val, 15,15, "blue")    
        x_val = x_val + 15
    x_val = -150
    y_val = y_val - 15

t.hideturtle()
ts.update()
ts.mainloop()
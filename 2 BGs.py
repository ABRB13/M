from turtle import *

def left_bgcolor(c):
    showturtle()
    penup()
    w = window_width()
    h = window_height()
    penwidth = 10
    # set a big pen width so the turtle is visible while drawing
    width(penwidth)
    # adjust position so we're inside the window border
    goto(-w/2 + penwidth/2, -h/2+penwidth)
    setheading(90)  # north

    pendown()
    color(c, c)     # set both drawing and fill color to be the same color
    begin_fill()
    forward(h - penwidth)
    right(90)
    forward(w/2 - penwidth)
    right(90)
    forward(h - penwidth)   # could be optimized..
    right(90)
    forward(w/2 - penwidth)
    right(90)
    end_fill()

    penup()
    goto(0,0)  # end by setting the turtle in the middle of the screen 
    width(1)
    color('black', 'white')
    setheading(90)
    mainloop()

screen = Screen()
left_bgcolor('orange')
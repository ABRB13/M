import turtle

screen = turtle.Screen()
turtle.colormode(255)

turtle.speed(0)

for i in range(100):
    turtle.circle(5*i) #circle (radius)
    turtle.circle(-5*i)
    turtle.left(i)
    
    turtle.color(2*i, 2*i, 2*i)
    
turtle.exitonclick()

turtle.mainloop()
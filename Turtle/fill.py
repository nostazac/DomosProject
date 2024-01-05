import turtle

t = turtle.Turtle()

t.shapesize(3,3,3)


t.begin_fill()
t.fd(100)   
t.lt(120)
t.fd(100)
t.pencolor("blue")
t.lt(120)
t.fd(100)

t.end_fill()

turtle.mainloop()
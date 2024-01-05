import turtle

def draw_paintbrush():
    turtle.pensize(5)
    turtle.color("blue")
    turtle.begin_fill()
    turtle.left(45)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(50)
    turtle.end_fill()

def draw_pallete():
    turtle.pensize(5)
    turtle.color("red")
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()
    
turtle.speed(2)
turtle.bgcolor("black")
turtle.title("Image Editor Logo")

draw_paintbrush()

turtle.penup()
turtle.goto(100,0)
turtle.pendown()

draw_pallete()

turtle.hideturtle()

turtle.mainloop()
    
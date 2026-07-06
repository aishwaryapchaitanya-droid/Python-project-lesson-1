import turtle
screen = turtle.Screen()
screen.bgcolor("lightblue")

t = turtle.Turtle()
t.pensize(3)
t.pencolor("blue")
t.fillcolor("yellow")

for i in range (4):
    t.forward(100)
    t.right(90)

t.end_fill()

turtle.done()
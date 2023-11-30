import turtle
import colorsys
turtle.bgcolor("black")
t = turtle.Turtle()
t.hideturtle()
turtle.tracer(50)
n=2
c=10
for i in range(1200):
    p = colorsys.hsv_to_rgb(c, 1, 0.99)
    turtle.pencolor(p)
    c+=0.002
    turtle.circle(-i, n)
    turtle.right(100)
    turtle.circle(i, c)
turtle.done()    
    
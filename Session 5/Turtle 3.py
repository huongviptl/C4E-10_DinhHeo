from turtle import *

speed(5)

def draw_star(x, y, length,colors):
    penup()
    goto(x, y)
    pendown()
    color(colors)
    for i in range(5):
        forward(length)
        right(144)

draw_star(10,20,100, "blue")
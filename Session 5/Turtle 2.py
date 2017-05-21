from turtle import *

speed(-1)

def draw_square(length, colors):
    color(colors)
    for i in range(4):
        forward(length)
        left(90)

for n in range(30):
    draw_square(n * 5, 'red')
    left(17)
    penup()
    forward(n * 2)
    pendown()
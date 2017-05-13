from turtle import *

speed(-1)

colors = ["red", "blue", "brown", "yellow", "grey"]

for n in range (5):
    color (colors[n])
    begin_fill()
    
    for _ in range (2):
        forward (50)
        left(90)
        forward (100)
        left(90)

    forward (50)

    end_fill()

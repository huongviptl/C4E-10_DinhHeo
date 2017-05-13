from turtle import *

speed(-1)

##colors = ["gray", "yellow", "purple", "blue", "red"]
for i in range (3, 8):
    if i == 3:
        color("red")
    elif i == 4:
        color("blue")
    elif i == 5:
        color("purple")
    elif i == 6:
        color("yellow")
    else:
        color("grey")
        
    for n in range(i):
        forward(100)
        left(360/i)

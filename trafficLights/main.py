# import
from turtle import *
from time import sleep

# screen
win = Screen()
win.setup(300,700)
win.title("Traffic Lights")

penup()
goto(0,180) # x=0, y=180
pendown()
pensize(4)

for i in range(2):
    forward(80)
    right(90)
    forward(220)
    right(90)


def redLight():
    penup()
    goto(40, 140)
    fillcolor("red")
    shape("circle")
    shapesize(3)


def yellowLight():
    penup()
    goto(40, 70)
    fillcolor("yellow")
    shape("circle")
    shapesize(3)


def greenLight():
    penup()
    goto(40, 0)
    fillcolor("green")
    shape("circle")
    shapesize(3)

while True:
    greenLight()
    sleep(9)
    yellowLight()
    sleep(3)
    redLight()
    sleep(9)



win.mainloop()
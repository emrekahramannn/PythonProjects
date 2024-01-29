# imports
import turtle
import time
import random

# game information
tail = []
score = 0
maxScore = 0

# Set Screen
win = turtle.Screen()
win.title("Snake Game")
win.setup(600,600)              # (300 - 300) x 2
win.bgcolor("green")
win.tracer(0)

# Objects
# Snake Object (Head)
snake = turtle.Turtle()
snake.speed(0)
snake.shape("circle")
snake.color("black")

# set position of snake
snake.penup()
snake.goto(0,0)
snake.direction = "stop"


# Movement Commands
def move():
    if snake.direction == "up":
        y = snake.ycor()            # move along +y 
        snake.sety(y+20) 

    if snake.direction == "down":
        y = snake.ycor()            # move along -y 
        snake.sety(y-20)

    if snake.direction == "right":
        x = snake.xcor()            # move along +x 
        snake.setx(x+20)

    if snake.direction == "left":
        x = snake.xcor()            # move along -x 
        snake.setx(x-20) 

# Controls of Movement
def goUp():
    if snake.direction != "down":
        snake.direction = "up"

def goDown():
    if snake.direction != "up":
        snake.direction = "down"

def goRight():
    if snake.direction != "left":
        snake.direction = "right"

def goLeft():
    if snake.direction != "right":
        snake.direction = "left"


# keyboard - screen interaction
win.listen() 

# key - function interaction
win.onkeypress(goUp, "Up")
win.onkeypress(goDown, "Down")
win.onkeypress(goRight, "Right")
win.onkeypress(goLeft, "Left")


# Bait Object
bait = turtle.Turtle()
bait.speed(0)
bait.shape("circle")
bait.color("brown")

# First Bait Coordinate
bait.penup()
bait.goto(0,100)



# When Snake Eats Bait -> new bait coordinate, tail length
def Eat():
    if snake.distance(bait) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280) 
        bait.goto(x,y)

        snake_tail = turtle.Turtle()    # snake's tail object
        snake_tail.speed(0)
        snake_tail.shape("circle")
        snake_tail.color("black")
        snake_tail.penup()
        tail.append(snake_tail)

        # when eat bait increase score by 5
        global score
        global maxScore
        score += 5
        if score > maxScore:
            maxScore = score
            win.title(f"Score: {score} Top Score: {maxScore}")

    # movement of snake's tail with head
    length = len(tail)
    for i in range(length-1,0,-1):
            x = tail[i-1].xcor()
            y = tail[i-1].ycor()
            tail[i].goto(x,y)
    if len(tail) > 0:
        x = snake.xcor()
        y = snake.ycor()
        tail[0].goto(x,y)           # first tail part turns into head


def beginnig():
    time.sleep(0.1)
    snake.goto(0,0)
    snake.direction = "stop"

    for t in tail:
        t.goto(1000,1000)
    
    tail.clear()        # when snake crash clear list
    score = 0
    win.title(f"Score: {score} Top Score: {maxScore}")


while True:
    win.update()
    Eat()
    move()
    # check if snake hits walls
    if snake.xcor() > 290 or snake.xcor() < -290 or snake.ycor() > 290 or snake.ycor() < -290:
        beginnig()
    # check if snake hits itself
    for t in tail:
        if t.distance(snake) < 20:
            beginnig()
    time.sleep(0.1)


win.mainloop()
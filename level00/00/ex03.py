import turtle
import random
screen = turtle.Screen()
screen.title("거북이 게임")
screen.bgcolor("white")
player = turtle.Turtle()
player.shape("turtle")
player.color("green")
player.penup()
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(random.randint(-200, 200), random.randint(-200, 200))
def move_up():
    player.setheading(90)
    player.forward(10)
def move_down():
    player.setheading(270)
    player.forward(10)
def move_left():
    player.setheading(180)
    player.forward(10)
def move_right():
    player.setheading(0)
    player.forward(10)
screen.onkeypress(move_up, "Up")
screen.onkeypress(move_down, "Down")
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")
screen.listen()
while True:
    if player.distance(food) < 20:
        food.goto(random.randint(-200, 200), random.randint(-200, 200))
    screen.update()

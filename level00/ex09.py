import turtle
import random

# 화면 설정
screen = turtle.Screen()
screen.title("거북이 게임")
screen.bgcolor("white")

# 거북이 설정
player = turtle.Turtle()
player.shape("turtle")
player.color("green")
player.penup()

# 먹이 설정
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(random.randint(-200, 200), random.randint(-200, 200))

# 거북이 이동 함수 정의
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

# 키보드 이벤트 처리
screen.onkeypress(move_up, "Up")
screen.onkeypress(move_down, "Down")
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")
screen.listen()

# 게임 루프
while True:
    # 거북이와 먹이의 충돌 검사
    if player.distance(food) < 20:
        food.goto(random.randint(-200, 200), random.randint(-200, 200))

    # 화면 갱신
    screen.update()

import turtle
import random

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Bouncing the ball game")
wn.tracer(0)


balls = []

LEFT_WALL = 300
RIGHT_WALL = -300
FLOOR = -300

for _ in range(10):
    balls.append(turtle.Turtle())

for ball in balls:
    ball.shape("circle")
    ball.color("green")
    ball.penup()
    ball.speed(0)
    x = random.randint(-290, 290)
    ball.goto(x, 200)
    ball.dy = 0
    ball.dx = 2

gravity = 1

def check_wall(xcor, ycor):
    if xcor() > LEFT_WALL:
        ball.dx *= -1

    if xcor() < RIGHT_WALL:
        ball.dx *= -1

    if ycor() < FLOOR:
        ball.dy *= -1

while True:
    wn.update()

    for ball in balls:
        ball.dy -= gravity
        ball.sety(ball.ycor() + ball.dy)

        ball.setx(ball.xcor() + ball.dx)




#turtle.mainloop()

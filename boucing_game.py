import turtle
import random

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Bouncing the ball game")
#wn.tracer(0)
turtle.tracer(n=None, delay=None)


balls = []

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

gravity = 0.1

while True:
    wn.update()

    for ball in balls:
        ball.dy -= gravity
        ball.sety(ball.ycor() + ball.dy)

        ball.setx(ball.xcor() + ball.dx)

        # Check for a wall collision
        if ball.xcor() > 300:
            ball.dx *= -1

        if ball.xcor() < -300:
            ball.dx *= -1

        # Check for bounce wall
        if ball.ycor() < - 300:
            ball.dy *= -1


    turtle.mainloop()

#Simple maze game by Dianne Jehee

import turtle
import math
import random

wn = turtle.Screen()
wn.bgcolor("#003B46")
wn.title("A maze game")
wn.setup(700, 700)
wn.tracer(0)

#Maakt een pen
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("#07575B")
        self.shapesize(1.2)
        self.penup()
        self.speed(0)


class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.shapesize(0.5)
        self.color("#66A5AD")
        self.penup()
        self.speed(0)
        self.gold = 0

    def go_up(self):
        move_to_x = self.xcor()
        move_to_y = self.ycor() + 24

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_down(self):
        move_to_x = self.xcor()
        move_to_y = self.ycor() - 24

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_left(self):
        move_to_x = self.xcor() - 24
        move_to_y = self.ycor()


        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_right(self):
        move_to_x = self.xcor() + 24
        move_to_y = self.ycor()


        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def is_collision(self, other):
        a = self.xcor()- other.xcor()
        b = self.ycor()- other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))

        if distance < 5:
            return True
        else:
            return False


class Treasure(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("#C4DFE6")
        self.shapesize(0.5)
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()


class Enemy(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("triangle")
        self.color("#092556")
        self.penup()
        self.speed(0)
        self.gold = 25
        self.goto(x, y)
        self.direction = random.choice(["up", "down", "left", "right"])

    def move(self):
        if self.direction == "up":
            dx = 0
            dy = 24
        elif self.direction == "down":
            dx = 0
            dy = -24
        elif self.direction == "left":
            dx = -24
            dy = 0
        elif self.direction == "right":
            dx = 24
            dy = 0
        else:
            dx = 0
            dy = 0

        if self.is_close(player):
            if player.xcor() < self.xcor():
                self.direction = "left"
            elif player.xcor() > self.xcor():
                self.direction = "right"
            elif player.ycor() < self.ycor():
                self.direction = "down"
            elif player.ycor() > self.ycor():
                self.direction = "up"

        move_to_x = self.xcor() + dx
        move_to_y = self.ycor() + dy

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        else:
            self.direction = random.choice(["up", "down", "left", "right"])

        wn.ontimer(self.move, t=random.randint(100, 300))

    def is_close(self, other):
        a = self.xcor()-other.xcor()
        b = self.ycor()-other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))

        if distance < 75:
            return True
        else:
            return False


    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()

#maakt de level lijst
levels = [""]

#Eerste level
level_1 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXEXXXXX   PXXXXXXXXXXXXX",
"XX XXXXX XXXXXXXX XXXXXXX",
"XX       XXXXXXX  XXXXXXX",
"XXXXXXXX XXXX    XXXXXXXX",
"XXXXXXXX XXXX XXXXXXXXXXX",
"XXXXXXXX XXXX XXXXXX XXXX",
"XX XXXXX XXX  XXXX E   XX",
"XX XXXXX       XXXXXXX XX",
"XX XXXXX XXXX      XXX XX",
"XX XXXXX XXXXXXXX  XXX XX",
"XX XXXXXXXXXXXXXX  XXX XX",
"XX XXXX XXXXXXXXX      XX",
"XX      XXXXXXXXX  XXX XX",
"XXXXXX  XXXXXXXXX  XXX XX",
"XXXXXXX XXXXXXXXX  XXX XX",
"XXXXXXXE           XXX XX",
"XXXXXXXXXX XXXXXXX XXX XX",
"XXXXXXXXXX  XXXXXX XXX XX",
"XXXXXXXXXX         XXX XX",
"XX    XXXX  XXXXXXXXXX XX",
"XX  XXXXXX  XXX     E  XX",
"XX  XXXXXX      XXXXXXXXX",
"XX             TXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
]

treasures = []

enemies = []

#Voegt de maze toe aan maze lijst#
levels.append(level_1)

#Maakt een level setup fucntie
def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level[y][x]
            screen_x = -288 + (x * 24)
            screen_y = 228 - (y * 24)

            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.stamp()
                walls.append((screen_x, screen_y))

            if character == "P":
                player.goto(screen_x, screen_y)

            if character == "T":
                treasures.append(Treasure(screen_x, screen_y))

            if character == "E":
                enemies.append(Enemy(screen_x, screen_y))

pen = Pen()
player = Player()

walls = []

setup_maze(levels[1])


wn.onkey(player.go_left, "Left")
wn.onkey(player.go_right, "Right")
wn.onkey(player.go_up, "Up")
wn.onkey(player.go_down, "Down")
wn.listen()

wn.tracer(0)

for enemy in enemies:
    wn.ontimer(enemy.move, t=250)

while True:
    for treasure in treasures:
        if player.is_collision(treasure):
            player.gold += treasure.gold
            print("Player Gold: {}".format(player.gold))
            print("You won")

            treasure.destroy()
            treasures.remove(treasure)
            wn.done()

    for enemy in enemies:
        if player.is_collision(enemy):
            print ("Oh, no! You died!")
            treasure.destroy()
            treasures.remove(treasure)
            wn.done()
            
    wn.update()



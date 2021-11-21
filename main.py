# Day 20 - Snake game
# https://docs.python.org/3/library/turtle.html
import turtle
from turtle import Screen, Turtle
import time

color_of_segment = ["red", "green", "yellow", "white"]
snake_body = []
step = 20

screen = Screen()

# screen setup
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("MY Snake Game")

turtle.tracer(0)

# TODO 1: Create a snake body
def create_body(color, shape, segments, position, size):
    for no_of_segment in range (0, segments):
        segment = Turtle(shape)
        segment.setpos(position[0] - size*(no_of_segment), position[1] )
        segment.color(color_of_segment[no_of_segment])
        snake_body.append(segment)

        turtle.update()

# TODO 2: Move the snake
def move_snake(heading, x, y):

    pos_previous_segment = snake_body[0].position()
    snake_body[0].setpos(pos_previous_segment[0]+x, pos_previous_segment[1]+y )
    print(snake_body[0].color(), pos_previous_segment, snake_body[0].position())

    for segment in range(1, len(snake_body)):
        turtle.update()
        print(snake_body[segment].color(), pos_previous_segment, snake_body[segment].position())

        snake_body[segment].setpos(pos_previous_segment)

        pos_previous_segment = snake_body[segment].position()


# TODO 3: Control the snake
def move_right():
    move_snake(0,20,0)

def move_up():
    move_snake(90,0,20)

def move_left():
    move_snake(180,-20,0)

def move_dwn():
    move_snake(270,0,-20)


# TODO 4: Detect collision with food
# TODO 5: Create a scoreboard
# TODO 6: Detect collision with wall
# TODO 7: Detect collision with tail

screen.listen()

create_body("white", "square", 3, (0,0), 20)


screen.onkey(key="D", fun=move_right)
screen.onkey(key="A", fun=move_left)
screen.onkey(key="W", fun=move_up)
screen.onkey(key="S", fun=move_dwn)


screen.exitonclick()
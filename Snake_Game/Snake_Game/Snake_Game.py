from turtle import Turtle, Screen
import time
from food import Food
from snake import Snake
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("gray")
screen.title("Luka Shekelashvili's Snake Game")
screen.tracer(0)
screen.listen()

snake1 = Snake()
food = Food()
scoreboard = Scoreboard()

screen.onkey(snake1.up, "Up")
screen.onkey(snake1.down, "Down")
screen.onkey(snake1.left, "Left")
screen.onkey(snake1.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake1.move()
    
    if snake1.segments[0].distance(food) < 15: 
        food.new_dot()
        snake1.expand()
        scoreboard.add_score()
        

    if snake1.segments[0].xcor() > 280 or snake1.segments[0].xcor() < -280 or snake1.segments[0].ycor() > 280 or snake1.segments[0].ycor() < -280:
       scoreboard.reset()
       snake1.reset()
       

    for segment in snake1.segments:
        if segment == snake1.segments[0]:
            pass
        elif snake1.segments[0].distance(segment) < 10:
             scoreboard.reset()
             snake1.reset()

screen.exitonclick()
 
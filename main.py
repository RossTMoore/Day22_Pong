#TODO: Import turtles and classes
from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
from dashes import Net

#TODO: Define screen region and out of bounds
screen = Screen()
screen.tracer(0)
screen.listen()
screen.bgcolor("black")
screen.colormode(255)
screen.setup(width=800, height=600)
screen.title("2-Player Pong")

#TODO: Create paddle for user (controlled) & AI
left_paddle = Paddle(-350, 0)
left_paddle.color(48,105,152)
right_paddle = Paddle(350, 0)
right_paddle.color(255, 212, 59)
screen.onkeypress(right_paddle.move_up, "Up")
screen.onkeypress(right_paddle.move_down, "Down")
screen.onkeypress(left_paddle.move_up, "w")
screen.onkeypress(left_paddle.move_down, "s")

#TODO: Create ball class
ball = Ball()

#TODO: Create scoreboard & center line
scoreboard = Scoreboard()
net = Net()
net.make_net()

#TODO: Start game
game_start = True
while game_start:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with either paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()


    #Detect ball out of bounds
    #Right Paddle misses
    if ball.xcor() > 420:
        ball.reset_position()
        scoreboard.l_point()
    #Left Paddle misses
    if ball.xcor() < -420:
        ball.reset_position()
        scoreboard.r_point()

#-----CODE-END-----
screen.exitonclick()
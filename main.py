from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen=Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong Game")
screen.tracer(0)

r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()
score=Scoreboard()


screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"q")
screen.onkey(l_paddle.go_down,"a")

game_is_on=True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor()>280 or ball.ycor()<-280:
        #needs to bounce when touches the top and bottom of the screem
        ball.bounce_y()
    #detect collision with  both paddle
    if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.bounce_x()

    #to check if ball missed right paddle
    if ball.xcor()>380:
        ball.reset_position()
        score.l_point()
    # to check if ball missed left paddle
    if ball.xcor()<-380:
        ball.reset_position()
        score.r_point()



screen.exitonclick()
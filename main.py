import random
import turtle
import time


from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.title("PONG GAME")
screen.bgcolor('black')

screen.tracer(0)
screen.listen()



l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
scoreboard_l = ScoreBoard((-200, 250))
scoreboard_r = ScoreBoard((200, 250))

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(l_paddle.go_forward, "d")
screen.onkey(l_paddle.go_backward, "a")



screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(r_paddle.go_forward_r, "Left")
screen.onkey(r_paddle.go_backward_r, "Right")


game_is_on = True
while game_is_on:
	# RELOAD ANIMATION MANUALLY AFTER WE PUT OBJECT IN PLACE, UPDATES THE FINAL PICTURE
	time.sleep(0.05) # delaying of code's execution below for 0.5 sec
	screen.update()
	ball.move()

	# Detecting collision with wall
	if ball.ycor() > 280 or ball.ycor() < -280:
		ball.bounce_y()

	# Detecting collision with paddle
	if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
		ball.random_y()
		ball.bounce_x()


	# Detecting when the ball goes out of the bound and add score L_PADDLE
	if ball.xcor() > 380:
		scoreboard_l.increasre_score()
		if scoreboard_l.score == 10:
			scoreboard_l.win()
			scoreboard_l.write(f"LEFT PLAYER WON!", False, align="center", font=('Arial', 32, 'normal'))
			game_is_on = False

		ball.reset_ball()
	# Detecting when the ball goes out of the bound and add score R_PADDLE
	if ball.xcor() < -380:
		scoreboard_r.increasre_score()
		if scoreboard_r.score == 10:
			scoreboard_r.win()
			scoreboard_r.write(f"RIGHT PLAYER WON!", False, align="center", font=('Arial', 32, 'normal'))
			game_is_on = False
		ball.reset_ball()










screen.exitonclick()
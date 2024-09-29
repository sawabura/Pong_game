import random
from turtle import Turtle

class Ball(Turtle):

	def __init__(self):
		super(Ball, self).__init__()
		self.color("white")
		self.shape("circle")
		self.shapesize(stretch_wid=2, stretch_len=2, outline=0)
		self.penup()
		self.x_move = 10
		self.y_move = 10

	def move(self):
		new_x = self.xcor() + self.x_move
		new_y = self.ycor() + self.y_move
		self.goto(new_x, new_y)

	def bounce_y(self):
		self.y_move *= -1

	def random_y(self):
		self.y_move = random.choice([10, -10])

	def random_x(self):
		self.x_move = random.choice([10, -10])


	def bounce_x(self):
		self.x_move *= -1

	def reset_ball(self):
		self.home()
		self.bounce_x()
		self.random_y()
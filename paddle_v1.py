from turtle import Turtle



class Paddle:

	def __init__(self, coord):
		self.cord_position = coord
		self.list_of_paddles = []
		self.create_paddle()



	def create_paddle(self):
		paddle = Turtle(shape='square')
		paddle.shapesize(stretch_wid=5, stretch_len=1, outline=40)
		paddle.color("white")
		paddle.penup()
		paddle.setpos(self.cord_position)
		self.list_of_paddles.append(paddle)


	def go_up(self):
		new_y = self.list_of_paddles[0].ycor() + 20
		self.list_of_paddles[0].goto(self.list_of_paddles[0].xcor(), new_y)
		print(self.list_of_paddles)

	def go_down(self):
		new_y = self.list_of_paddles[0].ycor() - 20
		self.list_of_paddles[0].goto(self.list_of_paddles[0].xcor(), new_y)
		print(self.list_of_paddles)

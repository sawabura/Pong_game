from turtle import Turtle




class Paddle(Turtle):

	def __init__(self, coord):
		super().__init__()
		self.shape("square")
		self.color("purple")
		self.shapesize(stretch_wid=5, stretch_len=1, outline=20)
		self.speed("fastest")
		self.penup()
		self.setpos(coord)

	def go_up(self):
		new_y = self.ycor() + 20
		self.goto(self.xcor(), new_y)

	def go_down(self):
		new_y = self.ycor() - 20
		self.goto(self.xcor(), new_y)

	def go_forward(self):
		self.forward(20)
		if self.xcor() > -300:
			self.undo()

	def go_backward(self):
		self.backward(20)
		if self.xcor() < -360:
			self.undo()

	def go_backward_r(self):

		self.forward(20)
		if self.xcor() > 360:
			self.undo()

	def go_forward_r(self):
		self.backward(20)
		if self.xcor() < 300:
			self.undo()
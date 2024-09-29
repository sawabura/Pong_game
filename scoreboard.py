from turtle import Turtle

class ScoreBoard(Turtle):


	def __init__(self, coords):
		super(ScoreBoard, self).__init__()
		self.score = 0
		self.color("white")
		self.penup()
		self.hideturtle()
		self.goto(coords)
		self.update_score()


	def increasre_score(self):
		self.score += 1
		self.clear()
		self.update_score()

	def update_score(self):
		self.write(f"SCORE {self.score}", False, align="center", font=('Arial', 32, 'normal'))

	def win(self):
		self.home()
		self.clear()


	def gameover(self):
		self.color("white")

		self.write(f"ITS GAMEOVER", False, align="center", font=('Arial', 32, 'normal'))
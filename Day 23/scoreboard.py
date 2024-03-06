from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(-220, 265)
        self.scoreboard()

    def scoreboard(self):
        self.write(f"Score: {self.score}", align="Center", font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="Center", font=FONT)

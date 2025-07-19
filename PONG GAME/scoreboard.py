from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.scoreboard()
        self.scores()


    def scoreboard(self):
        self.goto(0, 280)
        self.write(f"Scoreboard",True,align="center",font=("Arial",12,"bold"))

    def scores(self):
        self.clear()
        self.goto(-60, 210)
        self.write(self.l_score,True,align="left",font=("Arial",30,"normal"))
        self.goto(60, 210)
        self.write(self.r_score,True,align="right",font=("Arial",30,"normal"))

    def l_score_inc(self):
        self.l_score += 1
        self.scores()

    def r_score_inc(self):
        self.r_score += 1
        self.scores()
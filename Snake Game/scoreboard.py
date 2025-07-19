from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt') as f:
         self.high_score = int(f.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.scoreboard()

    def scoreboard(self):
        self.clear()
        self.goto(-80, 280)
        self.write(f"Score: {self.score}",True,align="center",font=("Arial",12,"bold"))
        self.goto(20, 280)
        self.write(f"High Score :{self.high_score}",True,align="center",font=("Arial",12,"bold"))

    #def game_over(self):
    #    self.goto(0, 0)
    #    self.write("Game Over",True,align="center",font=("Arial",12,"bold"))

    def highest_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt','w') as s:
                s.write(str(self.high_score))
        self.score = 0
        self.scoreboard()

    def increase_score(self):
        self.score += 1
        self.scoreboard()


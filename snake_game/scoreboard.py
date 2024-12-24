from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Arial", 24, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score_count = 0
        with open("data.txt", "r") as f:
            self.high_score = int(f.read())
        self.hideturtle()
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.goto(x=0, y=270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score_count} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score_count > self.high_score:
            self.high_score = self.score_count
            with open("data.txt", "w") as file:
                file.write(str(self.score_count))
        self.score_count = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def count(self):
        self.score_count += 1
        self.update_scoreboard()

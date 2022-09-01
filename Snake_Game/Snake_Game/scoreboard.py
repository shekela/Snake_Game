from turtle import Turtle

class Scoreboard(Turtle):
      def __init__(self):
          super().__init__()
          self.score = 0
          self.highscore = 0
          with open("data.txt") as file:
               numb = file.read()
               numstr = ""
               for line in numb:
                   numstr += line
                   if line.strip():
                      self.highscore = int(numstr) 
          self.penup()
          self.color("white")
          self.goto(-290, 270)
          self.hideturtle()
          self.update()

      def update(self):
          self.clear()
          self.write(f"Score: {self.score} High Score: {self.highscore}", align="left", font=("Arial", 20 , "normal"))

      def add_score(self):
          self.score += 1
          self.update()

      def reset(self):
          if self.score > self.highscore:
              self.highscore = self.score
              with open("data.txt", mode="w") as file:
                   file.write(f"{self.highscore}")
          self.score = 0
          self.update()


      #def gameover(self):
      #    self.goto(-70,0)
      #    self.write("GAME OVER", align="left", font=("Arial", 20 , "normal"))
      
          



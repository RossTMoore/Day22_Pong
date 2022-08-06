from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
      super().__init__()
      self.penup()
      self.shape("circle")
      self.color("white")
      self.move_speed = 0.1
      self.x_inc = 10
      self.y_inc = 10

    def move(self):
      new_y = self.ycor() + self.y_inc
      new_x = self.xcor() + self.x_inc
      self.goto(new_x, new_y)

    def move_left(self):
      new_y = self.ycor() - self.y_inc
      new_x = self.xcor() - self.x_inc
      self.goto(new_x, new_y)

    def bounce_y(self):
      self.y_inc *= -1

    def bounce_x(self):
      self.x_inc *= -1
      self.move_speed *= 0.8

    def reset_position(self):
      self.goto(0,0)
      self.move_speed = 0.1
      self.bounce_x()





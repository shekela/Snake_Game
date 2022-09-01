from turtle import Turtle
starting_position = [(0, 0), (-20, 0), (-40, 0)]
moving_distance = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        
    
    def create_snake(self):
        for position in starting_position:
            new_segment = Turtle()
            new_segment.color("black")
            new_segment.penup()
            new_segment.shape("square")
            new_segment.goto(position)
            self.segments.append(new_segment)

    def addsegment(self, position):
        new_segment = Turtle("square")
        new_segment.color("black")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
    

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def expand(self):
        self.addsegment(self.segments[-1].position())

    def move(self):
         for seg_num in range(len(self.segments)-1, 0, -1):
             nex_x = self.segments[seg_num - 1].xcor()
             new_y = self.segments[seg_num - 1].ycor()
             self.segments[seg_num].goto(nex_x, new_y)
         self.segments[0].forward(moving_distance)

    def up(self):
        if self.segments[0].heading() != DOWN:
           self.segments[0].setheading(UP)


    def down(self):
        if self.segments[0].heading() != UP:
           self.segments[0].setheading(DOWN)


    def left(self):
        if self.segments[0].heading() != RIGHT:
           self.segments[0].setheading(LEFT)


    def right(self):
        if self.segments[0].heading() != LEFT:
           self.segments[0].setheading(RIGHT)

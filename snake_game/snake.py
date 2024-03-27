from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:

    def __init__(self):
        self.all_segments = []
        self.create_snake()
        self.head = self.all_segments[0]
        
    def create_snake(self):
        pos_x = 0
        pos_y = 0

        for index in range(0, 3):
            self.add_segment(pos_x, pos_y)
            
    def add_segment(self, pos_x, pos_y):
        segment = Turtle(shape="square")
        segment.color("white")
        segment.penup()
        segment.goto(x=pos_x, y=pos_y)
        pos_x -= 20
        self.all_segments.append(segment)

    def extend(self):
        self.add_segment(self.all_segments[-1].xcor(), self.all_segments[-1].ycor())

    def move(self):
        for seg_num in range(len(self.all_segments) - 1, 0, -1):
            new_x = self.all_segments[seg_num - 1].xcor()
            new_y = self.all_segments[seg_num - 1].ycor()
            self.all_segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for seg in self.all_segments:
            seg.goto(1000, 1000)
        self.all_segments.clear()
        self.create_snake()
        self.head = self.all_segments[0]


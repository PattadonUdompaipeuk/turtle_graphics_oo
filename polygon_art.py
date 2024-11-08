import turtle
import random
class Polygon:
    def __init__(self, num_sides, size, orientation, location, color, border_size):
        self.num_sides = num_sides
        self.size = size
        self.orientation = orientation
        self.location = location
        self.color = color
        self.border_size = border_size

    def draw(self):
        turtle.penup()
        turtle.goto(self.location[0], self.location[1])
        turtle.setheading(self.orientation)
        turtle.color(self.color)
        turtle.pensize(self.border_size)
        turtle.pendown()
        for _ in range(self.num_sides):
            turtle.forward(self.size)
            turtle.left(360 / self.num_sides)
        turtle.penup()

    def move(self):
        pass

class PolygonArt:
    def run(self,choice):
        turtle.speed(0)
        turtle.bgcolor('black')
        turtle.tracer(0)
        turtle.colormode(255)

        if choice == 1:
            for _ in range(30):
                num_sides = 3
                size = random.randint(50, 150)
                orientation = random.randint(0, 90)
                location = [random.randint(-300, 300), random.randint(-200, 200)]
                color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
                border_size = random.randint(1, 10)
                Polygon(num_sides, size, orientation, location, color, border_size).draw()
            turtle.done()

        if choice == 2:
            for _ in range(30):
                num_sides = 4
                size = random.randint(50, 150)
                orientation = random.randint(0, 90)
                location = [random.randint(-300, 300), random.randint(-200, 200)]
                color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
                border_size = random.randint(1, 10)
                Polygon(num_sides, size, orientation, location, color, border_size).draw()
            turtle.done()

        if choice == 3:
            for _ in range(30):
                num_sides = 5
                size = random.randint(50, 150)
                orientation = random.randint(0, 90)
                location = [random.randint(-300, 300), random.randint(-200, 200)]
                color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
                border_size = random.randint(1, 10)
                Polygon(num_sides, size, orientation, location, color, border_size).draw()
            turtle.done()

        if choice == 4:
            for _ in range(30):
                num_sides = random.randint(3, 5)
                size = random.randint(50, 150)
                orientation = random.randint(0, 90)
                location = [random.randint(-300, 300), random.randint(-200, 200)]
                color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
                border_size = random.randint(1, 10)
                Polygon(num_sides, size, orientation, location, color, border_size).draw()
            turtle.done()

        if choice == 5:
            for _ in range(30):
                num_sides = 3
                size = random.randint(50, 150)
                orientation = random.randint(0, 90)
                location = [random.randint(-300, 300), random.randint(-200, 200)]
                color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
                border_size = random.randint(1, 10)
                Polygon(num_sides, size, orientation, location, color, border_size).draw()
                EmbeddedPolygon(3,num_sides, size, orientation, location, color, border_size).draw()
            turtle.done()

        if choice == 6:
            for _ in range(30):
                num_sides = 4
                size = random.randint(50, 150)
                orientation = random.randint(0, 90)
                location = [random.randint(-300, 300), random.randint(-200, 200)]
                color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
                border_size = random.randint(1, 10)
                Polygon(num_sides, size, orientation, location, color, border_size).draw()
                EmbeddedPolygon(3,num_sides, size, orientation, location, color, border_size).draw()
            turtle.done()

        if choice == 7:
            for _ in range(30):
                num_sides = 5
                size = random.randint(50, 150)
                orientation = random.randint(0, 90)
                location = [random.randint(-300, 300), random.randint(-200, 200)]
                color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
                border_size = random.randint(1, 10)
                Polygon(num_sides, size, orientation, location, color, border_size).draw()
                EmbeddedPolygon(3,num_sides, size, orientation, location, color, border_size).draw()
            turtle.done()

        if choice == 8:
            for _ in range(30):
                num_sides = random.randint(3, 5)
                size = random.randint(50, 150)
                orientation = random.randint(0, 90)
                location = [random.randint(-300, 300), random.randint(-200, 200)]
                color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
                border_size = random.randint(1, 10)
                Polygon(num_sides, size, orientation, location, color, border_size).draw()
                EmbeddedPolygon(3,num_sides, size, orientation, location, color, border_size).draw()
            turtle.done()

        if choice == 9:
            for _ in range(30):
                num_sides = random.randint(3, 5)
                size = random.randint(50, 150)
                orientation = random.randint(0, 90)
                location = [random.randint(-300, 300), random.randint(-200, 200)]
                color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
                border_size = random.randint(1, 10)
                Polygon(num_sides, size, orientation, location, color, border_size).draw()
                num_levels = random.randint(1, 4)
                EmbeddedPolygon(num_levels, num_sides, size, orientation, location, color, border_size).draw()
            turtle.done()

class EmbeddedPolygon(Polygon):
    def __init__(self, num_levels, num_sides, size, orientation, location, color, border_size, reduction_ratio=0.618):
        super().__init__(num_sides, size, orientation, location, color, border_size)
        self.num_levels = num_levels
        self.reduction_ratio = reduction_ratio

    def draw(self):
        for _ in range(self.num_levels):
            super().draw()
            turtle.penup()
            turtle.forward(self.size*(1-self.reduction_ratio)/2)
            turtle.left(90)
            turtle.forward(self.size*(1-self.reduction_ratio)/2)
            turtle.right(90)
            self.size *= self.reduction_ratio
            self.location[0] = turtle.pos()[0]
            self.location[1] = turtle.pos()[1]

art = PolygonArt()
art.run(random.randint(1, 9))





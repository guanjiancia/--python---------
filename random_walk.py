from random import choice
from random import randint
import pygal

'''class RandomWalk():
    def __init__(self,num_points=50):
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]
    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            x_direction = choice([-1,1])
            x_distance = choice([1,2,3,4])
            x_step = x_direction * x_distance
            y_direction = choice([-1,1])
            y_distance = choice([1,2,3,4])
            y_step = y_direction * y_distance
            if x_step == 0 and y_step == 0:
                continue
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step
            self.x_values.append(next_x)
            self.y_values.append(next_y)'''

class Die():
    def __init__(self,num_sides=6):
        self.num_sides = num_sides
    def roll(self):
        return randint(1,self.num_sides)
die = Die()
numbers = []
for number in range(1000):
    result = die.roll()
    numbers.append(result)
print(numbers)
count = []
for values in range(1,die.num_sides+1):
    counts = numbers.count(values)
    count.append(counts)
print(count)

hist = pygal.Bar()
hist.title = ("谢谢")
hist.x_labels = [1,2,3,4,5,6]
hist.x_title = ("x")
hist.y_title = ("y")
hist.add('D6',count)
hist.render_to_file("a.svg")













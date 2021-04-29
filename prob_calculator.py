import copy
import random
import re

class Hat:
    def __init__(self, **balls):
        self.contents = []
        for k, v in balls.items():
            for x in range(v):
                self.contents.append(k)

    def draw(self, n):
        if n > len(self.contents):
            return self.contents
        drawn_balls = []
        for i in range(n):
            removed = self.contents.pop(int(random.random() * len(self.contents)))
            drawn_balls.append(removed)
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    print(copy.deepcopy(hat))
    num_experiments *=10
    for x in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        balls = hat_copy.draw(num_balls_drawn)
        inner_count = 0
        for k,v in expected_balls.items():
            if balls.count(k) >= v:
                inner_count += 1
            if inner_count == len(expected_balls):
                count += 1
    return count / num_experiments


    


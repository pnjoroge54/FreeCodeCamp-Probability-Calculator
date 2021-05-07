import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for k, v in kwargs.items():
            for rep in range(v): 
                self.contents.append(k)
            
    def draw(self, number):
        drawn = []
        
        if number > len(self.contents):
            return self.contents
        
        for i in range(number):
            # Remove random element from list
            curr = self.contents.pop(random.randrange(len(self.contents)))
            drawn.append(curr)
            
        return drawn
                    
        
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    for i in range(num_experiments):
        expected_c = copy.deepcopy(expected_balls)
        hat_c = copy.deepcopy(hat)
        drawn = hat_c.draw(num_balls_drawn)
        for color in drawn:
            if color in expected_c:
                expected_c[color] -= 1
                
        if all(x <= 0 for x in expected_c.values()):
            count += 1
            
    return count / num_experiments
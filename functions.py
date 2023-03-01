import random

num_dice = 1

def roll():
    value = [1,2,3,4,5,6]
    result = []
    for x in range(num_dice):
        result.append(random.choice(value))
    return result

def config(number=1):
    global num_dice
    num_dice = int(number)


    

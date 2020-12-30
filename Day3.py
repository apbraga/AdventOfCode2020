import numpy as np

def traverse(down, right):
    file = open('day3_input.txt', 'r')
    data = [x.strip() for x in file.readlines()]
    x=0
    y=0
    tree = '#'
    trees = 0
    while(y < len(data)):
        if data[y][x] == tree:
            trees += 1
        y += down
        x = (x+right)%len(data[0])
    return trees

# print number of trees in the way
print(traverse(1, 1)*traverse(1, 3)*traverse(1, 5)*traverse(1, 7)*traverse(2, 1))

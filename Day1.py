import numpy as np

with open("day1_input.txt", "r", encoding="utf-8") as g:
    data = list(map(int, g.readlines()))

data = np.array(data)
remainder = 2020 - data

for x in data:
    if x in remainder:
        multiply = x * (2020-x)
        print(multiply)
        break

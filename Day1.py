import numpy as np
# bring in input data
with open("day1_input.txt", "r", encoding="utf-8") as g:
    data = list(map(int, g.readlines()))
data = np.array(data)
# set number of numbers to sum
param = 3

data = np.sort(data)
data[0]
# a + b + c = 2020
# a * b * c = ???

# PART 2
for i in range(len(data)):
    for j in range(len(data)):
        if(2020 - data[i] - data[j] in data):
            multiply = data[i] * data[j] * (2020 - data[i] - data[j])
            print(multiply)
            break

#PART 1
#remainder = 2020 - data
#for x in data:
#    if x in remainder:
#        multiply = x * (2020-x)
#        print(multiply)
#        break

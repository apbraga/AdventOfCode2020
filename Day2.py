import numpy as np
file = open('day2_input.txt', 'r')
count = 0
while True:
    line = file.readline()
    if not line:
        break
    split = line.split('-')
    min = int(split[0])-1
    split = split[1].split(' ')
    max = int(split[0])-1
    letter = split[1][0]
    pw = split[2]

    if (pw[min]==letter) ^ (pw[max]==letter):
        count += 1

print(count)

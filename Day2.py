import numpy as np
file = open('day2_input.txt', 'r')
count = 0
while True:
    line = file.readline()
    if not line:
        break
    split = line.split('-')
    min = int(split[0])
    split = split[1].split(' ')
    max = int(split[0])
    letter = split[1][0]
    pw = split[2]
    check = len(pw.split(letter))-1

    if (check >= min) and (check <= max):
        count += 1

print(count)

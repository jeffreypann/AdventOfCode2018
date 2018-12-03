import re
import numpy as np

with open("day3_data.txt") as f:
    data = f.readlines()  # turn lines into array
claims = map(lambda s: map(int, re.findall(r'-?\d+', s)), data)
fab = np.zeros((1000,1000))

for claim, x, y, dx, dy in claims:
    fab[x:x+dx,y:y+dy] += 1
print(np.sum(fab>1))

for claim, x, y, dx, dy in claims: # part 2
    if np.all(fab[x:x+dx,y:y+dy] == 1):
        print(claim)

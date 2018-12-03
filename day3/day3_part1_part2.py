import re
import numpy as np

with open("day3_data.txt") as f:
    data = f.readlines()  # turn lines into array
claims = map(lambda s: map(int, re.findall(r'-?\d+', s)), data)
count = 0
fab = np.zeros((1000,1000))
test = np.zeros((5,5))
for claim, x, y, dx, dy in claims:
    fab[x:x+dx,y:y+dy] += 1
print(np.sum(fab>1))

for claim, x, y, dx, dy in claims: # part 2
    if np.all(fab[x:x+dx,y:y+dy] == 2):
        print(claim)

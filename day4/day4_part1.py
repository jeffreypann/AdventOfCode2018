import numpy as np

lines = open('day4_data.txt').read().split('\n')
lines.sort()

def parseTime(line):
    words = line.split()
    date, time = words[0][1:], words[1][:-1]
    return int(time.split(':')[1])


def getID(line):
    words = line.split()
    ID = words[3][1:]
    return int(ID)


count = 0
seen = {}
id = getID(lines[0])
maxcount = 0
maxguy = 0
for i in range(1,len(lines)):
    print(lines[i])
    if len(lines[i]) == 27:
        count += parseTime(lines[i])
        print(count)
    elif len(lines[i]) == 31:
        count += -1*parseTime(lines[i])
        print(count)
    else:
        if id in seen.keys():
            seen[id] += count
        else:
            seen[id] = count
        if seen[id] > maxcount:
            maxguy = id
            maxcount = seen[id]
        count = 0
        id = getID(lines[i])
if seen[id] > maxcount:
    maxguy = id
    maxcount = seen[id]

minutes = np.zeros(60)
user = False
for i in range(0,len(lines)):
    if len(lines[i]) == 27 and user:
        left = parseTime(lines[i-1])
        right = parseTime(lines[i])
        minutes[left:right] += 1
    elif len(lines[i]) != 31 and len(lines[i]) != 27:
        if getID(lines[i]) == maxguy:
            user = True
        else:
            user = False
print(np.argmax(minutes)*maxguy)
print(maxguy)



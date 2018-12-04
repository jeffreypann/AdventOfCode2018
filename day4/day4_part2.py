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


minutes = np.zeros((4000, 60))

count = 0
seen = {}
id = getID(lines[0])
for i in range(0, len(lines)):
    if len(lines[i]) == 27:
        left = parseTime(lines[i - 1])
        right = parseTime(lines[i])
        minutes[id][left:right] += 1
    elif len(lines[i]) != 31:
        id = getID(lines[i])
print((np.argmax(minutes)//60) * (np.argmax(minutes)%60))
print(np.argmax(minutes)%60)


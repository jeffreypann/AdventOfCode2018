from collections import Counter

with open("day2_data.txt") as f:
    data = f.readlines() #turn lines into array
data = [x.strip() for x in data] #take out whitespace
threes = twos = twoSeen = threeSeen = 0
for id in data:
    letters = Counter(id)
    twoSeen = 0
    threeSeen = 0
    for letter in letters:
        if letters[letter] == 2 and twoSeen == 0:
            twos += 1
            twoSeen = 1
        if letters[letter] == 3 and threeSeen == 0:
            threes += 1
            threeSeen = 1
print(twos*threes)


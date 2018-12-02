from collections import Counter

with open("day2_data.txt") as f:
    data = f.readlines()  # turn lines into array
data = [x.strip() for x in data]  # take out whitespace
for word1 in data:
    for word2 in data:
        diff = 0
        i = 0
        j = 0
        if word1 == word2:
            pass
        else:
            while i < len(word1) and j < len(word1) and diff < 2:
                if word1[i] == word2[j]:
                    pass
                else:
                    diff += 1
                i += 1
                j += 1
            if diff == 1:
                for i in range(0,len(word1)):
                    if word1[i] != word2[i]:
                        print((word1[:i] + word2[i+1:]))
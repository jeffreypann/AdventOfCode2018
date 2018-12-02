with open("day1_part1_data.txt") as f:
    data = f.readlines() #turn lines into array
data = [x.strip() for x in data] #take out whitespace
freq = 0
for num in data:
    num_to_add = 1
    if num[0] == "-":
        num_to_add=-1
    num_to_add *= int(num[1:])
    freq += num_to_add
print(freq)
################# part 1 ###############

input = open('input.txt').read().strip()

col1 = []
col2 = []
sum = 0

for line in input.splitlines() :
    col1.append(int(line.split()[0]))
    col2.append(int(line.split()[1]))

col1.sort()
col2.sort()

for i in range(len(col1)) :
    sum = sum + abs(col1[i] - col2[i])

print(sum)


################# part 2 ###############

sim_score = 0
for i in range(len(col1)) :
    sim_score = sim_score + (col1[i] * len([num for num in col2 if num == col1[i]]))

print(sim_score)
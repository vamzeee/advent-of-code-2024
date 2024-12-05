################# part 1 ###############

input = open('input.txt').read().strip()

def is_order_correct(conditions, pages):
    for i in range(len(pages)-1):
        for j in range(i+1,len(pages)):
            temp_cond = pages[j] + "|" + pages[i]
            if temp_cond in conditions :
                return False
    return True

conditions = []
wrong_updates = []
update_queue = []
total = 0
for line in input.splitlines() :
    if '|' in line :
        conditions.append(line)
    elif line == '' :
        continue
    else :
        update_queue.append(line)

for update in update_queue :
    pages = update.split(',')

    if is_order_correct(conditions, pages):
        total += int(pages[len(pages)//2])
    ## required for part 2
    else :
        wrong_updates.append(pages)
print(total)

################# part 2 ###############
total_v2 = 0
times = 0
for update in wrong_updates:
    fixed = False
    while not fixed :
        fixed = True
        for i in range(len(update)-1):
            for j in range(i+1,len(update)):
                temp_cond = update[j] + "|" + update[i]
                if temp_cond in conditions:
                    temp = update[i]
                    update[i] = update[j]
                    update[j] = temp
                    fixed = False

for update in wrong_updates :
    total_v2+=int(update[len(update)//2])

print(total_v2)
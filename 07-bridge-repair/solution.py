################# part 1 ###############

input = open('input.txt').read().strip()

total = 0
operations = ['+', '*']

def generate_solutions(operations, nums):
    if len(nums) == 1:
        return [nums]
    
    combinations = []
    for op in operations:
        if op == '+':
            result = int(nums[0]) + int(nums[1])
        else:
            result = int(nums[0]) * int(nums[1])
        
        new_nums = [result] + nums[2:]
        combinations.extend(generate_solutions(operations, new_nums))

    return combinations

for line in input.splitlines():
    exp = line.split(':')[0]
    nums = line.split(':')[1].split()
    combinations = generate_solutions(operations, nums)
    if [int(exp)] in combinations:
        total+=int(exp)

print(total)


################# part 2 ###############
total = 0
operations = ['+', '*', '||']

def generate_solutions_v2(operations, nums):
    if len(nums) == 1:
        return [nums]
    
    combinations = []
    for op in operations:
        if op == '+':
            result = int(nums[0]) + int(nums[1])
        elif op == '*':
            result = int(nums[0]) * int(nums[1])
        else:
            result = int(str(nums[0]) + str(nums[1]))
        
        new_nums = [result] + nums[2:]
        combinations.extend(generate_solutions_v2(operations, new_nums))

    return combinations

for line in input.splitlines():
    exp = line.split(':')[0]
    nums = line.split(':')[1].split()
    combinations = generate_solutions_v2(operations, nums)
    if [int(exp)] in combinations:
        total+=int(exp)

print(total)
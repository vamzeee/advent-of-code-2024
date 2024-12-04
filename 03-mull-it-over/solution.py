################# part 1 ###############

import re

input = open('input.txt').read().strip()

expression = r"mul\(\d{1,3},\d{1,3}\)"

instructions = re.findall(expression, input)
total = 0
for instruction in instructions :
    num1 = int(instruction[instruction.find('(') + 1 : instruction.find(',')])
    num2 = int(instruction[instruction.find(',') + 1 : instruction.find(')')])
    total = total + (num1 * num2)

print(total)


################# part 2 ###############

new_expression = r"mul\(\d{1,3},\d{1,3}\)|don't\(\)|do\(\)"

all_instructions = re.findall(new_expression, input)
new_total = 0
are_instructions_enabled = True
for instruction in all_instructions :
    if instruction == "do()" :
        are_instructions_enabled = True
    elif instruction == "don't()" :
        are_instructions_enabled = False
    else :
        if are_instructions_enabled :
            num1 = int(instruction[instruction.find('(') + 1 : instruction.find(',')])
            num2 = int(instruction[instruction.find(',') + 1 : instruction.find(')')])
            new_total = new_total + (num1 * num2)

print(new_total)
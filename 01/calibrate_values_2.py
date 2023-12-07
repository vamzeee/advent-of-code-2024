# some of the digits are actually spelled out with letters: one, two, three, four, five, 
# six, seven, eight, and nine also count as valid "digits".
# Now, find the sum of all calibration values

sum = 0
def get_actual_line(line) :
    actual_line = line.replace("one", "one1one").replace("two", "two2two").replace("three", "three3three").replace("four", "four4four").replace("five", "five5five").replace("six", "six6six").replace("seven", "seven7seven").replace("eight", "eight8eight").replace("nine", "nine9nine")
    return actual_line

with open("D:/advent-of-code-2024/01/input.txt") as input :
    for line in input :
        number = ''
        actual_line = get_actual_line(line)
        reversed_line = actual_line[::-1]

        for i in actual_line :
            if i.isdigit() :
                number += i
                break
        for i in reversed_line :
            if i.isdigit() :
                number += i
                break
        if number != '' :
            sum+=int(number)
    print(sum)
# On each line, the calibration value can be found by combining the first digit 
# and the last digit (in that order) to form a single two-digit number.
# Find the sum of all calibration values
 
sum = 0

with open("input.txt") as input :
    for line in input :
        number = ''
        reversed_line = line[::-1]

        for i in line :
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
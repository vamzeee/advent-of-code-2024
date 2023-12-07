# https://adventofcode.com/2023/day/4

cards = open("D:/advent-of-code-2024/04/input.txt").read().strip()
sum = 0
for card in cards.splitlines() :
    points = 0
    winners = card.split(': ')[1].split(' | ')[0].split()
    numbers = card.split(': ')[1].split(' | ')[1].split()
    for num in numbers :
        if num in winners :
            if points == 0 :
                points+=1
            else :
                points*=2
    sum+=points
print(sum)

# https://adventofcode.com/2023/day/4#part2

cards = open("D:/advent-of-code-2024/04/input.txt").read().strip().splitlines()
D = dict()

for i in range(len(cards)) :
    D[i] = D.get(i, 0) + 1
    points = 0
    winners = cards[i].split(': ')[1].split(' | ')[0].split()
    numbers = cards[i].split(': ')[1].split(' | ')[1].split()
    for num in numbers :
        if num in winners :
            points+=1
    
    i_cards = D.get(i)

    p = i + 1
    while p <= i + points and p < len(cards) :
        D[p] = D.get(p, 0) + i_cards
        p+=1        

print(sum(D.values()))
    
     
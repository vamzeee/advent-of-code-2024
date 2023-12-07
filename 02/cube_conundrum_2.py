# https://adventofcode.com/2023/day/2#part2

sum = 0

with open("D:/advent-of-code-2024/02/input.txt") as input :
    for line in input :
        games = line.split(':')[1].split(';')
        min_red = 0
        min_green = 0
        min_blue = 0
        for game in games :
            for x in game.split(",") :
                x = x.strip()
                if ('red' in x and int(x.split()[0]) > min_red) :
                    min_red = int(x.split()[0])      
                elif('green' in x and int(x.split()[0]) > min_green) :
                    min_green = int(x.split()[0])
                elif('blue' in x and int(x.split()[0]) > min_blue) :
                    min_blue = int(x.split()[0])
        sum+= (min_red * min_green * min_blue) 
print(sum)
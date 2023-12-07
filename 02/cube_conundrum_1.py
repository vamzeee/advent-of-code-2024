# https://adventofcode.com/2023/day/2

sum = 0
with open("D:/advent-of-code-2024/02/input.txt") as input :
    for line in input :
        game_number = int(line.split(':')[0].split()[1])
        games = line.split(':')[1].split(';')
        impossible = False
        for game in games :
            if impossible :
                break
            for x in game.split(",") :
                x = x.strip()
                if ('red' in x and int(x.split()[0]) > 12) :
                    impossible = True
                    break      
                elif('green' in x and int(x.split()[0]) > 13) :
                    impossible = True
                    break
                elif('blue' in x and int(x.split()[0]) > 14) :
                    impossible = True
                    break
        if not impossible :
            print(game_number)
            sum+=game_number
print(sum)
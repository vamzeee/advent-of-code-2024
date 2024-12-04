################# part 1 ###############

input = open('input.txt').read().strip()

word = 'XMAS'
directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
total = 0

lines = input.splitlines()

def is_valid(i,j) :
    return 0 <= i < len(lines) and 0 <= j < len(lines[0])

def check_in_direction(i,j,di,dj) :
    for x in range(len(word)) :
        ni, nj = i + x * di, j + x * dj
        if not is_valid(ni, nj) or lines[ni][nj] != word[x] :
            return False
    return True

for i in range(len(lines)) :
    for j in range(len(lines[0])) :
        if lines[i][j] == word[0] :
            for direction in directions :
                if check_in_direction(i,j,direction[0],direction[1]) :
                    total +=1

print(total)


################# part 2 ###############

dir1 = [(-1,-1), (1,1)]
dir2 = [(-1,1), (1,-1)]

new_total = 0

def is_valid_v2(i,j):
    return 1 <= i < len(lines)-1 and 1 <= j < len(lines[0])-1

def check_diagonal(i,j,dir):
    ni1, nj1 = i + dir[0][0], j + dir[0][1]
    ni2, nj2 = i + dir[1][0], j + dir[1][1]

    if (lines[ni1][nj1] == 'M' and lines[ni2][nj2] == 'S') or (lines[ni1][nj1] == 'S' and lines[ni2][nj2] == 'M'):
        return True
    return False

for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j] == 'A' and is_valid_v2(i,j):
            if check_diagonal(i,j,dir1) and check_diagonal(i,j,dir2) :
                new_total +=1

print(new_total)


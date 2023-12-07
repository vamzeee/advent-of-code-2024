D = open("D:/advent-of-code-2024/03/input.txt").read().strip()
lines = D.split('\n')
matrix = [[c for c in line] for line in lines]
R = len(matrix)
C = len(matrix[0])

sum = 0
for r in range(len(matrix)) :
    number = ''
    is_part = False
    for c in range(len(matrix[r]) + 1) :
        if c < C and matrix[r][c].isdigit() :
            number+=matrix[r][c]
            



################# part 1 ###############

from itertools import cycle

input = open('input.txt').read().strip()

def locate_initial_location(rows):
    for i in range(len(rows)):
        for j in range(len(rows[0])):
            if rows[i][j] == '^':
                return i,j

def detect_edge(x,y,current_direction, rows):
    dx,dy = current_direction
    return not (0 <= x+dx < len(rows) and 0 <= y+dy < len(rows[0]))

rows = []
for row in input.splitlines():
    rows.append(list(row))

iterator = cycle([(-1,0), (0,1), (1,0), (0,-1)])
x,y = locate_initial_location(rows)
visited_locations = {(x,y)}

current_direction = next(iterator)
while not detect_edge(x,y,current_direction,rows):
    dx,dy = current_direction
    if rows[x+dx][y+dy] == '#':
        current_direction = next(iterator)
        continue
    x+=dx
    y+=dy
    visited_locations.add((x,y))

print(len(visited_locations))


################# part 2 ###############

count = 0

visited_locations.remove(locate_initial_location(rows))
for location in visited_locations:
    iterator = cycle([(-1,0), (0,1), (1,0), (0,-1)])
    current_direction = next(iterator)
    x,y = locate_initial_location(rows)
    rows[location[0]][location[1]] = '#'
    loc_with_dir = [(x,y,current_direction)]
    while not detect_edge(x,y,current_direction,rows):
        dx,dy = current_direction
        if rows[x+dx][y+dy] == '#':
            current_direction = next(iterator)
            continue
        x+=dx
        y+=dy
        if (x,y,current_direction) in loc_with_dir:
            count+=1
            break
        loc_with_dir.append((x,y,current_direction))
print(count)



















# def are_we_looping(x,y,current_direction,rows):
#     tx,ty = x,y
#     dx,dy = current_direction
#     rows_v2 = list(rows)
#     rows_v2[tx+dx][ty+dy] = '#'
#     turns = 3 # 
#     while turns > 0:
#         if rows[tx+dx][ty+dy] == '#':
#             rows_v2 = [list(row) for row in zip(*rows_v2)][::-1]
#             turns-=1
#             continue
#         else:
#             tx+=dx
#             ty+=ty
#     return x == tx and y == ty


# while not detect_edge(x,y,current_direction,rows):
#     dx,dy = current_direction
#     if not rows[x+dx][y+dy] == '#':
#         if are_we_looping(x,y,current_direction,rows):
#             count+=1
#         x+=dx
#         y+=dy
#         continue
#     current_direction = next(iterator)

# print(count)
        



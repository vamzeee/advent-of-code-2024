################# part 1 ###############

input = open('input.txt').read().strip()

antennas = dict()
grid = input.splitlines()
antinodes = set()

def find_distance(source, target):
    return tuple([target[0]-source[0], target[1]-source[1]])

def is_in_range(source, distance, grid):
    return 0 <= source[0] - distance[0] < len(grid) and 0 <= source[1] - distance[1] < len(grid[0])

def find_antinode(source, distance):
    return tuple([source[0] - distance[0], source[1] - distance[1]])

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if not grid[i][j] == ".":
            if grid[i][j] in antennas:
                antennas[grid[i][j]].append(tuple((i,j)))
            else:
                antennas[grid[i][j]] = []
                antennas[grid[i][j]].append(tuple((i,j)))

for locations in antennas.values():
    for i in range(len(locations)-1):
        for j in range(i+1, len(locations)):
            dist1 = find_distance(locations[i], locations[j])
            if is_in_range(locations[i], dist1, grid):
                antinodes.add(find_antinode(locations[i], dist1))
            dist2 = find_distance(locations[j], locations[i])
            if is_in_range(locations[j], dist2, grid):
                antinodes.add(find_antinode(locations[j], dist2))
                    
print(len(antinodes))


################# part 1 ###############
antinodes = set()

def find_antinodes_v2(source, distance, grid):
    loc_anti = set()
    while is_in_range(source, distance, grid):
        antinode = tuple([source[0] - distance[0], source[1] - distance[1]])
        loc_anti.add(antinode)
        source = antinode
    return loc_anti

for locations in antennas.values():
    for i in range(len(locations)-1):
        for j in range(i+1, len(locations)):
            antinodes.add(locations[i])
            antinodes.add(locations[j])
            dist1 = find_distance(locations[i], locations[j])
            if is_in_range(locations[i], dist1, grid):
                antinodes.update(find_antinodes_v2(locations[i], dist1, grid))
            dist2 = find_distance(locations[j], locations[i])
            if is_in_range(locations[j], dist2, grid):
                antinodes.update(find_antinodes_v2(locations[j], dist2, grid))

print(len(antinodes))
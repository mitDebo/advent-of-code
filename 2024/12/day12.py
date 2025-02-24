with open("input.txt") as f:
    lines = f.readlines()

map = []
for l in lines:
    l = l.strip()
    row = []
    for c in l:
        row.append(c)
    map.append(row)

areas = []

def find_area(map:list, y:int, x:int) -> (int, int):
    if isinstance(map[y][x], int):
        return 0, 0

    fencing, area = map_area(map, y, x, map[y][x])
    for y, row in enumerate(map):
        for x, c in enumerate(row):
            if c == '-':
                map[y][x] = len(areas)
    return fencing, area

def map_area(map:list, y:int, x:int, crop:str) -> (int, int):
    if y < 0 or y >= len(map) or x < 0 or x >= len(map[0]):
        return 1, 0
    if map[y][x] == '-':
        return 0, 0
    if map[y][x] != crop:
        return 1, 0

    fencing, area = 0, 1
    map[y][x] = "-"

    f, a = map_area(map, y + 1, x, crop)
    fencing += f
    area += a
    f, a = map_area(map, y - 1, x, crop)
    fencing += f
    area += a
    f, a = map_area(map, y, x + 1, crop)
    fencing += f
    area += a
    f, a = map_area(map, y, x - 1, crop)
    fencing += f
    area += a

    return fencing, area

for y, row in enumerate(map):
    for x, c in enumerate(row):
        if c != "-":
            areas.append(find_area(map, y, x))

total = 0
for a in areas:
    total += a[0] * a[1]

print("Answer one: {}".format(total))
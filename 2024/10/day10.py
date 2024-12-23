def get_trailhead_score(m:list, y:int, x:int) -> int:
    if y >= len(m) or x >= len(m[0]):
        return 0

    elevation = int(m[y][x])
    if elevation == 9:
        return 1

    total = 0
    if y - 1 >= 0 and m[y - 1][x] == elevation + 1:
        total += get_trailhead_score(m, y - 1, x)
    if y + 1 < len(m) and m[y + 1][x] == elevation + 1:
        total += get_trailhead_score(m, y + 1, x)
    if x - 1 >= 0 and m[y][x - 1] == elevation + 1:
        total += get_trailhead_score(m, y, x - 1)
    if x + 1 < len(m[0]) and m[y][x + 1] == elevation + 1:
        total += get_trailhead_score(m, y, x + 1)

    return total

def get_trailhead_endpoints(m:list, y:int, x:int) -> set:
    if y >= len(m) or x >= len(m[0]):
        return set()

    elevation = int(m[y][x])
    if elevation == 9:
        return {(y, x)}

    trailheads = set()
    if y - 1 >= 0 and m[y - 1][x] == elevation + 1:
        trailheads = trailheads.union(get_trailhead_endpoints(m, y - 1, x))
    if y + 1 < len(m) and m[y + 1][x] == elevation + 1:
        trailheads = trailheads.union(get_trailhead_endpoints(m, y + 1, x))
    if x - 1 >= 0 and m[y][x - 1] == elevation + 1:
        trailheads = trailheads.union(get_trailhead_endpoints(m, y, x - 1))
    if x + 1 < len(m[0]) and m[y][x + 1] == elevation + 1:
        trailheads = trailheads.union(get_trailhead_endpoints(m, y, x + 1))

    return trailheads

map = []

with open('input.txt') as f:
    for y, line in enumerate(f):
        w = []
        for x, c in enumerate(line.strip()):
            if c == '.':
                c = 0
            w.append(int(c))
        map.append(w)

total = 0
score = 0
for y, line in enumerate(map):
    for x, c in enumerate(line):
        if int(c) == 0:
            total += len(get_trailhead_endpoints(map, y, x))
            score += get_trailhead_score(map, y, x)

print("Answer one: {}".format(total))
print("Answer two: {}".format(score))
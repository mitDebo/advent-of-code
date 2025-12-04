def total_neighbors(grid:list, x:int, y:int) -> int:
    gridlen = len(grid)
    gridheight = len(grid[0])

    total = 0
    for j in range(y - 1, y + 2):
        if j < 0 or j >= gridheight:
            continue
        for i in range(x - 1, x + 2):
            if i < 0 or i >= gridlen or (x == i and y == j):
                continue
            if grid[j][i] == '@':
                total += 1

    return total

def get_removable_items(grid:list) -> list:
    items = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            cur_grid = grid[y][x]
            if cur_grid == '@':
                t = total_neighbors(grid, x, y)
                if t < 4:
                    items.append((x, y))
    return items

grid = []
total = 0
with open('input.txt', 'r') as f:
    for line in f.readlines():
        grid.append(list(line.strip()))

items_to_remove = get_removable_items(grid)
while len(items_to_remove) > 0:
    amt = len(items_to_remove)
    print(f"Removing {amt} items")
    total += amt
    for item in items_to_remove:
        grid[item[1]][item[0]] = '.'
    items_to_remove = get_removable_items(grid)

print(total)
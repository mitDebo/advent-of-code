def has_value(b:list, y:int, x:int, value:str) -> bool:
    if y < 0 or y >= len(b) or x < 0 or x >= len(b[y]):
        return False

    return b[y][x] == value

def get_xmas_count(b:list, y:int, x:int) -> int:
    if b[y][x] != 'X':
        return 0

    total = 0
    for vx in [-1, 0, 1]:
        for vy in [-1, 0, 1]:
            if (has_value(b, y + vy, x + vx, 'M')
                and has_value(b, y + 2 * vy, x + 2 * vx, 'A')
                and has_value(b, y + 3 * vy, x + 3 * vx, 'S')):
                total += 1

    return total

def has_double_mas(b:list, y:int, x:int) -> bool:
    v = b[y][x]

    if v != 'A':
        return False

    for dx in [-1, 1]:
        for dy in [-1, 1]:
            if (has_value(b, y - dy, x + dx, 'M')
                and has_value(b, y - dy, x - dx, 'M')
                and has_value(b, y + dy, x - dx, 'S')
                and has_value(b, y + dy, x + dx, 'S')):
                return True
            if (has_value(b, y + dy, x - dx, 'M')
                and has_value(b, y - dy, x - dx, 'M')
                and has_value(b, y + dy, x + dx, 'S')
                and has_value(b, y - dy, x + dx, 'S')):
                return True

    return False

board = []

with open("input.txt") as f:
    for line in f:
       board.append(list(line.strip()))

total = 0
double_mas_total = 0
for y, row in enumerate(board):
    for x, value in enumerate(row):
        total += get_xmas_count(board, y, x)
        if has_double_mas(board, y, x):
            double_mas_total += 1

print("Answer one: " + str(total))
print("Answer two: " + str(double_mas_total))

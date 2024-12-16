def has_value(b:list, x:int, y:int, value:str) -> bool:
    if y < 0 or y >= len(b) or x < 0 or x >= len(b[y]):
        return False

    return b[x][y] == value

def get_xmas_count(b:list, x:int, y:int) -> int:
    if b[x][y] != 'X':
        return 0

    total = 0
    for vx in [-1, 0, 1]:
        for vy in [-1, 0, 1]:
            if (has_value(b, x + vx, y + vy, 'M')
                and has_value(b, x + 2 * vx, y + 2 * vy, 'A')
                and has_value(b, x + 3 * vx, y + 3 * vy, 'S')):
                total += 1

    return total



board = []

with open("input.txt") as f:
    for line in f:
       board.append(list(line.strip()))

total = 0
double_mas_total = 0
for y, row in enumerate(board):
    for x, value in enumerate(row):
        total += get_xmas_count(board, x, y)
        double_mas_total = get_double_mas_count(board, x, y)

print("Answer one: " + str(total))
print("Answer two: " + str(double_mas_total))

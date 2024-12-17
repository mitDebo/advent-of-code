class Guard:
    def __init__(self, y:int, x:int, direction:str):
        self.x = x
        self.y = y
        self.direction = direction

    def rotate(self):
        if self.direction == "^":
            self.direction = ">"
        elif self.direction == ">":
            self.direction = "v"
        elif self.direction == "v":
            self.direction = "<"
        elif self.direction == "<":
            self.direction = "^"

    def update(self):
        if self.direction == "^":
            self.y -= 1
        elif self.direction == ">":
            self.x += 1
        elif self.direction == "v":
            self.y += 1
        elif self.direction == "<":
            self.x -= 1


def is_guard_on_board(g:Guard, b:list) -> bool:
    return 0 <= g.y < len(b) and 0 <= g.x < len(b[0])


def is_next_square_blocked(g:Guard, b:list) -> bool:
    h = len(b)
    w = len(b[0])

    if g.direction == "^":
        return b[max(g.y - 1, 0)][g.x] == '#'
    elif g.direction == ">":
            return b[g.y][min(w - 1, g.x + 1)] == '#'
    elif g.direction == "v":
            return b[min(h - 1, g.y + 1)][g.x] == '#'
    elif g.direction == "<":
            return b[g.y][max(0, g.x - 1)] == '#'

    return False

def update_board(g:Guard, b:list) -> None:
    if is_next_square_blocked(g, b):
        g.rotate()
        b[g.y][g.x] = g.direction
        return

    b[g.y][g.x] = "X"
    g.update()
    if is_guard_on_board(g, b):
        b[g.y][g.x] = g.direction


def print_board(b:list) -> None:
    for row in b:
        print(''.join(row))

board = []
row_num = 0

with open("input.txt") as f:
    for line in f:
        row = list(line.strip())
        if '^' in row:
            guard = Guard(row_num, row.index('^'), "^")

        board.append(row)
        row_num += 1

while is_guard_on_board(guard, board):
    update_board(guard, board)

total = 0
for row in board:
    for cell in row:
        if cell == 'X':
            total += 1

print("Answer one: {}".format(total))
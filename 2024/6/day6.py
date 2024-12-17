import copy

class Guard:
    def __init__(self, y:int, x:int, direction:str):
        self.__original_y = y
        self.__original_x = x
        self.__original_direction = direction

        self.x = x
        self.y = y
        self.direction = direction

        self.visited = [(y, x, "^")]
        self.is_looping = False

    def rotate(self):
        if self.direction == "^":
            self.direction = ">"
        elif self.direction == ">":
            self.direction = "v"
        elif self.direction == "v":
            self.direction = "<"
        elif self.direction == "<":
            self.direction = "^"
        self.__append_visited()

    def update(self):
        if self.direction == "^":
            self.y -= 1
        elif self.direction == ">":
            self.x += 1
        elif self.direction == "v":
            self.y += 1
        elif self.direction == "<":
            self.x -= 1
        self.__append_visited()

    def is_stuck(self):
        return self.is_looping

    def reset(self):
        self.x = self.__original_x
        self.y = self.__original_y
        self.direction = self.__original_direction

        self.visited = [(self.y, self.x, self.direction)]
        self.is_looping = False


    def __append_visited(self):
        n = (self.y, self.x, self.direction)
        if n in self.visited:
            self.is_looping = True
        self.visited.append(n)


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

    # b[g.y][g.x] = 'X'
    g.update()
    if is_guard_on_board(g, b):
        b[g.y][g.x] = g.direction


def print_board(b:list) -> None:
    for r in b:
        print(''.join(r))

original_board = []
row_num = 0

with open("input.txt") as f:
    for line in f:
        row = list(line.strip())
        if '^' in row:
            guard = Guard(row_num, row.index('^'), "^")

        original_board.append(row)
        row_num += 1

board = copy.deepcopy(original_board)
while is_guard_on_board(guard, board) and not guard.is_stuck():
    update_board(guard, board)

visited = 0
for row in board:
    for cell in row:
        if cell in ['X', '^', '>', 'v', '<']:
            visited += 1

loop_totals = 0
for y, row in enumerate(original_board):
    for x, cell in enumerate(row):
        print("attempting {y}, {x}".format(y=y, x=x))
        new_board = copy.deepcopy(original_board)
        if new_board[y][x] == '#' or new_board[y][x] == '^':
            continue

        guard.reset()
        new_board[y][x] = '#'
        while is_guard_on_board(guard, new_board) and not guard.is_stuck():
            update_board(guard, new_board)

        if guard.is_stuck():
            loop_totals += 1

print("Answer one: {}".format(visited))
print("Answer two: {}".format(loop_totals))
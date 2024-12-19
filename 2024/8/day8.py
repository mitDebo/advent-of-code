class Node:
    def __init__(self, y:int, x:int, c:str):
        self.y = y
        self.x = x
        self.c = c

    def is_on_board(self, height:int, width:int) -> bool:
        return 0 <= self.y < height and 0 <= self.x < width

    def __eq__(self, other):
        return self.y == other.y and self.x == other.x

    def __add__(self, other):
        return Node(self.y + other.y, self.x + other.x, 'X')

    def __sub__(self, other):
        return Node(self.y - other.y, self.x - other.x, 'X')

    def __mul__(self, other:int):
        return Node(self.y * other, self.x * other, 'X')

with open("input.txt") as f:
    lines = f.read().strip().split("\n")

map = []
nodes = {}

board_height = len(lines)
board_width = len(lines[0])
found_nodes = []

def print_board(lines:list, nodes:list):
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            n = Node(y, x, 'X')
            print('#' if n in nodes else c, end="")
        print()

def find_anti_nodes(existing:list, new:Node) -> list:
    anti_nodes = [new]
    for e in existing:
        delta_node = Node(new.y - e.y, new.x - e.x, 'X')

        i = -1
        test_node = e + delta_node * i
        while test_node.is_on_board(board_height, board_width):
            anti_nodes.append(test_node)
            i -= 1
            test_node = e + delta_node * i

        i = 1
        test_node = new + delta_node
        while test_node.is_on_board(board_height, board_width):
            anti_nodes.append(test_node)
            i += 1
            test_node = new + delta_node * i

    return anti_nodes

for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c != '.':
            if c not in nodes:
                nodes[c] = []
            n = Node(y, x, c)
            for anti_node in find_anti_nodes(nodes[c], n):
                if anti_node not in found_nodes:
                    found_nodes.append(anti_node)
            nodes[c].append(n)

print_board(lines, found_nodes)
print("Answer one: {}".format(len(found_nodes)))
class Node:
    def __init__(self, y:int, x:int, c:str):
        self.y = y
        self.x = x
        self.c = c

    def is_on_board(self, width:int, height:int) -> bool:
        return 0 <= self.y < height and 0 <= self.x < width

    def __eq__(self, other):
        return self.y == other.y and self.x == other.x and self.c == other.c

with open("input.txt") as f:
    lines = f.read().strip().split("\n")

map = []
nodes = {}

board_height = len(lines)
board_width = len(lines[0])
found_nodes = []

def find_anti_nodes(existing:list, new:Node) -> list:
    anti_nodes = []
    for e in existing:
        print(f"Testing: {e.c}:({e.y}, {e.x}) vs {e.c}:({new.y}, {new.x})")
        anti_node1 = Node(2 * e.y - new.y, 2 * e.x - new.x, 'x')
        anti_node2 = Node(2 * new.y - e.y, 2 * new.x - e.x, 'x')

        if anti_node1.is_on_board(board_height, board_width):
            print(f"Found: ({anti_node1.y}, {anti_node1.x})")
            anti_nodes.append(anti_node1)
        if anti_node2.is_on_board(board_height, board_width):
            print(f"Found: ({anti_node2.y}, {anti_node2.x})")
            anti_nodes.append(anti_node2)
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

print("Answer one: {}".format(len(found_nodes)))


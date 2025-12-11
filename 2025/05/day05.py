import math
from typing import Self

class Node:
    def __init__(self, min:int = 0, max:int = math.inf):
        self.min:int = min
        self.max:int = max
        self.next:Self = None


    def add(self, n:Self) -> Self:
        if n.max < self.min:
            n.next = self
            return n

        if n.min > self.max:
            if self.next == None:
                self.next = n
            else:
                node = self.next.add(n)
                self.next = node
            return self

        if n.min < self.min:
            self.min = n.min

        if self.max < n.max:
            self.max = n.max

        # trim out the nodes now covered by this one
        node = self
        while node.next is not None and node.next.min <= self.max:
            node = node.next
        self.max = max(self.max, node.max)
        self.next = node.next

        return self
class Range:
    def __init__(self):
        self.head = None


    def add(self, n:Node):
        if self.head == None:
            self.head = n
            return
        else:
            node = self.head.add(n)
            self.head = node

    def is_in_range(self, i:int) -> bool:
        if self.head == None:
            return False
        n:Node = self.head
        while n is not None:
            if n.min <= i <= n.max:
                return True
            n = n.next

        return False

    def get_count(self) -> int:
        if self.head == None:
            return 0
        else:
            node = self.head
            count = 0
            while node is not None:
                count += node.max - node.min + 1
                node = node.next

            return count

    def print(self):
        node = self.head
        while node is not None:
            print(f"({node.min} --> {node.max})")
            node = node.next

def get_range(line:str) -> Node:
    line = line.strip()
    v = line.split('-')
    min = int(v[0])
    max = int(v[1])
    return Node(min=min, max=max)


with open('input.txt', 'r') as f:
    lines = f.readlines()

total = 0
count = 0
gathering_ingredients = True
range = Range()
for i, line in enumerate(lines):
    if line.isspace():
        gathering_ingredients = False
        continue

    if gathering_ingredients:
        r = get_range(line)
        print(f"Adding ({r.min}, {r.max})")
        range.add(r)
        range.print()
        print()
    else:
        v = int(line.strip())
        if range.is_in_range(v):
            total += 1

print(f"Total: {total}")
print(f"Count: {range.get_count()}")
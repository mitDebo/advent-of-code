def calculate_stack(s:list, op:str) -> int:
    total = 0 if op == "+" else 1
    while len(s) > 0:
        if op == "+":
            total += s.pop()
        else:
            total *= s.pop()

    return total

with open("input.txt", "r") as f:
    lines = f.readlines()

max_y = len(lines)
max_x = len(lines[0])

stack = []
current_int = ""
grand_total = 0
for x in range(max_x - 2, -1, -1):
    for y in range(max_y):
        c = lines[y][x]
        if c == "+" or c == "*":
            stack.append(int(current_int))
            grand_total += calculate_stack(stack, c)
            stack = []
            current_int = ""
            break
        current_int += c

    current_int = current_int.strip()
    if current_int == "":
        continue
    stack.append(int(current_int))
    current_int = ""

print(grand_total)

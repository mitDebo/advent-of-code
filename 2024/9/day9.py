import copy

def defragment(d:list) -> list:
    disk = copy.deepcopy(d)
    i = 0
    k = len(disk) - 1
    while disk[i] != -1 and i <= k:
        i += 1
    while disk[k] == -1 and k >= i:
        k -= 1

    while i <= k:
        temp = disk[i]
        disk[i] = disk[k]
        disk[k] = temp
        while disk[i] != -1 and i <= k:
            i += 1
        while disk[k] == -1 and k >= i:
            k -= 1

    return disk

def defragment2(d:list) -> list:
    def find_next_free_block(d: list, start: int) -> (int, int):
        i = start
        width = 0
        while i < len(d) and d[i] != -1:
            i += 1
        while i + width < len(d) and d[i + width] == -1:
            width += 1
        return i, width

    def find_previous_occupied_block(d: list, end: int) -> (int, int):
        i = end - 1
        width = 0
        while d[i] == -1 and i > 0:
            i -= 1
        file_id = d[i]

        while d[i] == file_id and i > 0:
            width += 1
            i -= 1
        i += 1
        return i, width

    def swap_blocks(d:list, free_start:int, occupied_start:int, length:int):
        for i in range(length):
            temp = d[free_start + i]
            d[free_start + i] = d[occupied_start + i]
            d[occupied_start + i] = temp

    disk = copy.deepcopy(d)
    f, f_width = find_next_free_block(disk, 0)  # f = start of free block
    o, o_width = find_previous_occupied_block(disk, len(disk))  # o = start of occupied block
    left, right = f, o + o_width

    while left < right:
        while o >= f:
            file_id = d[o]
            if o_width <= f_width:
                swap_blocks(disk, f, o, o_width)
            elif f < right:
                f, f_width = find_next_free_block(disk, f + f_width)
                continue
            f, f_width = find_next_free_block(disk, left)
            o, o_width = find_previous_occupied_block(disk, o)

        f, f_width = find_next_free_block(disk, left)
        o, o_width = find_previous_occupied_block(disk, o)
        left = f
        right = o + o_width

    return disk

def checksum(disk:list) -> int:
    total = 0
    for i, c in enumerate(disk):
        if c != -1:
            total += i * c

    return total


disk = []
is_free_block = False
id = 0

with open("input.txt") as f:
    for line in f:
        for c in line:
            for i in range(int(c)):
                if is_free_block:
                    disk.append(-1)
                else:
                    disk.append(id)
            if not is_free_block:
                id += 1
            is_free_block = not is_free_block

disc = defragment(disk)
disc2 = defragment2(disk)
print(disc)
print(disc2)
print(checksum(disc))
print(checksum(disc2))

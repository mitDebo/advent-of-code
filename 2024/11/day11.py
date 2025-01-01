cache = dict()

def count_blinks(stones:list, iterations:int) -> int:
    total = 0
    for s in stones:
        total += count_blinks_full(s, iterations)
    return total

def count_blinks_full(stone: int, iterations:int) -> int:
    if iterations == 0:
        return 1
    if (stone, iterations) in cache:
        return cache[(stone, iterations)]

    if stone == 0:
        result = count_blinks_full(1, iterations - 1)
    elif len(str(stone)) % 2 == 0:
        index = len(str(stone)) // 2
        left_count = count_blinks_full(int(str(stone)[:index]), iterations - 1)
        right_count = count_blinks_full(int(str(stone)[index:]), iterations - 1)
        result = left_count + right_count
    else:
        result = count_blinks_full(stone * 2024, iterations - 1)

    cache[(stone, iterations)] = result
    return result


with open("input.txt") as f:
    line = f.readline().strip()

stones = list(map(int, line.split(" ")))
total25 = count_blinks(stones, 75)

print("Answer one: {}".format(total25))
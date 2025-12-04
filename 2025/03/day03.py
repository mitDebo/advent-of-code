def calculate_joltage(s:str) -> int:
    joltage = "000000000000"
    for i, c in enumerate(s):
        for r, j in enumerate(joltage):
            dist_s = len(s) - i
            dist_j = len(joltage) - r
            if dist_s >= dist_j:
                if int(c) > int(j):
                    joltage = joltage[:r] + c + "0" * (len(joltage) - r - 1)
                    break

    return int(joltage)


total = 0

with open("input.txt", "r") as f:
    for line in f.readlines():
        line = line.strip()
        total += calculate_joltage(line)

    print(total)






def has_repeats(value:int) -> bool:
    s = str(value)
    return s in (s + s)[1:-1]

total = 0

with open('input.txt', 'r') as f:
    for line in f.readlines():
        ranges = line.split(',')
        for r in ranges:
            print(f"EVALUATING {r}")
            values = r.split('-')
            s_min = values[0]
            s_max = values[1]

            i = int(s_min)
            while i <= int(s_max):
                if has_repeats(i):
                    total += i
                i += 1

print(total)

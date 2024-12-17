total = 0

with open("input.txt") as f:
    for line in f:
        line = line.strip()
        l = line.split(":")

        goal = int(l[0])
        terms = l[1].strip().split()

        for op in range(2 ** len(terms) - 1):
            running_total = 0
            for i, term in enumerate(terms):
                if i == 0:
                    running_total = int(term)
                    continue
                running_total = running_total + int(term) if (op >> i & 1) else running_total * int(term)

            if running_total == goal:
                total += running_total
                break

print("Answer one: {}".format(total))
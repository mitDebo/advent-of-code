def add_rule(r:dict, l:str):
    comes_before, value = l.split("|")
    if value not in r:
        r[value] = []
    r[value].append(comes_before)

def is_good(page_order:list, r:dict):
    for i in range(len(pages)):
        rule = rules.get(pages[i])
        # if no rule found, just continue
        if rule is None:
            continue
        s = set(rule).intersection(set(pages[i:]))
        if len(s) > 0:
            return False

    return True


rules = {}
unfixed_total = 0
total = 0

with open("input.txt") as f:
    for line in f:
        line = line.strip()
        if line == "":
            break
        add_rule(rules, line)

    for line in f:
        pages = line.strip().split(",")
        if is_good(pages, rules):
            unfixed_total += int(pages[len(pages) // 2])

    total += int(pages[len(pages) // 2])

print("Answer one: {}".format(unfixed_total))
print("Answer two: {}".format(total))
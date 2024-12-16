def add_rule(r:dict, l:str):
    comes_before, value = l.split("|")
    if value not in r:
        r[value] = []
    r[value].append(comes_before)

def is_good(page_order:list, r:dict):
    for i in range(len(page_order)):
        rule = rules.get(page_order[i])
        # if no rule found, just continue
        if rule is None:
            continue
        s = set(rule).intersection(set(page_order[i:]))
        if len(s) > 0:
            return False

    return True

def fix_pages(page_order:list, r:dict) -> list:
    i = len(page_order) - 1
    while i >= 0:
        l = page_order[i:]
        if not is_good(l, r):
            temp = page_order[i]
            page_order[i] = page_order[i + 1]
            page_order[i + 1] = temp
            i += 1
            continue

        i -= 1
    return page_order


rules = {}
unfixed_total = 0
fixed_total = 0

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
        else:
            pages = fix_pages(pages, rules)
            fixed_total += int(pages[len(pages) // 2])

print("Answer one: {}".format(unfixed_total))
print("Answer two: {}".format(fixed_total))
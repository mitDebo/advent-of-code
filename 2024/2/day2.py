def is_safe_step(step: int, prev_step: int) -> bool:
    if (step == 0
        or abs(step) > 3
        or prev_step < 0 < step
        or step < 0 < prev_step):
        return False

    return True

def is_safe(l: list) -> bool:
    if len(l) < 2:
        return False

    last_value = 0
    last_distance = 0
    for index, value in enumerate(l):
        value = int(value)
        if index == 0:
            last_value = value
            continue

        distance = value - last_value
        if not is_safe_step(distance, last_distance):
            return False

        last_value = value
        last_distance = distance

    return True

def is_tolerance_safe(l: list) -> bool:
    if is_safe(l):
        return True

    for i in range(len(l)):
        tolerance_list = l[:i] + l[i+1:]
        if is_safe(tolerance_list):
            return True

    return False


total_safe = 0
total_safe_with_tolerance = 0
with open("input.txt") as f:
    for line in f:
        report = line.split(" ")
        if is_safe(report):
            total_safe += 1
        if is_tolerance_safe(report):
            total_safe_with_tolerance += 1

print("Answer one: " + str(total_safe))
print("Answer two: " + str(total_safe_with_tolerance))





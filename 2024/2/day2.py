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
        if (distance == 0
            or abs(distance) > 3
            or last_distance < 0 < distance
            or distance < 0 < last_distance):
            return False

        last_value = value
        last_distance = distance

    return True

total_safe = 0
with open("input.txt") as f:
    for line in f:
        report = line.split(" ")
        if is_safe(report):
            total_safe += 1

print("Answer one: " + str(total_safe))





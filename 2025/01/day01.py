password = 0
dial_position = 50

with open("input.txt", "r") as f:
    for line in f:
        direction = line[0]
        distance = int(line[1:])

        if abs(distance > 100):
            password += abs(distance) // 100
            distance = distance % 100

        if direction == "L":
            new_position = dial_position - distance
            if new_position < 0 and dial_position != 0:
                password += 1
            dial_position = (dial_position - distance) % 100
        else:
            new_position = dial_position + distance
            if new_position > 100 and dial_position != 0:
                password += 1
            dial_position = (dial_position + distance) % 100

        if dial_position == 0:
            password += 1

print(password)
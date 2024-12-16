f = open("input.txt")

l1 = []
l2 = []

for line in f:
    s = line.split("   ")
    l1.append(int(s[0]))
    l2.append(int(s[1]))

l1.sort()
l2.sort()

total = 0
for i in range(len(l1)):
    total += abs(l1[i] - l2[i])

print(total)

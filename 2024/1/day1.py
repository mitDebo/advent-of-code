f = open("input.txt")

l1 = []
l2 = []
occur = {}

for line in f:
    s = line.split("   ")
    i1 = int(s[0])
    i2 = int(s[1])

    l1.append(i1)
    l2.append(i2)
    if i2 not in occur:
        occur[i2] = 0
    occur[i2] += 1

l1.sort()
l2.sort()

distanceTotal = 0
dupeTotal = 0
for i in range(len(l1)):
    distanceTotal += abs(l1[i] - l2[i])
    if l1[i] in occur:
        dupeTotal += l1[i] * occur[l1[i]]

print("Answer one: " + str(distanceTotal))
print("Answer two: " + str(dupeTotal))

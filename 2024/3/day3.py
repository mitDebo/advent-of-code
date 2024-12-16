import re

regex = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
stripping_regex = re.compile(r"don't\(\).*?(do\(\)|$)")
total = 0
stripped_total = 0

with open('input.txt') as f:
    contents = f.read()

instructions = regex.finditer(contents)
for i in instructions:
    total += int(i.group(1)) * int(i.group(2))

stripped_contents = stripping_regex.sub('', contents.replace('\n', ''))

instructions = regex.finditer(stripped_contents)
for i in instructions:
    stripped_total += int(i.group(1)) * int(i.group(2))

print("Answer one: " + str(total))
print("Answer two: " + str(stripped_total))

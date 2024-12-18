from itertools import product

two_ops_total = 0
three_ops_total = 0

with open("input.txt") as f:
    lines = f.read().strip().split("\n")

for line in lines:
    values = line.split()
    answer = int(values[0][:-1])
    nums = list(map(int, values[1:]))

    def evaluate(operations:tuple) -> int:
        t = nums[0]
        for i, op in enumerate(operations):
            if op == "+":
                t += nums[i + 1]
            elif op =="*":
                t *= nums[i + 1]
            elif op == "|":
                t = int(str(t) + str(nums[i + 1]))

        return t

    for op_str in product("+*", repeat=len(nums) - 1):
        if evaluate(op_str) == answer:
            two_ops_total += answer
            break

    for op_str in product("+*|", repeat=len(nums) - 1):
        if evaluate(op_str) == answer:
            print(f"WORKED! {answer} = {op_str}")
            three_ops_total += answer
            break

print("Answer one: {}".format(two_ops_total))
print("Answer two: {}".format(three_ops_total))

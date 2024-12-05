import re

with open("./day3/input.txt") as f:
    text = f.read()
    matches = re.findall(r"mul\(\-?\d+,\-?\d+\)|do\(\)|don't\(\)", text)
    sum = 0
    enabled = True

    for item in matches:
        if item == "don't()":
            enabled = False
        elif item == "do()":
            enabled = True
        elif enabled:
            nums = [int(n) for n in re.findall(r"(\-?\d+)", item)]
            sum += nums[0] * nums[1]

    print(sum)

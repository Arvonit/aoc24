import re

with open("./day3/input.txt") as f:
    text = f.read()
    matches = re.findall(r"mul\((-?\d+),(-?\d+)\)", text)
    sum = 0

    for pair in matches:
        prod = int(pair[0]) * int(pair[1])
        sum += prod

    print(sum)

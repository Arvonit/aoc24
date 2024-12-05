l_nums = []
r_nums = []

with open("./day1/input.txt") as f:
    for line in f:
        nums = line.split("   ")
        l_nums.append(int(nums[0]))
        r_nums.append(int(nums[1]))

l_nums.sort()
r_nums.sort()
distance = 0

for i in range(len(l_nums)):
    diff = abs(l_nums[i] - r_nums[i])
    distance += diff

print(distance)

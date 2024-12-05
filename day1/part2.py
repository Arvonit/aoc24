l_nums = []
r_nums = []

with open("./day1/input.txt") as f:
    for line in f:
        nums = line.split("   ")
        l_nums.append(int(nums[0]))
        r_nums.append(int(nums[1]))


similarity_score = 0

for num in l_nums:
    score = num * r_nums.count(num)
    similarity_score += score

print(similarity_score)

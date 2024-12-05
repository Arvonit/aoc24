def polarity(num: int) -> int:
    if num == 0:
        return 0
    elif num < 0:
        return -1
    else:
        return 1


num_safe = 0

with open("./day2/input.txt") as f:
    for level in f:
        reports = level.split(" ")
        differences = []
        safe = True

        for i in range(1, len(reports)):
            left, right = int(reports[i - 1]), int(reports[i])
            diff = right - left

            if abs(diff) < 1 or abs(diff) > 3:
                safe = False
                break

            if len(differences) > 0 and polarity(diff) != polarity(differences[-1]):
                safe = False
                break

            differences.append(diff)

        if safe:
            num_safe += 1


print(num_safe)

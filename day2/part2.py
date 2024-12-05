def polarity(num: int) -> int:
    if num == 0:
        return 0
    elif num < 0:
        return -1
    else:
        return 1


def check_safety(levels: list[int]) -> bool:
    differences = []

    for i in range(1, len(levels)):
        left, right = int(levels[i - 1]), int(levels[i])
        diff = right - left

        if abs(diff) < 1 or abs(diff) > 3:
            return False

        if len(differences) > 0 and polarity(diff) != polarity(differences[-1]):
            return False

        differences.append(diff)

    return True


num_safe = 0

with open("./day2/input.txt") as f:
    for report in f:
        levels = [int(item) for item in report.split(" ")]

        if check_safety(levels):
            num_safe += 1
            continue

        # Pop a level from the list until it becomes safe, if possible
        for i in range(len(levels)):
            mod_levels = list(levels)
            mod_levels.pop(i)

            if check_safety(mod_levels):
                num_safe += 1
                break

print(num_safe)

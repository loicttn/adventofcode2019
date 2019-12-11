def step1(inp: int) -> int:
    res = str(inp)
    if len(res) != 6:
        return 0
    double = 0
    for i in range(len(res)):
        if i + 1 < len(res) and int(str(res[i])) == int(str(res[i+1])):
            double += 1
        if i + 1 < len(res) and int(str(res[i])) > int(str(res[i+1])):
            return 0
    return 1 if double else 0


assert step1(111111) == 1
assert step1(223450) == 0
assert step1(123789) == 0
res = 0
for i in range(137683, 596253):
    res += step1(i)
print("step1 solution is", res)


def step2(inp: int) -> int:
    res = str(inp)
    if len(res) != 6:
        return 0
    double = 0
    for i in range(len(res)):
        if i + 1 < len(res) and int(str(res[i])) == int(str(res[i+1])):
            if not (i - 1 >= 0 and int(str(res[i])) == int(str(res[i-1]))):
                if not (i + 2 < len(res) and int(str(res[i])) == int(str(res[i+2]))):
                    double += 1
        if i + 1 < len(res) and int(str(res[i])) > int(str(res[i+1])):
            return 0
    return 1 if double > 0 else 0


assert step2(222333) == 0
assert step2(123444) == 0
assert step2(111122) == 1
res = 0
for i in range(137683, 596253):
    res += step2(i)
print("step2 solution is", res)

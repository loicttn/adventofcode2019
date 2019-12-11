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

x=0
for j in range(137683,596253):l=[-1]+[int(i)for i in str(j)]+[10];d=lambda i:l[i-1]!=l[i+1]and l[i]==l[i+1]and l[i]!=l[i+2];x+=any([d(i) for i in range(1,7)]) and l==sorted(l)
print(x)

x=0
for j in range(137683,596253):l=[-1]+[int(i)for i in str(j)]+[10];x+=any([l[i]==l[i+1]and l[i]not in [l[i-1],l[i+2]]for i in range(1,7)])and l==sorted(l)
print(x)
exit(0)

assert step2_golf("222333") == 0
assert step2_golf("123444") == 0
assert step2_golf("111122") == 1
res = 0
res2 = 0
for i in range(137683, 596253):
    res += step2(i)
    x = step2_golf(i)
    res2 += x

print("step2 solution is", res)
print("=>", res2)

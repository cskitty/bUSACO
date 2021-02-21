t = int(input())


def count(x, s):
    c = 0
    for y in s:
        if y == x:
            c += 1
    return c


def cost(one, zero, s):
    c = 0
    for x in s:
        if x == "0":
            c += zero
        else:
            c = one

    return c


for x in range(t):
    n, c0, c1, h = tuple(map(int, input().split()))
    s = input()
    count0 = count(0, s)
    count1 = count(1, s)
    change_cost = abs(c0 - c1)
    m = cost(c0, c1, s)
    if count0 > count1:
        s.replace("1", "0")
        m = min(m, cost(c0, c1, s) + h * count1)

    else:
        s.replace("0", "1")
        m = min(m, cost(c0, c1, s) + h * count0)

    print(m)
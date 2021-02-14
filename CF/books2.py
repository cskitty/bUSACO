n, t = list(map(int, input().split()))
a = list(map(int, input().split()))

p0 = 1
p1 = 0
ans = 0

while p0 < n:
    sum = a[p0]
    curAns = 0
    while p1 < n:
        sum += a[p1]
        if sum > t:
            break

        p1 += 1
        curAns += 1

    ans = max(curAns, ans)
    p0 += 1

print(ans)
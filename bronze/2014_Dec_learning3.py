import bisect

fIn, fOut = open("learning.in"), open("learning.out", "w")

INF = int(1e10)
N, A, B = map(int, fIn.readline().split())
cows = []
cowWeights = []
count = 0
for _ in range(N):
    f = fIn.readline().split()
    cows.append([f[0], int(f[1])])
    cowWeights.append(int(f[1]))

cows.append(("NS", INF))
cows = [("NS", -INF)] + cows

cows = sorted(cows, key=lambda x: int(x[1]))

for i in range(len(cows) - 1):
    s = cows[i][1]
    e = cows[i + 1][1]
    m = (s + e) // 2

    if cows[i][0] == "S":
        s = max(A, s + 1)
        m = min(B, m)
        if m - s + 1 >= 0:
            count += m - s + 1

    e = cows[i + 1][1]
    s = cows[i][1]
    m = (s + e) // 2

    if cows[i + 1][0] == "S":
        m = max(A, m + 1)
        e = min(B, e)
        if e - m >= 0:
            count += e - m + 1

    if (cows[i + 1][0] == "S" and cows[i][0] == "NS") and (e - s) % 2 == 0 and A <= m <= B:
        count += 1

    print(count, cows[i], cows[i + 1], s, m, e)
fOut.write(str(count))

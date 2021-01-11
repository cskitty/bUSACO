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
    if f[0] == "S":
        count += 1

cowWeights.append(INF)
cowWeights = [-INF] + cowWeights

cowWeights.sort()
cows.append(("NS", INF))
cows = [("NS", -INF)] + cows

cows = sorted(cows, key=lambda x: int(x[1]))

bA = bisect.bisect_left(cowWeights, A)
bB = bisect.bisect_left(cowWeights, B)


if cows[bA][1] == A:
    bA += 1

if (cows[bA][1] + cows[bA + 1][1]) // 2 <= A:
    count += cows[bA][1] - A
else:
    if (cows[bA + 1][1] - cows[bA][1]) % 2 == 0:
        if cows[bA + 1][0] == "S":
            count += cows[bA + 1][1] - (cows[bA][1] + cows[bA + 1][1]) // 2

        if cows[bA][0] == "S":
            count += A - (cows[bA + 1][1] - (cows[bA][1] + cows[bA + 1][1]) // 2)

    else:
        if

if cows[bB][1] == B:
    bB -= 1

count += cows[bA][1] - A
count += B - cows[bB][1]


if bA == bB:

for i in range(bA + 1, bB):
    if (cows[i][1] - cows[i + 1][1]) % 2 == 0:
        if cows[i][0] == "S" and cows[i + 1][0] == "NS":
            count += (cows[i + 1][1] - cows[i][1] + 1) // 2 - 1

        if cows[i + 1][0] == "S" and cows[i][0] == "NS":
            count += (cows[i + 1][1] - cows[i][1] + 1) // 2 - 1

        if cows[i][0] == "S" and cows[i + 1][0] == "S":
            count += cows[i + 1][1] - cows[i][1] + 1



    else:
        if cows[i][0] == "S":
            count += (cows[i + 1][1] - cows[i][1] + 1) // 2

        if cows[i + 1][0] == "S":
            count += (cows[i + 1][1] - cows[i][1] + 1) // 2
    print(cows[i], cows[i + 1], count)

fOut.write(str(count))

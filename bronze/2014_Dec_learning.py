fIn, fOut = open("learning.in"), open("learning.out", "w")

N, A, B = map(int, fIn.readline().split())
cows = []
count = 0
for _ in range(N):
    f = fIn.readline().split()
    cows.append([f[0], int(f[1])])
    if f[0] == "S":
        count += 1

cows = sorted(cows, key=lambda x: int(x[1]))

print(count)

if cows[0][1] > A and cows[0][0] == "S":
    count += cows[0][1] - A

if cows[-1][1] < B and cows[-1][0] == "S":
    count += B - cows[0][1]

for i in range(N - 1):
    if (cows[i][1] - cows[i + 1][1]) % 2 == 1:
        if cows[i][0] == "S" and cows[i + 1][0] == "NS":
            count += (cows[i + 1][1] - cows[i][1] + 1) // 2 - 1

        if cows[i + 1][0] == "S" and cows[i][0] == "NS":
            count += (cows[i + 1][1] - cows[i][1] + 1) // 2 - 1

        if cows[i][0] == "S" and cows[i + 1][0] == "S":
            count += cows[i + 1][1] - cows[i][1] - 1

    else:
        if cows[i][0] == "S":
            count += (cows[i + 1][1] - cows[i][1] + 1) // 2

        if cows[i + 1][0] == "S":
            count += (cows[i + 1][1] - cows[i][1] + 1) // 2
    print(cows[i], cows[i + 1], count)

fOut.write(str(count))

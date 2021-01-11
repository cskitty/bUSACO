fIn, fOut = open("baseball.in"), open("baseball.out", "w")
N = int(fIn.readline())

cows = sorted([int(fIn.readline()) for x in range(N)])

count = 0
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if 2 * (cows[j] - cows[i]) >= cows[k] - cows[j] >= cows[j] - cows[i]:
                count += 1

fOut.write(str(count))
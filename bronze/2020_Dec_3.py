N = int(input())
cows = {}
myMax = 1000

for x in range(N):
    f = input().split()

    cows[x] = f
    cows[x][1] = int(cows[x][1])
    cows[x][2] = int(cows[x][2])

grass = [[myMax + 1 for x in range(myMax)] for y in range(myMax)]
for k in cows:
    grass[cows[k][1]][cows[k][2]] = 0

out = [0] * N
for time in range(1, myMax + 1):
    for k in cows:
        if out[k] != 0:
            continue

        if cows[k][0] == "E":
            cows[k][1] += 1
        else:
            cows[k][2] += 1


        if cows[k][1] >= myMax or cows[k][2] >= myMax:
            out[k] = "Infinity"
        elif grass[cows[k][1]][cows[k][2]] < time:
            out[k] = time
        else:
            grass[cows[k][1]][cows[k][2]] = time

for o in out:
    print(o)
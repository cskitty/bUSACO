fin, fout = open("relay.in"), open("relay.out", "w")

N = int(fin.readline())
cows = {}
for x in range(1, 1 + N):
    cows[x] = int(fin.readline())

count = 0
for cow in range(1, 1 + N):
    curCow = cows[cow]
    cowsGoneThrough = set()
    cowsGoneThrough.add(cow)
    if curCow == 0:
        count += 1
        print(cow)
        continue

    while curCow not in cowsGoneThrough:
        cowsGoneThrough.add(curCow)
        if curCow == 0:
            count += 1
            break
        curCow = cows[curCow]

        if len(cowsGoneThrough) >= N + 1:
            count += 1

            break

fout.write(str(count))
N = int(input())

North = []
East  = []
id    = 0
INF   = 1000000001

cowpos = [(0, 0)] * N
for i in range(N):
    d, x, y = input().split()

    x = int(x)
    y = int(y)

    if d == 'N':
        North.append((x, y, id))
    else:
        East.append((x, y, id))
    cowpos[id] = (x, y)
    id += 1

meetTime = []
for nCow in North:
    for eCow in East:
        yTime = eCow[1] - nCow[1]
        xTime = nCow[0] - eCow[0]

        if (xTime == yTime):
            continue

        if yTime > xTime and xTime > 0:
            meetTime.append((yTime, nCow[2], eCow[2], 0))
        elif yTime < xTime and yTime > 0:
            meetTime.append((xTime, eCow[2], nCow[2], 1))

#print(meetTime)
meetTime.sort()
#print(meetTime)

ans = [INF] * N
stopped = set()
for mt in meetTime:
    #if not mt[2] in stopped and not mt[1] in stopped:
    if ans[mt[2]] == INF and ans[mt[1]] == INF:
        ans[mt[1]] = mt[0]
        #stopped.add(mt[1])
        continue

    if ans[mt[1]] == INF:
        if mt[3]:
            #east

            start2 = cowpos[mt[2]][1]
            end2 = start2 + ans[mt[2]]

            if (cowpos[mt[1]][1] >= start2 and cowpos[mt[1]][1] <= end2):
                ans[mt[1]] = mt[0]
        else:
            #north
            start2 = cowpos[mt[2]][0]
            end2 = start2 + ans[mt[2]]

            if (cowpos[mt[1]][0] >= start2 and cowpos[mt[1]][0] <= end2):
                ans[mt[1]] = mt[0]

for i in range(N):
    if ans[i]  == INF:
        print("Infinity")
    else:
        print(ans[i])
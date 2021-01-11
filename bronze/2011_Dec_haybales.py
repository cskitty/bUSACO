fIn, fOut = open("haybales.in"), open("haybales.out", "w")
N = int(fIn.readline())
hayBales = [int(fIn.readline()) for _ in range(N)]
height = sum(hayBales) // N
pos = []
neg = []

for hayBale in hayBales:
    if hayBale - height > 0:
        pos.append(hayBale - height)
    else:
        neg.append(hayBale - height)

nIdx = 0
pIdx = 0
moved = 0

while pIdx < len(pos) and nIdx < len(neg):
    if pos[pIdx] + neg[nIdx] < 0:
        neg[nIdx] += pos[pIdx]
        moved += pos[pIdx]
        pos[pIdx] = 0

        pIdx += 1
    else:
        pos[pIdx] += neg[nIdx]
        moved -= neg[nIdx]
        neg[nIdx] = 0
        nIdx += 1

fOut.write(str(moved) + '\n')
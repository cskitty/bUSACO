fIn, fOut = open("records.in"), open("records.out", "w")
N = int(fIn.readline())
records = []

for x in range(N):
    records.append(tuple(sorted(fIn.readline().split())))

d = {}

for record in records:
    try:
        d[record] += 1

    except:
        d[record] = 1

fOut.write(str(max(sorted(d.values()))))

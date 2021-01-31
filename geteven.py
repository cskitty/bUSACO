fin, fout = open('geteven.in'), open("geteven.out", "w")
N = int(fin.readline())
values = {}
for x in range(N):
    f = fin.readline().split()
    try:
        values[f[0]].append(int(f[1]))
    except:
        values[f[0]] = [int(f[1])]

c = {}
for val in values:
    c[val] = len(values[val])

count = 0
for b in values["B"]:
    for i in values["I"]:
        if (b + i) % 2 == 0:
            count += c["G"] * c["O"] * c["M"] * c["S"] * c["E"]
        else:
            for g in values["G"]:
                for o in values["O"]:
                    for e in values["E"]:
                        for s in values["S"]:
                            if (g + o + e + s) % 2 == 0:
                                count += c["M"]
                            else:
                                for m in values["M"]:
                                    if m % 2 == 0:
                                        count += 1
fout.write(str(count))

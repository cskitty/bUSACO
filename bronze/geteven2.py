fin, fout = open('geteven.in'), open("geteven.out", "w")
N = int(fin.readline())
values = {}
for x in range(N):
    f = fin.readline().split()
    try:
        values[f[0]][int(f[1]) % 2] += 1
    except:
        values[f[0]] = [0, 0]
        values[f[0]][int(f[1]) % 2] += 1
count = 0

for b in range(2):
    for e in range(2):
        for s in range(2):
            for i in range(2):
                for g in range(2):
                    for o in range(2):
                        for m in range(2):
                            if ((b + i) * (g + o + e + s) * m) % 2 == 0:
                                count += values["B"][b] * values["E"][e] * values["S"][s] * \
                                         values["I"][i] * values["G"][g] * values["O"][o] * \
                                         values["M"][m]


fout.write(str(count))

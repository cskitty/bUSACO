fin, fout = open("stacking.in"), open("stacking.out", "w")
N, K = tuple(map(int, fin.readline().split()))
haybales = []

for _ in range(K):
    f = tuple(map(int, fin.readline().split()))
    haybales += list(range(f[0], f[1] + 1))

#stacks = [0] * N
for hb in haybales:
    stacks[hb - 1] += 1

stacks.sort()
fout.write(str(stacks[N // 2]) + "\n")

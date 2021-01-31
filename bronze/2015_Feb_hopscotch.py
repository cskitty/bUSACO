fin, fout = open("hopscotch.in"), open("hopscotch.out", "w")

Y, X = tuple(map(int, fin.readline().split()))

dp = [[0 for x in range(X)] for y in range(Y)]
dp[0][0] = 1

colors = []
for _ in range(Y):
    colors.append(fin.readline().strip())

for x in range(X):
    for y in range(Y):
        for v in range(y + 1, Y):
            for u in range(x + 1, X):
                if colors[y][x] != colors[v][u]:
                    dp[v][u] += dp[y][x]


fout.write(str(dp[-1][-1]))
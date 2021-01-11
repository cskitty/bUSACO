fout, fin = open("planting.out", "w"), open("planting.in")

N = int(fin.readline())
adj = {}
paths = [tuple(map(int, fin.readline().split())) for _ in range(N - 1)]

for path in paths:
    try:
        adj[path[0]].append(path[1])
    except:
        adj[path[0]] = [path[1]]

    try:
        adj[path[1]].append(path[0])
    except:
        adj[path[1]] = [path[0]]

ans = 0
for n in adj:
    ans = max(ans, len(adj[n]))

fout.write(str(ans + 1))
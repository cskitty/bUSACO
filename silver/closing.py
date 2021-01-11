fin, fout = open("closing.in"), open("closing.out", "w")
N, M = list(map(int, fin.readline().split()))

paths = [tuple(map(int, fin.readline().split())) for _ in range(M)]
order = [int(fin.readline()) for _ in range(N - 1)]
graph = {}
visited = set()

def dfs(node):
    if node in visited:
        return
    visited.add(node)
    #print(node)
    for neighbor in graph[node]:
        dfs(neighbor)


for path in paths:
    try:
        graph[path[0]].add(path[1])
    except:
        graph[path[0]] = {path[1]}

    try:
        graph[path[1]].add(path[0])
    except:
        graph[path[1]] = {path[0]}


if len(visited) == N:
    fout.write("YES\n")
else:
    fout.write("NO\n")

def remove(node):
    for n in graph:
        try:
            graph[n].remove(node)
        except:
            pass

    del graph[node]
    return graph

for i in range(N - 1):
    visited = set()
    dfs(list(graph.keys())[0])
    graph = remove(order[i])
    print("bunny ", i)
    print(graph)
    print(visited)
    if len(visited) == N - i:
        fout.write(str("YES\n"))
    else:
        fout.write(str("NO\n"))
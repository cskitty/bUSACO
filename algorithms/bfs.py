from collections import deque

graph = {}
graph["you"] = ["bob", "claire", "alice"]
graph["claire"] = ["jonny"]
graph["alice"] = ["peggy"]
graph["bob"] = ["anuj", "peggy"]
graph["jonny"] = []
graph["anuj"] = []
graph["peggy"] = []

visited = set()
visited.add("you")

i = 0
q = deque()
q.append("you")

print(q)

while q:
    node = q.popleft()

    for n in graph[node]:
        if n in visited:
            continue
        print(n)
        q.append(n)
        visited.add(n)


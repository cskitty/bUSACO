def cal(cows):
    M, N = 0
    for cow in cows:
        M = max(M, cows[0])
        N = max(N, cow[1])
    farm = [[0] * N] in range(M)
    for i in range(cows.size()):
        farm[cows[i][0]][cows[i][1]] = i
    result = set()
    dirs = [[0, 1], [0, -1], [1, 1], [1, -1], [1, 0], [-1, 0], [-1, -1], [-1, 1]]
    for i in range(len(cows)):
        cow = cows[i]
        subset = set()
        subset.add(i)
        footprint = set()
        x, y = cow[0], cow[1]
        queue = []
        footprint.add((x, y))
        queue.add((x, y))
        result.add((i))

        while (queue):
            for i in range(len(queue)):
                x, y = queue.popleft()
                for dir in dirs:
                    _x = x + dir[0]
                    _y = y + dir[1]
                    if not validate(_x, _y, M, N):
                        continue
                    if (_x, _y) not in footprint:
                        if farm[_x][_y] != 0:
                            subset.add(farm[_x][_y])
                        footprint.add((_x, _y))
                        queue.append((_x, _y))
            result.add(subset.copy())

        return len(result)


def validate(x, y, M, N):
    return x >= 0 and x < M and y >= 0 and y < N
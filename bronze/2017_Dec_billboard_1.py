fIn, fOut = open("billboard.in"), open("billboard.out", "w")

x1, y1, x2, y2 = tuple(map(int, fIn.readline().split()))
x3, y3, x4, y4 = tuple(map(int, fIn.readline().split()))
tx1, ty1, tx2, ty2 = tuple(map(int, fIn.readline().split()))

myMin = min(x1, y1, x2, y2, x3, y3, x4, y4, tx1, ty2, tx2, ty1)
myMax = max(x1, y1, x2, y2, x3, y3, x4, y4, tx1, ty2, tx2, ty1)

matrix = [[0 for x in range(myMin, myMax + 1)] for y in range(myMin, myMax + 1)]

coors = [x1, y1, x2, y2, x3, y3, x4, y4, tx1, ty2, tx2, ty1]
for i in range(12):
    coors[i] -= myMin

print(coors)

for x in range(x1, x2):
    for y in range(y1, y2):
        matrix[x][y] = 1

for x in range(x3, x4):
    for y in range(y3, y4):
        matrix[x][y] = 1

for x in range(tx1, tx2):
    for y in range(ty1, ty2):
        matrix[x][y] = 0

count = 0
for x in matrix:
    for y in x:
        if y == 1:
            count += 1

fOut.write(str(count))
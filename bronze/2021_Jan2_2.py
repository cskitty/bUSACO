N = input()
s = input().split()
evenCount = 0
oddCount = 0
for x in s:
    if int(x) % 2 == 0:
        evenCount += 1
    else:
        oddCount += 1

if evenCount == oddCount or evenCount == 1 + oddCount:


N = int(input())
A = list(map(int, input().split()))

ans = 0
for i in range(N):
    for j in range(i+1):
       mySet = set()
       sum = 0
       for k in range(j, i+1):
         sum += A[k]
         mySet.add(A[k])
       #print(sum, mySet, i, j, (i-j+1))
       count = (i-j+1)
       if (sum % count == 0) and (sum // count) in mySet:
         ans += 1

print(ans)


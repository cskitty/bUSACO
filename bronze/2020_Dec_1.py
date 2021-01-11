A = list(map(int, input().split()))
A.sort()

if (A[0] + A[1] == A[2]):
    print(str(A[0]) + ' ' + str(A[1]) + ' ' + str(A[3]))
else:
    print(str(A[0]) + ' ' + str(A[1]) + ' ' + str(A[2]))
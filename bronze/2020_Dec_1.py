N = list(map(int, input().split()))
N.sort()

aPbPc = N[-1]
a = N[0]
b = N[1]
print(a, b, end=" ")

# N[0] is A
# N[1] is B
n2 = a + b # Always true

print(aPbPc - n2)
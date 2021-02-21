N = input()
s = input().split()
oddC = 0
evenC = 0
for cow in s:
    if int(cow) % 2 == 0:
        evenC += 1
    else:
        oddC += 1

# recursive function, assuming O >= E
def group(O, E):
    dif = O - E
    if dif == 0:
        return O + E
    elif dif == 1:
        return O + E - 2
    elif dif == 2:
        return E + O - 1
    else:
        O -= 2
        E += 1
        return group(O, E)

if evenC > oddC:
    print(2 * oddC + 1)
else:
    print(group(oddC, evenC))
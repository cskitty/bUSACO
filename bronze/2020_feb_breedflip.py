fin, fout = open('breedflip.in'), open('breedflip.out', 'w')

n = int(fin.readline())

a = fin.readline()
b = fin.readline()

s = []
for x in range(n):
    if a[x] != b[x]:
        s.append(1)
    else:
        s.append(0)

def count(x,s):
    count = 0
    for f in range(len(s) - 1):
        if s[f] == int(x[0]) and s[f+ 1] == int(x[1]):
            count += 1

    return count

s = [0] + s + [0]
fout.write(str((count('01', s) + count('10', s))//2))
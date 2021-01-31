alphabet = input()
s = input()
curLeI = 0
ans = 1
times = alphabet * 1
found = times.find(s[curLeI])
while curLeI < len(s):
    times = times[found + 1:]
    found = times.find(s[curLeI])

    if found == -1:
        times += alphabet
        ans += 1
    else:
        curLeI += 1

print(ans - 1)

"""
SAMPLE INPUT:
opqrstuvwxyzabcdefghijklmnopqrstuvwxyz
mood
SAMPLE OUTPUT:
3
"""
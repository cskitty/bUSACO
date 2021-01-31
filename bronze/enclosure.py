expr = input().split()

bl = 0
br = 0
pl = 0
pr = 0

for x in expr:
    if x in {"[", "]", "(", ")"}:

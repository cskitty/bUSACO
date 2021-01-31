expr = input().split()

brCount = 0
blCount = 0

prCount = 0
plCount = 0

missing = ""
for x in expr:
    if x == "[":
        blCount += 1
    elif x == "]":
        brCount += 1
    elif x == "(":
        blCount += 1
    elif x == ")":
        brCount += 1

if blCount > brCount:
    missing = "]"
if blCount < brCount:
    missing = "["
if prCount < plCount:
    missing = ")"
if plCount > prCount:
    missing = "("

opp = {"[":"]", "]":"[", "(":")", ")":"("}

stack = []

if missing == ")" or missing == "]":
    for x in expr:
        if x in {"]", "[", ")", "("}:
            if len(stack) == 0:
                stack.append(x)
            elif stack[-1] == opp[x]:
                stack.pop(-1)

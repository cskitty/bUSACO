N = int(input())
skills = list(map(int, input().split()))
ans = 0
skills.sort()
for i in range(0,N - 1, 2):
    ans += skills[i + 1] - skills[i]

print(ans)
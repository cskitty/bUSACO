N = int(input())
flowers = list(map(int, input().split()))

count = 0
for i in range(N):
    for j in range(i, N):
        working = False
        average = sum(flowers[i:j + 1]) / (j - i + 1)

        for flower in flowers[i:j + 1]:
            if flower == average:
                working = True

        if working:
            count += 1

print(count)
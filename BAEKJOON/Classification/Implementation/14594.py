n = int(input())
m = int(input())

wall = [1] * (n + 1)
for i in range(m):
    x, y = map(int, input().split())
    for j in range(x, y):
        if j == 0 or j == n + 1:
            continue
        wall[j] = 0

print(wall.count(1) - 1)

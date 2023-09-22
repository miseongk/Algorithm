n, m = map(int, input().split())

flower = [[-1] * (m + 1) for _ in range(n + 1)]

left = list(map(int, input().split()))
for i in range(1, n + 1):
    flower[i][0] = left[i - 1]

up = list(map(int, input().split()))
for i in range(1, m + 1):
    flower[0][i] = up[i - 1]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if flower[i - 1][j] == flower[i][j - 1]:
            flower[i][j] = 0
        else:
            flower[i][j] = 1

print(flower[n][m])

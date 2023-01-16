import sys
input = sys.stdin.readline
n, m = map(int, input().split())

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

sum = [[0 for _ in range(m+1)] for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, m+1):
        sum[i][j] = arr[i-1][j-1] + sum[i-1][j] + sum[i][j-1] - sum[i-1][j-1]

max_sum = -10000 * 200 * 200
for x1 in range(n):
    for y1 in range(m):
        for x2 in range(x1, n):
            for y2 in range(y1, m):
                s = sum[x2+1][y2+1] - sum[x1][y2+1] - sum[x2+1][y1] + sum[x1][y1]
                max_sum = max(max_sum, s)

print(max_sum)
import sys

input = sys.stdin.readline
n = int(input())
matrix = []
visited = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))
    visited.append(list([0, 0] for _ in range(n))) # [depth, cnt]

if matrix[0][0] < n:
    visited[matrix[0][0]][0][0] += 1
    visited[matrix[0][0]][0][1] += 1
    visited[0][matrix[0][0]][0] += 1
    visited[0][matrix[0][0]][1] += 1

cnt = 0
for i in range(n):
    for j in range(n):
        if visited[i][j][0] != 0:
            if matrix[i][j] + i == n-1 and j == n-1:
                cnt += visited[i][j][1]
                continue
            if matrix[i][j] + j == n-1 and i == n-1:
                cnt += visited[i][j][1]
                continue
            if matrix[i][j] + i <= n-1:
                visited[matrix[i][j] + i][j][0] += 1
                visited[matrix[i][j] + i][j][1] += visited[i][j][1]
            if matrix[i][j] + j <= n-1:
                visited[i][matrix[i][j] + j][0] += 1
                visited[i][matrix[i][j] + j][1] += visited[i][j][1]
        else:
            continue

print(cnt)

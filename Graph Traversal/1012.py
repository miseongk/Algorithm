import sys
sys.setrecursionlimit(10 ** 4)


def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if matrix[x][y] == 1:
        matrix[x][y] = 0

        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False


T = int(input())
result = [0] * T
for i in range(T):
    n, m, k = map(int, input().split())
    matrix = [[0] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        matrix[x][y] = 1
    for j in range(n):
        for h in range(m):
            if dfs(j, h):
                result[i] += 1
for i in range(T):
    print(result[i])

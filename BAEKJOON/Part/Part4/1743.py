from collections import deque

n, m, k = map(int, input().split())
graph = [[0] * m for _ in range(n)]

for i in range(k):
    x, y = map(int, input().split())
    graph[x-1][y-1] = 1

queue = deque()
def bfs(x, y):
    cnt = 0
    if graph[x][y] == 0:
        return 0
    queue.append((x, y))
    while queue:
        a, b = queue.popleft()
        graph[a][b] = 0
        cnt += 1
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            graph[nx][ny] = 0
            queue.append((nx, ny))
    return cnt


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
max = 0
for i in range(n):
    for j in range(m):
        cnt = bfs(i, j)
        if cnt > max:
            max = cnt

print(max)
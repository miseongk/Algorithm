from collections import deque

m, n = map(int, input().split())
tomato = [list(map(int,input().split())) for _ in range(n)]

q = deque()
cnt = 0
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            q.append((i, j, 0))
        elif tomato[i][j] == 0:
            cnt += 1

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

while q:
    x, y, time = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue

        if tomato[nx][ny] == 0:
            tomato[nx][ny] = 1
            cnt -= 1
            q.append((nx, ny, time + 1))

if cnt > 0:
    print(-1)
else:
    print(time)
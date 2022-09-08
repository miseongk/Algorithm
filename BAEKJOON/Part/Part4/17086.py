import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
visited = []
for i in range(n):
    visited.append(list(map(int, input().split())))

queue = deque()
def bfs(i, j):
    queue.append((i, j, visited[i][j]))
    while queue:
        x, y, num = queue.popleft()
        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                if visited[nx][ny] == 0:
                    visited[nx][ny] = num + 1
                else:
                    if visited[nx][ny] > num + 1:
                        visited[nx][ny] = num + 1
                    else:
                        continue
                queue.append((nx, ny, visited[nx][ny]))

dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0 , -1, 1, -1, 1, 1, -1]

for i in range(n):
    for j in range(m):
        if visited[i][j] == 1:
            bfs(i, j);
max = 0
for i in range(n):
    for j in range(m):
        if max < visited[i][j]:
            max = visited[i][j]

print(max - 1)

# [참고]⭐️
# 나는 상어 한마리를 기준으로 거리를 다 계산하고 다음 상어를 또 기준으로 거리를 수정하는 방식으로 함 -> 비효율적
# 상어가 있는 곳을 기준으로 "동시에" 방문하면 한번에 구할 수 있음!!!
# import sys

# input = sys.stdin.readline
# n, m = map(int, input().split())
# visited = []
# for i in range(n):
#     visited.append(list(map(int, input().split())))

# def bfs(sharks):
#     global max
#     max = 0
#     queue = sharks
#     while queue:
#         x, y, num = queue.pop(0)
#         for k in range(8):
#             nx = x + dx[k]
#             ny = y + dy[k]
#             if nx >= 0 and nx < n and ny >= 0 and ny < m:
#                 if visited[nx][ny] == 0:
#                     visited[nx][ny] = num + 1
#                     queue.append((nx, ny, visited[nx][ny]))

#                     if max < num + 1:
#                         max = num + 1

# dx = [-1, 1, 0, 0, -1, 1, -1, 1]
# dy = [0, 0 , -1, 1, -1, 1, 1, -1]

# sharks = []
# for i in range(n):
#     for j in range(m):
#         if visited[i][j] == 1:
#             sharks.append((i, j, visited[i][j]))
# bfs(sharks)
# print(max - 1)
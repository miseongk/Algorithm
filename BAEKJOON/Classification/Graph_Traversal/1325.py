import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v2].append(v1)

def bfs(graph, visited, start):
    visited[start] = True
    queue = deque([start])
    cnt = 0
    while queue:
        v = queue.popleft()
        cnt += 1
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
    return cnt

max_cnt = 0
max_idx = []
for start in range(1, n+1):
    visited = [False] * (n+1)
    if len(graph[start]) == 0:
        continue
    cnt = bfs(graph, visited, start)
    if cnt > max_cnt:
        max_cnt = cnt
        max_idx = [start]
    elif cnt == max_cnt:
        max_cnt = cnt
        max_idx.append(start)

for i in max_idx:
    print(i, end=' ')

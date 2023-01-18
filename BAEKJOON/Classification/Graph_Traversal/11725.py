import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
for i in range(n-1):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

parent = [0] * (n+1)
visited = [False] * (n+1)

queue = deque([1])
visited[1] = True
while queue:
    v = queue.popleft()
    for i in graph[v]:
        if not visited[i]:
            queue.append(i)
            parent[i] = v
            visited[i] = True

for i in parent[2:]:
    print(i)

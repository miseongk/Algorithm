import sys
sys.setrecursionlimit(10000)

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)

def dfs(graph, visited, start):
    visited[start] = True

    for i in graph[start]:
        if visited[i] == False:
            dfs(graph, visited, i)

cnt = 0
for i in range(1, n+1):
    if visited[i] == False:
        dfs(graph, visited, i)
        cnt += 1

print(cnt)
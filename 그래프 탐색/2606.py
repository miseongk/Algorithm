def dfs(v):
    global result
    visited[v] = True
    result += 1
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

n = int(input())
m = int(input())
visited = [False] * (n+1)
graph = [[] for _ in range(n+1)]
result = 0

for _ in range(m):
    tmp = list(map(int, input().split()))
    graph[tmp[0]].append(tmp[1])
    graph[tmp[1]].append(tmp[0])

for g in graph:
    g.sort()

dfs(1)
print(result - 1)
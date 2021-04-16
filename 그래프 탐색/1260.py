from collections import deque

def dfs(v):
    visited[v] = True
    print(v, end=' ')
    for i in range(n+1):
        if G[v][i] == 1 and not visited[i]:
            dfs(i)

def bfs(v):
    queue = deque([v])
    visited[v] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in range(n+1):
            if G[v][i] == 1 and not visited[i]:
                queue.append(i)
                visited[i] = True

n, m, v = map(int, input().split())
visited = [False] * (n+1)
G = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(m):
    tmp = list(map(int, input().split()))
    G[tmp[0]][tmp[1]] = 1
    G[tmp[1]][tmp[0]] = 1

dfs(v)
visited = [False] * (n+1)
print(sep='\n')
bfs(v)
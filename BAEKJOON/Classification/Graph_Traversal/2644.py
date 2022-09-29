from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
x, y = map(int, input().split())
m = int(input())
relation =[[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    relation[a].append(b)
    relation[b].append(a)

visited = [0] * (n+1)

def bfs(q, y):
    while q:
        cur, rel = q.popleft()
        if cur == y:
            return rel
        for i in relation[cur]:
            if visited[i]  == 0:
                q.append((i, rel + 1))
                visited[i] = 1
    
    return -1

q = deque()
q.append((x, 0))
visited[x] == 1
print(bfs(q, y))

from collections import deque

f, s, g, u, d = map(int, input().split())

visited = [0] * 1000001
q = deque()
q.append((s, 0))
visited[s] = 1

if s == g:
    print(0)
    exit(0)

while q:
    cur, cnt = q.popleft()
    if cur - d == g or cur + u == g:
        print(cnt+1)
        exit(0)
    if cur - d >= 1 and visited[cur-d] == 0:
        q.append((cur-d, cnt+1))
        visited[cur-d] = 1
    if cur + u <= f and visited[cur+u] == 0:
        q.append((cur+u, cnt+1))
        visited[cur+u] = 1

print("use the stairs")
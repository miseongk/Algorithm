from collections import deque

n, k = map(int, input().split())
if n >= k:
    print(n-k)
    exit(0)

visited = [0] * 200001

q = deque()
q.append((n, 1))
visited[n] = 1
flag = 0

while q:
    if flag == 1:
        break
    cur, time = q.popleft()
    for i in (cur-1, cur+1, cur*2):
        if i == k:
            flag = 1
            break
        if visited[i] == 0 and 0 <= i <= 100000:
            q.append((i, time+1))
            visited[i] = 1

print(time)

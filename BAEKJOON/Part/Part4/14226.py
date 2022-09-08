from collections import deque

s = int(input())
visited = [[0] * 1001 for _ in range(1001)]

if s == 2:
    print(s)
else:
    queue = deque()
    queue.append([2, 1, 2]) # idx 0: 현재 입력된 이모티콘 수, idx 1: 현재 복사된 이모티콘 수, idx 2: 연산 수
    visited[2][1] = 1
    while queue:
        q = queue.popleft()
        if q[0] != q[1]:
            if visited[q[0]][q[0]] == 0:
                queue.append((q[0], q[0], q[2] + 1))
                visited[q[0]][q[0]] = 1
        if q[0] + q[1] == s or q[0] - 1 == s:
            cnt = q[2] + 1
            break
        if q[0] + q[1] <= 1000:
            if visited[q[0] + q[1]][q[1]] == 0:
                queue.append((q[0] + q[1], q[1], q[2] + 1))
                visited[q[0] + q[1]][q[1]] = 1
        if visited[q[0] - 1][q[1]] == 0:
            queue.append((q[0] - 1, q[1], q[2] + 1))
            visited[q[0] - 1][q[1]] = 1
    
    print(cnt)

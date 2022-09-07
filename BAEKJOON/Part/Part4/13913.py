from collections import deque

n, k = map(int, input().split())
visited = [-1] * 100001

if n >= k:
    print(n - k)
    for i in range(n, k-1, -1):
        print(i, end=' ')
else:
    queue = deque([n])
    visited[n] = n
    flag = 0
    while queue:
        q = queue.popleft()
        for i in (q*2, q-1, q+1):
            if i >= 0 and i <= 100000:
                if i == k:
                    visited[k] = q
                    flag = 1
                    break
                if visited[i] == -1:
                    visited[i] = q
                    queue.append(i)
        if flag == 1:
            break

    result = []
    cur = k
    while True:
        result.append(cur)
        if visited[cur] == n:
            result.append(n)
            break
        cur = visited[cur]
        
    print(len(result)-1)
    for i in result[::-1]:
        print(i, end=' ')

from collections import deque

n, k = map(int, input().split())
visited = [-1] * 100001

if n >= k:
    print(n-k)
else:
    queue = deque()
    queue.append(n)
    visited[n] = 0
    while queue:
        q = queue.popleft()
        if q*2 > 0 and q*2 <= 100000:
            if visited[q*2] == -1:
                visited[q*2] = visited[q]
                queue.append(q*2)

        for i in (q-1, q+1):
            if i >= 0 and i <= 100000:
                if visited[i] == -1:
                    visited[i] =  visited[q] + 1
                    queue.append(i)
                else:
                    if visited[i] > visited[q] + 1:
                        visited[i] = visited[q] + 1

    print(visited[k])

# [참고]
# 이거 어떻게 생각해.....
# def c(n,k):
#     if n >= k:
#         return n-k
#     elif k == 1:
#         return 1
#     elif k % 2: # k가 홀수이면 무조건 1 더하고 k-1과 k+1로 n을 만드는 방법 중에 최소 횟수 찾기
#         return 1 + min(c(n,k-1),c(n, k+1))
#     else: # k%2 == 0 k가 짝수이면 2 나눌때는 아무것도 더하지 않으니까 '2를 나눈수 중에서 n을 만드는 방법과 k에서 n까지 -1을 하는 방법' 중 최소 횟수 찾기
#         return min(k-n, c(n,k//2))
# n, k = map(int,input().split())
# print(c(n,k))

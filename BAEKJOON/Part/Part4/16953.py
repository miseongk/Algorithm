from collections import deque

a, b = map(int, input().split())

def bfs(a, b):
    queue = deque()
    queue.append((a*2, 1))
    queue.append((a*10 + 1, 1))

    while queue:
        q = queue.popleft()
        if q[0] == b:
            return q[1]
        if q[0] > b:
            continue
        if q[0] < b:
            queue.append((q[0]*2, q[1]+1))
            queue.append((q[0]*10 + 1, q[1]+1))
    return -2

print(bfs(a, b) + 1)

# [참고]
# 문제에서 2를 곱하거나 10을 곱한 후 1을 더해주는 연산만 가능하다.
# 2를 곱해서 홀수가 절대 될 수 없으므로 m의 뒤에 숫자가 1일때는 10으로 나누고
# 짝수일 때는 2로 나눠준다 (2를 곱하는 것보다 10곱하고 1 더하는 수가 훨씬 크기 때문에 10으로 나누는게 우선순위가 더 높음)
# 그 외의 홀수는 절대 나올 수 없으므로 while문에서 빠져나온다.

# n,m = map(int,input().split())
# count=0
# while n!=m:
#     if n>m:
#         count=-2
#         break
#     elif str(m)[-1]=='1':
#         m=m//10
#         count+=1
#     elif m%2==0:
#         m=m//2
#         count+=1
#     else:
#         count=-2
#         break
# print(count+1)

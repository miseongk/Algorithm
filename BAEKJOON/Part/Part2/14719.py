h, w = map(int, input().split())
arr = list(map(int, input().split()))

block = [[0] * w for _ in range(h)]

for i in range(w):
    for j in range(h-1, h-1-arr[i], -1):
        block[j][i] = 1

cnt = 0
for i in range(h-1, -1, -1):
    left, right = -1, -1
    for j in range(w):
        if block[i][j] == 1:
            if left == -1:
                left = j
            else:
                right = j
        if left != -1 and right != -1:
            diff = right - left - 1
            cnt += (right - left - 1)
            j -= 1
            left, right = right, -1

print(cnt)

# [참고]
# H, W = map(int, input().split())
# A = list(map(int, input().split()))
# M = []
# m = -1
# for i in range(len(A)-1, -1, -1):
#     if m < A[i]:
#         m = A[i]
#     M = [m] + M
#
# R = 0
# m = A[0]
# for i in range(1, len(A)-1):
#     t = min(m, M[i]) - A[i]
#     if t > 0:
#         R += t
#     if m < A[i]:
#         m = A[i]
# print(R)

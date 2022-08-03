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

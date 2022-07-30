n = int(input())
arr = list(map(int, input().split()))

cnt = 0
for m in arr:
    if m == 1:
        continue
    if m == 2 or m == 3:
        cnt += 1
        continue
    for i in range(2, m):
        if m % i == 0:
            break
        if i == m-1:
            cnt += 1

print(cnt)

m = int(input())
n = int(input())

flag = 0
arr = []
for i in range(m, n+1):
    flag = 0
    if i == 1:
        continue
    if i == 2:
        arr.append(i)
        continue
    for j in range(2, i):
        if i % j == 0:
            flag = 1
            break
    if flag == 0:
        arr.append(i)

if len(arr) == 0:
    print(-1)
else:
    print(sum(arr))
    print(min(arr))

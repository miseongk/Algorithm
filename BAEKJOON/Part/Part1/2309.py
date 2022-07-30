arr = []
sum = 0
for i in range(9):
    h = int(input())
    arr.append(h)
    sum += h

extra = sum - 100
flag = 0
for i in range(9):
    for j in range(i+1, 9):
        if (arr[i] + arr[j]) == extra:
            del arr[j]
            del arr[i]
            flag = 1
            break
    if flag == 1:
        break

arr.sort()

for i in range(7):
    print(arr[i])

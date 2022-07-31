a, b = map(int, input().split())

arr = [0] * 1001
j = 1
num = j
for i in range(b):
    arr[i] = j
    num -= 1
    if num == 0:
        j += 1
        num = j

arr = arr[a-1:b]
print(sum(arr))

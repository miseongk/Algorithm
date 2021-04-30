n = int(input())
array = []
for i in range(n):
    array.append(int(input()))

d = [0] * n
if n == 1:
    print(array[0])
elif n == 2:
    print(array[0] + array[1])
else:
    d[0] = array[0]
    d[1] = array[0] + array[1]
    d[2] = max(d[1], array[0] + array[2], array[1] + array[2])
    if n > 3:
        for i in range(3, n):
            d[i] = max(d[i-3] + array[i-1] + array[i], d[i-2] + array[i], d[i-1])

    print(max(d))

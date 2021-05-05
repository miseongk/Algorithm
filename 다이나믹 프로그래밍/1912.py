n = int(input())
array = list(map(int, input().split()))

d = [0] * (n+1)
d[0] = array[0]

for i in range(1, n):
    if array[i] + array[i-1] < 0:
        if array[i] > d[i-1]:
            d[i] = array[i]
    else:
        d[i] = d[i-1] + array[i] + array[i-1]
    if array[i] + d[i-1] > d[i-1]:
        d[i] = array[i] + d[i-1]
    else:
        d[i] = d[i-1]
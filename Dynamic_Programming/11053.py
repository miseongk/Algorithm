a = int(input())
array = list(map(int, input().split()))

d = [1] * (a+1)

for i in range(1, a):
    for j in range(0, i+1):
        if array[j] < array[i]:
            d[i] = max(d[i], d[j] + 1)

print(max(d))

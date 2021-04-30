T = int(input())
array = []

for i in range(T):
    array.append(int(input()))

for i in range(T):
    if array[i] <= 3:
        print(1)
    else:
        d = [0] * (array[i] + 1)
        d[1], d[2], d[3] = 1, 1, 1
        for j in range(4, array[i] + 1):
            d[j] = d[j-3] + d[j-2]
        print(d[array[i]])

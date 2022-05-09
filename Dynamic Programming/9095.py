T = int(input())
array = []
for i in range(T):
    array.append(int(input()))

d = [0] * 11
d[0] = 0
d[1] = 1
d[2] = 2
d[3] = 4

for i in range(T):
    for j in range(4, array[i] + 1):
        d[j] = d[j-3] + d[j-2] + d[j-1]

for i in array:
    print(d[i])


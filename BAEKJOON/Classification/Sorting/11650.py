n = int(input())
array = []

for i in range(n):
    array.append(list(map(int, input().split())))
array.sort(key=lambda x: x[1])
array.sort(key=lambda x: x[0])

for x,y in array:
    print(x, y)
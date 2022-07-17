n = int(input())
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(3):
        if j == 0:
            array[i][j] = min(array[i-1][j+1], array[i-1][j+2]) + array[i][j]
        elif j == 1:
            array[i][j] = min(array[i-1][j-1], array[i-1][j+1]) + array[i][j]
        else:
            array[i][j] = min(array[i-1][j-2], array[i-1][j-1]) + array[i][j]

print(min(array[n-1][0], array[n-1][1], array[n-1][2]))
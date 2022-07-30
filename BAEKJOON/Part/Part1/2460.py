arr = [list(map(int, input().split()))for _ in range(10)]

max = arr[0][1]
current = arr[0][1]
for i in range(1, 10):
    if max < (current - arr[i][0] + arr[i][1]):
        max = current - arr[i][0] + arr[i][1]

    current = current - arr[i][0] + arr[i][1]

print(max)
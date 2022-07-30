n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    arr[i].sort(reverse=True)
    print(arr[i][2])

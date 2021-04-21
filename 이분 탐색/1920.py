n = int(input())
A = list(map(int, input().split()))
m = int(input())
a = list(map(int, input().split()))

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return 1
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0

A.sort()

for i in range(m):
    print(binary_search(A, a[i], 0, n-1))
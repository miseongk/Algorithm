k, n = map(int, input().split())
array = []
for i in range(k):
    array.append(int(input()))

start = 0
end = max(array)
result = 0

while start <= end:
    total = 0
    mid = (start + end) // 2
    total = sum([i//mid if mid != 0 else i for i in array])
    if total < n:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)
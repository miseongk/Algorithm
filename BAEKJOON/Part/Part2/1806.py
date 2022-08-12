n, s = map(int, input().split())
nums = list(map(int, input().split()))

if sum(nums) < s:
    print(0)
    exit(0)

start = 0
end = 0
interval_sum = 0
cnt = n
min = n
for start in range(n):
    while interval_sum < s and end < n:
        interval_sum += nums[end]
        end += 1

    if interval_sum >= s:
        cnt = end - start

    interval_sum -= nums[start]

    if min > cnt:
        min = cnt

print(min)

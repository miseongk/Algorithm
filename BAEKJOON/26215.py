import heapq

n = int(input())
house = list(map(int, input().split()))
house.sort(reverse=True)

q = []
for i in house:
    heapq.heappush(q, (-i, i))

minute = 0
if len(q) == 1:
    minute = -1 if house[0] > 1440 else house[0]
else:
    while q:
        first = heapq.heappop(q)[1]
        first -= 1
        if len(q) > 0:
            second = heapq.heappop(q)[1]
            second -= 1
            if second > 0:
                heapq.heappush(q, (-second, second))
        if first > 0:
            heapq.heappush(q, (-first, first))
        minute += 1
        if minute > 1440:
            minute = -1
            break

print(minute)

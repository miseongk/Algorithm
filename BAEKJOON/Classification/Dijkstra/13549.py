import heapq
import sys
INF = int(1e9)

n, k = map(int, input().split())
graph = [[] for _ in range(200001)]
d = [INF] * 200001


# def set_graph(now):
#     if now <= 0 or now > (k + n) or now == k:
#         return
#     graph[now].append((now * 2, 0))
#     graph[now].append((now + 1, 1))
#     graph[now].append((now - 1, 1))
#     set_graph(now * 2)
#     set_graph(now-1)
#     set_graph(now+1)

for i in range(1, 100001):
    graph[i].append((i * 2, 0))
    graph[i].append((i - 1, 1))
    graph[i].append((i + 1, 1))


if n == 0:
    if k == n:
        print(0)
    else:
        print(1)
    exit(0)

q = []
d[n] = 0
heapq.heappush(q, (0, n))
while q:
    dist, now = heapq.heappop(q)
    if dist > d[now]:
        continue
    for i in graph[now]:
        cost = dist + i[1]
        if cost < d[i[0]]:
            d[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))

print(d[k])

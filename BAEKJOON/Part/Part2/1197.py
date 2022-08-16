# Kruskal 알고리즘
# import sys
#
# v, e = map(int, input().split())
# parent = [0] * (v+1)
# for i in range(1, v+1):
#     parent[i] = i
#
# edges = []
# total_cost = 0
#
# for _ in range(e):
#     start, end, cost = map(int, input().split())
#     edges.append((cost, start, end))
#
# edges.sort()
#
#
# def find_parent(x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent[x])
#     return parent[x]
#
#
# def union_parent(a, b):
#     a = find_parent(a)
#     b = find_parent(b)
#     if a < b:
#         parent[b] = parent[a]
#     else:
#         parent[a] = parent[b]
#
# # 크루스칼 알고리즘
# for i in range(e):
#     cost, a, b = edges[i]
#     if find_parent(a) != find_parent(b):
#         union_parent(a, b)
#         total_cost += cost
#
# print(total_cost)
# ----------------------------------------------------------------------
# Prim 알고리즘
import heapq

INF = int(1e9)

v, e = map(int, input().split())
graph = [[] for _ in range(v + 1)]
visited = [0] * (v + 1)

for i in range(e):
    u, v, weight = map(int, input().split())
    graph[u].append([weight, u, v])
    graph[v].append([weight, v, u])


# Prim 알고리즘
def prim(graph, start):
    q = []
    visited[start] = 1
    adj = graph[start]
    for i in adj:
        heapq.heappush(q, i)
    mst = []
    total_weight = 0
    while q:
        weight, u, v = heapq.heappop(q)
        if visited[v] == 0:
            visited[v] = 1
            mst.append((u, v))
            total_weight += weight

            for edge in graph[v]:
                if visited[edge[2]] == 0:
                    heapq.heappush(q, edge)

    return total_weight


print(prim(graph, 1))

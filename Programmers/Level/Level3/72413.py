import heapq
INF = int(1e9)

def solution(n, s, a, b, fares):
    global INF
    
    graph = [[] for _ in range(n+1)]
    for fare in fares:
        graph[fare[0]].append((fare[1], fare[2]))
        graph[fare[1]].append((fare[0], fare[2]))
    
    min_cost = INF
    for i in range(1, n+1):
        cost = 0
        # 합승 구간
        a_with_b = dijkstra(s, n, graph)
        if a_with_b[i] == INF:
            continue
        cost += a_with_b[i]
        # 합승 이후 각자 이동
        alone = dijkstra(i, n, graph)
        if alone[a] == INF or alone[b] == INF:
            continue
        cost += alone[a] + alone[b]
        
        # 최소 요금 찾기
        if cost < min_cost:
            min_cost = cost

    return min_cost

def dijkstra(start, n, graph):
    global INF
    
    distance = [INF] * (n+1)
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist:
            continue
        for i in graph[node]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance

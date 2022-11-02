import heapq

def solution(n, paths, gates, summits):
    answer = []
    graph = [[] for _ in range(n+1)]
    INF = int(1e9)
    distance = [INF] * (n+1)
    # 리스트 순회는 O(n) 시간이 걸리지만 set 순회는 O(1) 시간이 걸림 -> 시간초과 방지
    summits = set(summits)
    
    for path in paths:
        graph[path[0]].append((path[1], path[2]))
        graph[path[1]].append((path[0], path[2]))
    
    q = []
    for gate in gates:
        distance[gate] = 0
        heapq.heappush(q, (0, gate))

    while q:
        dist, now = heapq.heappop(q)
        # 산봉우리면 건너뛰기
        # 그 이유는 산봉우리는 도착지점이기 때문에 다른 곳으로 이동할 수 없게 막아야 되기 때문
        if now in summits or dist > distance[now]:
            continue
        for child in graph[now]:
            if distance[child[0]] > max(dist, child[1]):
                distance[child[0]] = max(dist, child[1])
                heapq.heappush(q, (distance[child[0]], child[0]))
            
    for summit in summits:
        answer.append([summit,distance[summit]])
    answer.sort(key = lambda x: (x[1],x[0]))
    
    return answer[0]

# 📓 최소 신장 트리 (MST, Minimum Spanning Tree)
## Spanning Tree
그래프 내의 모든 정점을 포함하는 트리

- 그래프의 **최소 연결 부분 그래프**
- n개의 정점을 가지는 그래프의 최소 간선의 수는 (n-1)개이고, (n-1)개의 간선으로 연결되어 있으면 필연적으로 트리 형태가 된다
- 즉, 그래프에서 일부 간선을 선택해서 만든 트리

## MST
spanning tree 중에서 **사용된 간선들의 가중치 합이 최소인 트리**

### 특징
1. 간선의 가중치 합이 최소여야 한다.
2. n개의 정점을 가지는 그래프에 대해 반드시 (n-1)개의 간선만을 사용해야 한다.
3. 사이클이 포함되어서는 안된다.

# MST 구현 방법 💡
## 1. Kruskal MST 알고리즘
비용에 따라 정렬된 간선을 하나씩 선택하며 MST를 찾는 방법

### 동작 원리
1. 주어진 모든 간선 정보에 대해 간선 비용이 낮은 순서로 정렬을 수행
2. 정렬된 간선 정보를 하나씩 확인하면서 현재의 간선이 노드들 간의 사이클을 발생시키는지 확인
3. 만약 사이클이 발생하지 않은 경우, 최소 신장 트리에 포함시키고 사이클이 발생한 경우, 최소 신장 트리에 포함시키지 않음
4. 1번~3번의 과정을 모든 간선 정보에 대해 반복 수행

노드들 간의 사이클이 발생하는지 여부는 _노드들의 부모노드가 같다면 사이클이 발생_, 같지 않다면 사이클이 발생하지 않음을 의미한다.
<br>초기단계 - 간선을 정렬하고, 부모노드를 가리키는 테이블을 자기 자신을 부모노드로 하도록 값을 초기화
```python
v, e = map(int, input().split())

# 부모 테이블 초기화
parent = [0] * (v+1)
for i in range(1, v+1):
    parent[i] = i

# find 연산
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# union 연산
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 간선 정보를 담을 리스트와 최소 신장 트리 계산 변수 정의
edges= []
total_cost = 0

# 간선 정보를 입력받고 비용을 기준으로 정렬
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

# 간선 정보를 비용 기준으로 오름차순 정렬
edges.sort()

# 간선 정보를 하나씩 확인하면서 크루스칼 알고리즘 수행
for i in range(e):
    cost, a, b = edges[i]
    # find 연산 후, 부모노드가 서로 다르면 사이클 발생하지 않으므로 union 연산 수행 -> 최소 신장 트리에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        total_cost += cost

print(total_cost)
```
## 2. Prim MST 알고리즘
시작 정점에서 출발하여 정점을 하나씩 선택하며 신장트리 집합을 확장해나가는 방법

### 동작 원리
1. 시작 단계에서는 시작 정점만이 MST 잡합에 포함된다.
2. 앞 단계에서 만들어진 MST 집합에 인접한 정점들 중에서 **최소 비용으로 연결된 정점을 선택**하여 트리를 확장한다.
   - 즉, 가장 낮은 가중치를 먼저 선택한다.
3. 위의 과정을 트리가 (n-1)개의 간선을 가질 때까지 반복한다.

```python
import heapq
INF = int(1e9)

v, e = map(int, input().split())
graph = [[] for _ in range(v+1)]
visited = [0] * (v+1)

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
```


<br>[출처] 
<br>https://gmlwjd9405.github.io/2018/08/28/algorithm-mst.html
<br>https://techblog-history-younghunjo1.tistory.com/262 
<br>https://deep-learning-study.tistory.com/595
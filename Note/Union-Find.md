# 📓 Union Find

### 서로소 집합 자료구조

- 서로소 집합이란 공통 원소가 없는 두 집합을 의미한다.
- 서로소 부분 집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료구조이다.
- 서로소 집합 자료구조는 두 종류의 연산을 지원한다.
  - 합집합(Union): 두 개의 원소가 포함된 집합을 하나의 집합으로 합치는 연산
  - 찾기(Find): 특정한 원소가 속한 집합이 어떤 집합인지 알려주는 연산
- 서로소 집합 자료구조는 Union Find 자료구조라고 불리기도 한다.

### 동작 과정

1. 합집합(Union) 연산을 확인하여, 서로 연결된 두 노드 A, B를 확인한다.
   1. A와 B의 루트 노트 A', B'를 각각 찾는다.
   2. A'를 B'의 부모 노드로 설정한다.
2. 모든 합집합(Union) 연산을 처리할 때까지 1번의 과정을 반복한다.

```python
# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드를 찾을 때까지 재귀 호출
    if parent[x] != x:
        # find 함수 비효율성 개선을 위해 find_parent 함수 호출 후 갱신
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선의 개수 입력 받기
v, e = map(int, input().split())
parent = [0] * (v + 1)

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# Union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)
```

[출처] - 이것이 코딩 테스트다 with Python

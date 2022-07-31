# 📓 순열 (Permutation)
서로 다른 n개의 원소에서 r개를 중복없이 순서에 상관있게 선택 또는 나열하는 것

## 순열 구현하기
### 1. itertools 라이브러리 사용
```python
import itertools

data = ['a', 'b', 'c']
result = list(itertools.permutations(data)

print(result)
# [('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]
```
### 2. DFS 사용
```python
data = ['a', 'b', 'c']
visited = [0 for _ in range(len(data))]
result = []

def dfs(cnt, list):
    if cnt == len(data):
        result.append(list[:])
        return
    
    for i, val in enumerate(data):
        # 만약 방문했다면 건너 뛰기
        if visited[i] == 1:
            continue
            # 현재까지의 list에 값을 추가하고, 방문 표시하기
        list.append(val)
        visited[i] = 1

        dfs(cnt + 1, list)
        # 방금 전 list에 추가한 값과 방문 할 것을 되돌려주기
        list.pop()
        visited[i] = 0

dfs(0, [])
print(result)
# [('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]
```

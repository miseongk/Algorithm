# 📓 Dictionary (Hash)
파이썬에서는 Dictionary라는 자료구조를 통해 해시를 제공한다. 

## 해시를 언제 사용할까?
### 1. 리스트를 사용할 수 없을 때
리스트는 숫자 인덱스를 이용하여 원소에 접근한다. 따라서 list['a']와 같이 인덱스 값을 숫자가 아닌 다른 값을 사용하려고 할 때 딕셔너리를 사용한다.
### 2. 빠른 접근/ 탐색이 필요할 때
딕셔너리의 함수 시간 복잡도는 대부분 O(1)이므로 아주 빠르다.

   | Operation   | Dictionary  | List        |
   |-------------|-------------|-------------|
   | Get         | O(1)        | O(1)        |
   | Insert      | O(1)        | O(1)~O(N)   |
   | Update      | O(1)        | O(1)        |
   | Delete      | O(1)        | O(1)~O(N)   |
   | Search      | O(1)        | O(N)        |

   즉, 원소를 삽입, 삭제, 검색할 때 딕셔너리를 사용하는 것이 좋다!
### 3. 집계가 필요할 때
원소의 개수를 세는 문제가 많이 출제되는데, 이때 해시와 collections 모듈의 Couter 클래스를 사용하면 아주 빠르게 문제 해결 가능하다.

## Dictionary 사용법
```python
# 딕셔너리 생성
dict1 = {}
dict2 = dict()
dict3 = {'a': 1, 'b': 2}

# get
dict3['a']
dict3.get('a', 0) # get 메소드는 해당 key가 없을 시 두번째 파라미터 값을 가져옴

# insert, update
dict3['c'] = 3 # insert
dict3['c'] = 300 # key가 있을 시 update

# delete
del dict3['c']

# 순회
for key in dict3:
    print(key) # 'a' 'b' 'c'
for key, value in dict3.items():
    print(key, value) # 'a' 1 'b' 2

# 조회
print('a' in dict3) # True
dict3.keys()
dict3.values()
```

[출처] - https://yunaaaas.tistory.com/46
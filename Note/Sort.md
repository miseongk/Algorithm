# 📓 Sort

## List 정렬

- sort: 본체를 정렬

```python
a = [1, 5, 3, 7, 2]
a.sort()

print(a) # [1, 2, 3, 5, 7]
```

- sorted: 정렬된 결과를 반환, 본체는 그대로

```python
a = [1, 5, 3, 7, 2]
b = sorted(a)

print(a) # [1, 5, 3, 7, 2]
print(b) # [1, 2, 3, 5, 7]
```

### key 속성에 lambda 사용하기 ⭐️

```python
a = [(1, 'apple'), (2, 'car'), (3, 'banana')]
a.sort(key = lambda item: item[1])
# 결과 [(1, 'apple'), (3, 'banana'), (2, 'car')]
```

## Dictionary 정렬

### Key를 기준으로 정렬

```python
dict = {'car': 2, 'apple': 1, 'banana': 3}

# 오름차순
sorted_dict = sorted(dict.items())
# 결과 [('apple': 1), ('banana': 3), ('car': 2)]


# 내림차순
sorted_dict = sorted(dict.items(), key = lambda item: item[0], reverse = True)
# 결과 [('car': 2), ('banana': 3), ('apple': 1)]
```

sorted()는 위와 같이 Tuple pair로 이루어진 list를 반환한다. <br>
참고로, dict.items()를 출력해보면 Tuple pair로 이루어진 list가 반환된다.

### Value를 기준으로 정렬

```python
dict = {'car': 2, 'apple': 1, 'banana': 3}

# 오름차순
sorted_dict = sorted(dict.items(), key = lambda item: item[1])
# 결과 [('apple': 1), ('car': 2), ('banana': 3)]


# 내림차순
sorted_dict = sorted(dict.items(), key = lambda item: item[1], reverse = True)
# 결과 [('banana': 3), ('car': 2), ('apple': 1)]
```

[참고] - https://codechacha.com/ko/python-sorting-dict/

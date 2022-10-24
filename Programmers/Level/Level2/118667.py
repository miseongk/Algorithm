from collections import deque

def solution(queue1, queue2):
    avg = (sum(queue1) + sum(queue2)) // 2
    cnt = 0
    total = sum(queue1)
    # 속도를 위해 리스트를 deque로 변환 -> popleft는 O(1) 하지만 리스트의 pop(0)은 O(n) 이기 때문
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    while queue1 and queue2:
        if total < avg:
            pop_item = queue2.popleft()
            queue1.append(pop_item)
            total += pop_item
            cnt += 1
        elif total > avg:
            pop_item = queue1.popleft()
            total -= pop_item
            cnt += 1
        else:
            return cnt
    return -1

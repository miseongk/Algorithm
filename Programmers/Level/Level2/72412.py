# 참고 - https://hongcoding.tistory.com/56

from itertools import combinations

def solution(info, query):
    answer = []
    info_dict = {}
    
    for i in range(len(info)):
        li = info[i].split()
        # 앞의 4부분을 키 값으로, 뒤의 점수를 value 값으로 분리한다.
        key = li[:-1]
        val = li[-1]
        # 키 값으로 만들 수 있는 조합을 생성해 info_dict에 넣는다.
        for j in range(5):
            for c in combinations(key, j):
                com = ''.join(c)
                if com in info_dict:
                    info_dict[com].append(int(val))
                else:
                    info_dict[com] = [int(val)]

    # 딕셔너리의 각 원소마다 value 값을 기준으로 정렬
    for i in info_dict:
        info_dict[i].sort()

    for q in query:
        cnt = 0
        score = []
        
        li = q.split()
        q_key = li[:-1]
        q_val = li[-1]
        while 'and' in q_key:
            q_key.remove('and')
        while '-' in q_key:
            q_key.remove('-')

        # 쿼리문을 이어 붙여 info_dict에서 찾는다.
        find = ''.join(q_key)
        if find in info_dict:
            score = info_dict[find]

        if len(score) == 0:
            answer.append(0)
        else:
            # 탐색 시 효율성을 위해 이분탐색을 사용
            cnt = len(score) - binaryLowerBound(score, int(q_val))
            answer.append(cnt)
                     
    return answer

# 이분탐색(lower bound) - 찾고자 하는 값이 존재하지 않는다면 해당 값과 같거나 큰 좌표 반환
def binaryLowerBound(arr, val):
    left, right = 0, len(arr)
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] >= val: # 타겟보다 좌표값이 크거나 같으면
            right = mid # 우측 조정
        elif arr[mid] < val: # 타겟보다 좌표값이 작으면
            left = mid + 1 # 좌측 조정
    return left # 하계는 타겟보다 같거나 큰 좌표이므로


# *이분탐색(upper bound) - 찾고자 하는 값이 존재하지 않는다면 해당 값보다 큰 값중에 가장 최소 좌표 반환
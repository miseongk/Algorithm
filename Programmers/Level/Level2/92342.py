max_score = 0
max_array = []

def solution(n, info):
    global max_score
    global max_array
    
    ryan = 0
    apeach = 0
    for i in range(len(info)):
        if info[i] != 0:
            apeach += 10 - i
    ryan_array = [0] * 11
    
    if n - info[0] - 1 >= 0:
        ryan_array[0] = info[0] + 1
        dfs(0, info[0] + 1, n - info[0] - 1, 10, ryan, apeach, ryan_array, info)
    
    ryan_array[0] = 0
    dfs(0, 0, n, 0, ryan, apeach, ryan_array, info)

    return max_array if len(max_array) > 0 else [-1]

# idx: 현재 과녁 인덱스
# cnt: 맞춘 과녁 개수
# remain_n: 남은 과녁 개수
# score: 현재 얻은 과녁 점수 (0~10)
# ryan: 현재 라이언 총 점수
# apeach: 현재 어피치 총 점수
# ryan_array: 현재까지 라이언이 맞춘 과녁 array
# info: 입력데이터 info
def dfs(idx, cnt, remain_n, score, ryan, apeach, ryan_array, info):
    global max_score
    global max_array

    # 점수가 0이 될 때까지 과녁이 남을 경우
    if idx == 10:
        ryan_array[10] = remain_n
        if ryan - apeach > max_score:
            max_score = ryan - apeach
            max_array = ryan_array.copy()
        elif ryan - apeach == max_score:
            if ryan - apeach > 0:
                for i in range(10, -1, -1):
                    if ryan_array[i] > 0 or max_array[i] > 0:
                        if ryan_array[i] > max_array[i]:
                            max_array = ryan_array.copy()
                        break       

        return
    
    # 모든 과녁을 쏜 경우
    if remain_n == 0:
        ryan_array[idx] = cnt
        for i in range(idx+1, 11):
            ryan_array[i] = 0
        if cnt > 0:
            ryan += score
            if info[idx] > 0:
                apeach -= score
        if ryan - apeach > max_score:
            max_score = ryan - apeach
            max_array = ryan_array.copy()
        elif ryan - apeach == max_score:
            if ryan - apeach > 0:
                for i in range(10, -1, -1):
                    if ryan_array[i] > 0 or max_array[i] > 0:
                        if ryan_array[i] > max_array[i]:
                            max_array = ryan_array.copy()
                        break        
        
        return
    
    else:
        ryan_array[idx] = cnt
        if cnt > 0:
            ryan += score
            if info[idx] > 0:
                apeach -= score
        
        if remain_n - info[idx+1] - 1 >= 0:
            dfs(idx+1, info[idx+1] + 1, remain_n - info[idx+1] - 1, 10 - idx - 1, ryan, apeach, ryan_array, info)
            
        dfs(idx+1, 0, remain_n, 0, ryan, apeach, ryan_array, info)

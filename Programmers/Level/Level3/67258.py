from collections import defaultdict

def solution(gems):
    answer = []
    buy_gems = set(gems)
    current_gems = defaultdict(int)
    answer_list = set()

    start = 0
    end = 0
    current_gems[gems[0]] = 1
    
    if len(buy_gems) == 1:
        return [1, 1]
    
    for i in range(1, len(gems)):
        if gems[i] == gems[start]:
            current_gems[gems[start]] -= 1
            if current_gems[gems[start]] == 0:
                del current_gems[gems[start]]
            start += 1
        end += 1
        current_gems[gems[end]] += 1

        while (True):
            num = current_gems[gems[start]]
            if num > 1:
                current_gems[gems[start]] -= 1
                if current_gems[gems[start]] == 0:
                    del current_gems[gems[start]]
                start += 1
            else: 
                break
                
        if len(current_gems.keys()) == len(buy_gems):
            answer_list.add((start, end, end - start + 1))
    
    answer_list = list(answer_list)
    answer_list.sort(key=lambda x: (x[2], x[0]))
    answer = [answer_list[0][0] + 1, answer_list[0][1] + 1] 
    
    return answer

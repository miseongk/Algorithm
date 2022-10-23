def solution(survey, choices):
    answer = ''
    type = {
        'R': 0, 'T': 0, 'C': 0, 'F': 0,
        'J': 0, 'M': 0, 'A': 0, 'N': 0
    }
    # 튜플 첫번째 원소 : 지표에서 점수가 더해질 위치 인덱스, 튜플 두번째 원소 : 더해질 점수
    score = {
        1: (0, 3), 2: (0, 2), 3: (0, 1), 4: (0, 0),
        5: (1, 1), 6: (1, 2), 7: (1, 3)
    }
    for s, choice in zip(survey, choices):
        type[s[score[choice][0]]] += score[choice][1]
    
    answer += 'R' if type['R'] >= type['T'] else 'T'
    answer += 'C' if type['C'] >= type['F'] else 'F'
    answer += 'J' if type['J'] >= type['M'] else 'M'
    answer += 'A' if type['A'] >= type['N'] else 'N'
        
    return answer
    
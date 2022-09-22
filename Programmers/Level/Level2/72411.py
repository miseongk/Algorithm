from itertools import combinations

def solution(orders, course):
    answer = []
    coms = {}
    for order in orders:
        for c in course:
            results = list(combinations(list(order), c))
            if c not in coms:
                coms[c] = {}
            for result in results:
                result = ''.join(sorted(result))
                if result in coms[c]:
                    coms[c][result] += 1
                else:
                    coms[c][result] = 1
    
    for i in course:
        sort_com = sorted(coms[i].items(), key = lambda item: item[1], reverse = True)
        max = 1
        for j in sort_com:
            if max < j[1]:
                max = j[1]
                answer.append(j[0])
                continue
            if max == j[1] and j[1] != 1:
                answer.append(j[0])
            else:
                break
        
        answer.sort()
    
    return answer
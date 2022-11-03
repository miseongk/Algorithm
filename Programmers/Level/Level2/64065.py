def solution(s):
    answer = []
    tuple_list = []
    for t in s[2:-2].split('},{'):
        tuple_list.append(list(int(i) for i in t.split(',')))
    tuple_list.sort(key=lambda x:len(x))
    
    for tup in tuple_list:
        answer.append(list(set(tup) - set(answer))[0])
        
    return answer

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    dic = {}
    for i, val in enumerate(id_list):
        dic[val] = {}
        dic[val]['idx'] = i
        dic[val]['reported'] = set()

    for i in report:
        i = i.split(' ')
        dic[i[1]]['reported'].add(i[0])

    for i in id_list:
        if len(dic[i]['reported']) >= k:
            for report in dic[i]['reported']:
                answer[dic[report]['idx']] += 1

    return answer

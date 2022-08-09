def solution(s):
    answer = 0
    dic = {"zero": 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    string = ""

    for i in s:
        if i >= 'a' and i <= 'z':
            string += i
            if string in dic:
                answer = answer * 10 + dic[string]
                string = ""
        else:
            answer = answer * 10 + int(i)

    return answer

# [참고]
# def solution(s):
#     num_dic = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
#     answer = s
#     for key, value in num_dic.items():
#         answer = answer.replace(key, value)
#     return int(answer)
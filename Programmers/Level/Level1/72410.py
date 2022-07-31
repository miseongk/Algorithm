def solution(new_id):
    answer = new_id
    answer = answer.lower()
    chars = '~!@#$%^&*()=+[{]}:?,<>/'
    for c in chars:
        answer = answer.replace(c, "")
    i = 0
    len_ = len(answer)
    while True:
        if i == len_ - 1:
            break
        if answer[i] == '.':
            if answer[i + 1] == '.':
                answer = answer[0:i] + answer[i+1:len_]
                len_ -= 1
                i -= 1
        i += 1
    answer = answer.strip('.')
    if len(answer) == 0:
        answer = 'a'
    if len(answer) >= 16:
        answer = answer[0:15]
        answer = answer.rstrip('.')
    if len(answer) <= 2:
        while len(answer) < 3:
            tmp = answer[-1]
            answer = answer + tmp

    return answer

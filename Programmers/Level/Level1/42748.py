def solution(array, commands):
    answer = []
    for com in commands:
        arr = array[com[0] - 1:com[1]]
        arr.sort()
        answer.append(arr[com[2] - 1])
    return answer

# [참고]
# lambda 매개변수 : 표현식
# map(함수, 리스트) -> 리스트의 원소를 하나씩 꺼내서 함수의 매개변수로 넣어서 처리 후 반환
# def solution(array, commands):
#     return list(map(lambda x: sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

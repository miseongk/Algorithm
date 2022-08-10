def solution(board, moves):
    answer = 0
    result = []
    flag = 0
    for move in moves:
        for i in board:
            if i[move - 1] == 0:
                continue

            if len(result) != 0:
                while len(result) > 0:
                    if result[-1] == i[move - 1]:
                        result.pop()
                        answer += 1
                        flag = 1
                    else:
                        break
            result.append(i[move - 1])
            if flag == 1:
                result.pop()
                answer += 1
                flag = 0
            i[move - 1] = 0

            break

    return answer

# [참고]
# def solution(board, moves):
#     stacklist = []
#     answer = 0
#
#     for i in moves:
#         for j in range(len(board)):
#             if board[j][i-1] != 0:
#                 stacklist.append(board[j][i-1])
#                 board[j][i-1] = 0
#
#                 if len(stacklist) > 1:
#                     if stacklist[-1] == stacklist[-2]:
#                         stacklist.pop()
#                         stacklist.pop()
#                         answer += 2
#                 break
#
#     return answer
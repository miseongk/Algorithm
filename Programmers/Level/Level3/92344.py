def solution(board, skill):
    answer = 0
    m = len(board[0])
    n = 0
    for _ in board:
        n += 1
    sum = [[0] * (m+1) for _ in range(n+1)]

    for s in skill:
        if s[0] == 1:
            sum[s[1]][s[2]] -= s[5]
            sum[s[1]][s[4]+1] += s[5]
            sum[s[3]+1][s[2]] += s[5]
            sum[s[3]+1][s[4]+1] -= s[5]
        else:
            sum[s[1]][s[2]] += s[5]
            sum[s[1]][s[4]+1] -= s[5]
            sum[s[3]+1][s[2]] -= s[5]
            sum[s[3]+1][s[4]+1] += s[5]
                
    # 누적합 구하기
    # 왼쪽에서 오른쪽
    for row in sum:
        for i in range(1, len(row)):
            row[i] += row[i-1] 
    # 위에서 아래
    for j in range(len(sum)):
        for i in range(1, len(sum)):
            sum[i][j] += sum[i-1][j]

    for i in range(n):
        for j in range(m):
            board[i][j] += sum[i][j]
            if board[i][j] > 0:
                answer += 1
                         
    return answer
    
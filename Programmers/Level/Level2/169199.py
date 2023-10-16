from collections import deque


def solution(board):
    answer = 0
    x, y = 0, 0

    for i in range(len(board)):
        length = len(board[i])
        pos = board[i].find("R")
        if pos != -1:
            x, y = i, pos
        dest_pos = board[i].find("G")
        if dest_pos != -1:
            dest_x, dest_y = i, dest_pos

    n = len(board)
    m = length

    visited = []
    for i in range(n):
        visited.append([-1] * m)

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    q = deque([(x, y, 0)])
    while q:
        x, y, level = q.popleft()
        if board[x][y] == "G":
            return level
        for i in range(4):
            nx, ny = x, y
            while True:
                nx += dx[i]
                ny += dy[i]
                # 벽을 넘어가는 경우
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    if board[nx - dx[i]][ny - dy[i]] == "G":
                        return level + 1
                    if visited[nx - dx[i]][ny - dy[i]] == -1:
                        visited[nx - dx[i]][ny - dy[i]] = level + 1
                        q.append((nx - dx[i], ny - dy[i], level + 1))
                    break
                # 벽에 막히는 경우
                if board[nx][ny] == "D":
                    if board[nx - dx[i]][ny - dy[i]] == "G":
                        return level + 1
                    if visited[nx - dx[i]][ny - dy[i]] == -1:
                        visited[nx - dx[i]][ny - dy[i]] = level + 1
                        q.append((nx - dx[i], ny - dy[i], level + 1))
                    break

    if visited[dest_x][dest_y] == -1:
        return -1

    return answer

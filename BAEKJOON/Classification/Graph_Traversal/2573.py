from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ice = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
# 변화하는 빙산 저장 (깊은복사 slicing 방법)
after_ice = [item[:] for item in ice]

def bfs(q):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if ice[nx][ny] == 0:
                if after_ice[x][y] > 0:
                    after_ice[x][y] -= 1
                else:
                    continue
            else:
                if visited[nx][ny] == 0:
                    q.append((nx, ny))
                    visited[nx][ny] = 1

def bfs_find_cnt(q2, visited):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while q2:
        x, y = q2.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if ice[nx][ny] != 0 and visited[nx][ny] == 0:
                q2.append((nx, ny))
                visited[nx][ny] = 1

def find_cnt(ice, visited):
    cnt = 0
    q2 = deque()
    for i in range(n):
        for j in range(m):
            if cnt == 1 and ice[i][j] != 0 and visited[i][j] == 0:
                return cnt + 1
            if ice[i][j] != 0 and visited[i][j] == 0:
                q2.append((i, j))
                visited[i][j] = 1
                bfs_find_cnt(q2, visited)
                cnt += 1

    return cnt

num = 0
q = deque()
while True:
    # 초기 시작점 찾기
    flag = 0
    for i in range(n):
        if flag == 1:
            break
        for j in range(m):
            if ice[i][j] != 0:
                q.append((i, j))
                visited[i][j] = 1
                flag = 1
                break
    if flag == 0:
        print(0)
        exit(0)
    # 1년 후의 빙하 구하기
    bfs(q)
    ice = [item[:] for item in after_ice]
    visited = [[0]*m for _ in range(n)]
    num += 1
    # 빙하 덩어리 개수 구하기
    if find_cnt(ice, visited) == 2:
        break
    else:
        visited = [[0]*m for _ in range(n)]

print(num)

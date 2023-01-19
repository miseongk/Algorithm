import sys
import copy
from collections import deque
input = sys.stdin.readline

m, n, h = map(int, input().split())
box = [[] for _ in range(h)]
for i in range(h):
    for j in range(n):
        box[i].append(list(map(int, input().split())))

cp_box = copy.deepcopy(box)
dh = [0, 0, 0, 0, 1, -1]
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
queue = deque([])
day = 0
cnt = 0

def move(i, j, k, day, queue):
    global cnt

    for l in range(6):
        nh = i + dh[l]
        nx = j + dx[l]
        ny = k + dy[l]
        if nh < 0 or nx < 0 or ny < 0 or nh >= h or nx >= n or ny >= m:
            continue
        if box[nh][nx][ny] == 0:
            box[nh][nx][ny] = 1
            cnt -= 1
            queue.append((nh, nx, ny, day+1))


for i in range(h):
    for j in range(n):
        for k in range(m):
            if cp_box[i][j][k] == 1:
                move(i, j, k, day, queue)
            elif cp_box[i][j][k] == 0:
                cnt += 1

if cnt == 0:
    print(0)
    exit(0)

while queue:
    i, j, k, day = queue.popleft()
    move(i, j, k, day, queue)

print(day if cnt == 0 else -1)

from collections import deque
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n = int(input())
area = [list(map(int, input().split())) for _ in range(n)]

max_h = 0
for i in area:
    max_h = max(max_h, max(i))

visited = [[max_h] * n for _ in range(n)]

def dfs(x, y, h):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if visited[x][y] == h:
        visited[x][y] -= 1
        
        dfs(x-1, y, h)
        dfs(x+1, y, h)
        dfs(x, y-1, h)
        dfs(x, y+1, h)

        return True
    return False

max_num = 0
for i in range(max_h-1, -1, -1):
    cnt = 0
    for j in range(n):
        for k in range(n):
            if area[j][k] - i > 0 and visited[j][k] == i+1:
                pass
            else:
                visited[j][k] -= 1
    for j in range(n):
        for k in range(n):
            if visited[j][k] == i+1:
                if dfs(j, k, i+1) == True:
                    cnt += 1

    max_num = max(max_num, cnt)

print(max_num)

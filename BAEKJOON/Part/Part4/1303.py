n, m = map(int, input().split())

graph =[]
visited = [[] for _ in range(m)]
for i in range(m):
    graph.append(list(map(str, input())))
    for _ in range(n):
        visited[i].append(False)

def dfs(x, y, c):
    global cnt
    cnt = c
    if x < 0 or x >= m or y < 0 or y >= n:
            return False
    if visited[x][y] == False and graph[x][y] == cur:
        visited[x][y] = True
        cnt += 1
        dfs(x+1, y, cnt)
        dfs(x-1, y, cnt)
        dfs(x, y-1, cnt)
        dfs(x, y+1, cnt)

        return True
    return False

white_score = 0
blue_score = 0
cur = ''
for i in range(m):
    for j in range(n):
        if graph[i][j] == 'W':
            cur = 'W'
        else:
            cur = 'B'
        if dfs(i, j, 0) == True:
            if cur == 'W':
                white_score += cnt ** 2
            else:
                blue_score += cnt ** 2
        
print(white_score, blue_score)
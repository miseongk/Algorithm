def dfs(x, y):
    global sum
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        sum += 1
        return True
    return False

n = int(input())
graph = []
sum = 0
result = 0
result_sum = []

for i in range(n):
    graph.append(list(map(int, input())))

for i in range(n):
    for j in range(n):
        if dfs(i, j):
            result += 1
            result_sum.append(sum)
            sum = 0

print(result)
result_sum.sort()
for i in range(len(result_sum)):
    print(result_sum[i])

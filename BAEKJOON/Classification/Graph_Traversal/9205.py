t = int(input())

def dfs(x, y, visited):
    if abs(festival[0] - x) + abs(festival[1] - y) <= 1000:
        return True
    else:
        for idx, store in enumerate(stores):
            if x == store[0] and y == store[1]:
                continue
            distance = abs(store[0] - x) + abs(store[1] - y)
            if distance <= 1000 and visited[idx] == 0:
                visited[idx] = 1
                if dfs(store[0], store[1], visited) == True:
                    return True
    return False

for j in range(t):
    n = int(input())
    stores = []
    visited = [0] * n

    for i in range(n + 2):
        if i == 0:
            home = tuple(map(int, input().split()))
        elif i == n+1:
            festival = tuple(map(int, input().split()))
        else:
            stores.append(tuple(map(int, input().split())))
    
    if dfs(home[0], home[1], visited) == True:
        print("happy")
    else:
        print("sad")


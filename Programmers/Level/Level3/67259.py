import heapq

def solution(board):
    answer = 0
    INF = int(1e9)
    distance = []
    for b in board:
        distance.append([[INF] * 4 for _ in range(len(b))])
        length = len(b)
    
    # 'E': 0, 'S': 1, W': 2, 'N': 3
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    q = []
    for i in range(4):
        distance[0][0][i] = 0
    heapq.heappush(q, (0, (0, 0), 0))
    while q:
        cost, pos, direction = heapq.heappop(q)
        
        if cost > distance[pos[0]][pos[1]][direction]:
            continue
        
        for i in range(4):
            nx = pos[0] + dx[i]
            ny = pos[1] + dy[i]
            
            if nx < 0 or nx >= length or ny < 0 or ny >= length or board[nx][ny] == 1:
                continue
            
            if pos[0] == 0 and pos[1] == 0:
                new_cost = 100
            else:
                new_cost = calCost(cost, direction, i)
                
            if new_cost <= distance[nx][ny][i]:
                distance[nx][ny][i] = new_cost
                heapq.heappush(q, (new_cost, (nx, ny), i))
    
    return min(distance[length-1][length-1])

def calCost(cost, direction, i):
    if direction == i:
        new_cost = cost + 100
    else:
        new_cost = cost + 600
        
    return new_cost

def solution(places):
    answer = []
    for place in places:
        matrix = []
        for row in place:
            row_list = []
            for i in range(5):
                if row[i] == 'P':
                    row_list.append(3)
                elif row[i] == 'O':
                    row_list.append(0)
                elif row[i] == 'X':
                    row_list.append(2)
            matrix.append(row_list)
        
        flag = 0
        for i in range(5):
            for j in range(5):
                if matrix[i][j] == 3:
                    if check(matrix, i, j, i, j, 0) == False:
                        flag = 1
                        break
            if flag == 1:
                break
        if flag == 0:
            answer.append(1)
        else:
            answer.append(0)
        
    return answer

def check(matrix, x, y, prev_x, prev_y, cnt):
    if cnt == 2:
        return True
    
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx < 0 or nx >= 5 or ny < 0 or ny >= 5 or (nx == prev_x and ny == prev_y):
            continue
        
        if matrix[nx][ny] == 0:
            matrix[nx][ny] = 1
            if check(matrix, nx, ny, prev_x, prev_y, cnt + 1) == False:
                return False
        elif matrix[nx][ny] == 3:
            return False

    return True
    
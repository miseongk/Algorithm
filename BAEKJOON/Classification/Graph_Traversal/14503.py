import sys
input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())

matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

def rotate(d):
    if d == 0:
        d = 3
    else:
        d -= 1
    
    return d

def goNext(r, c, d):
    if d == 0:
        r -= 1
    elif d == 1:
        c += 1
    elif d == 2:
        r += 1
    else:
        c -= 1
    
    return r, c

def goBack(r, c, d):
    if d == 0:
        r += 1
    elif d == 1:
        c -= 1
    elif d == 2:
        r -= 1
    else:
        c += 1

    return r, c

cnt = 0
stop = 0

while(True):
    # 네 방향 모두 청소가 되어있거나 벽인 경우
    if stop == 4:
        r, c = goBack(r, c, d)
        if matrix[r][c] == 1:
            break
        stop = 0
        continue

    # 아직 청소하지 않은 공간인 경우 청소
    if matrix[r][c] == 0:
        matrix[r][c] = 2
        cnt += 1
        stop = 0

    d = rotate(d)
    r, c = goNext(r, c, d)
    # 이미 청소한 공간이거나 벽인 경우
    if matrix[r][c] != 0:
        r, c = goBack(r, c, d)
        stop += 1

print(cnt)

    
import sys
input = sys.stdin.readline

n = int(input())
likes = []
student = [0] * (n**2)
for _ in range(n**2):
    likes.append(list(map(int, input().split())))
for i in range(n**2):
    student[likes[i][0] - 1] = likes[i]
place = [[0 for _ in range(n)] for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for pos in range(n**2):
    tmp = []
    for i in range(n):
        for j in range(n):
            like = 0
            empty = 0
            if place[i][j] != 0:
                tmp.append((-1, -1, -i, -j, likes[pos][0]))
                continue
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    continue
                if place[nx][ny] in likes[pos]:
                    like += 1
                if place[nx][ny] == 0:
                    empty += 1
            # 인접한 좋아하는 학생 수, 인접한 비어있는 칸 수, (마이너스)행, (마이너스)열, 학생 번호
            # 행과 열에 마이너스 붙인 이유는 튜플을 내림차순으로 정렬하기 때문.
            # 문제 조건에서 행과 열은 작은 순으로 선택하기 때문에 마이너스를 붙여 작은 번호의 행과 열이 큰것처럼 하기 위함.
            tmp.append((like, empty, -i, -j, likes[pos][0])) 
    fit = sorted(tmp, key=lambda x: (-x[0], -x[1], -x[2], -x[3]))
    place[-fit[0][2]][-fit[0][3]] = fit[0][4]

def calculateSatisfaction(like):
    if like == 0 or like == 1:
        return like
    elif like == 2:
        return 10
    elif like == 3:
        return 100
    else:
        return 1000
  
# 학생 만족도 총 합 구하기
sum = 0
for i in range(n):
    for j in range(n):
        like = 0
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if place[nx][ny] in student[place[i][j]-1]:
                like += 1
        sum += calculateSatisfaction(like)

print(sum)

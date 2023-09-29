n = int(input())

people = []
for i in range(n):
    people.append(tuple(map(int, input().split())))

score = [n] * n
for i in range(n):
    for j in range(i + 1, n):
        if people[i][0] > people[j][0] and people[i][1] > people[j][1]:
            score[i] -= 1
        elif people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            score[j] -= 1
        else:
            score[i] -= 1
            score[j] -= 1

for s in score:
    print(s, end=" ")

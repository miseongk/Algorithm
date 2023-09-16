T = int(input())
floor = [[0] * 15 for _ in range(15)]
for i in range(15):
    floor[0][i] = i
for f in range(1, 15):
    for ho in range(1, 15):
        floor[f][ho] = sum(floor[f-1][0:ho+1])

for i in range(T):
    k = int(input())
    n = int(input())
    print(floor[k][n])
import copy

n, m, k = map(int, input().split())

tile = []
for i in range(n):
    tile.append(list(input()))

cnt = 0
for i in range(k):
    for j in range(k):
        result = dict()
        for l in range(0, n, k):
            for h in range(0, m, k):
                tmp = result.get(tile[i + l][j + h], 0)
                result[tile[i + l][j + h]] = tmp + 1
        sortedDict = sorted(result.items(), key=lambda x: -x[1])
        for l in range(0, n, k):
            for h in range(0, m, k):
                if tile[i + l][j + h] != sortedDict[0][0]:
                    cnt += 1
                    tile[i + l][j + h] = sortedDict[0][0]
print(cnt)
for i in range(n):
    for j in range(m):
        print(tile[i][j], end="")
    print()

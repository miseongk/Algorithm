x = int(input())

d = [0] * (x+1)
d[0] = 0
d[1] = 0

for i in range(2, x+1):
    min_ = d[i-1] + 1
    if i % 2 == 0:
        min_ = min(d[i//2] + 1, min_)
    if i % 3 == 0:
        min_ = min(d[i//3] + 1, min_)
    d[i] = min_

print(d[x])
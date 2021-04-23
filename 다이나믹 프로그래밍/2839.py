n = int(input())
d = [5001] * (n+1)

d[0] = 0
for i in range(3, n+1):
    if d[i-3] != 5001:
        d[i] = d[i-3] + 1

for i in range(5, n+1):
    if d[i-5] != 5001:
        d[i] = d[i-5] + 1

if d[n] != 5001:
    print(d[n])
else:
    print(-1)
n = int(input())
t = []
p = []
for i in range(n):
    t_, p_ = list(map(int, input().split()))
    t.append(t_)
    p.append(p_)

d = [0] * (n+1)

for i in range(n):
    tmp = i + t[i]
    if tmp <= n:
        if d[i] == 0:
            if i > 0:
                d[i] = d[i-1]
        d[i] = max(d[:i+1])
        d[tmp] = max(d[tmp], d[i] + p[i])
    else:
        d[i] = max(d[:i+1])

print(max(d))

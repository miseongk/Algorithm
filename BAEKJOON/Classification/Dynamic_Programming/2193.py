n = int(input())

d = [0] * (n+1)

if n == 1:
    print(1)
elif n == 2:
    print(1)
else:
    d[1] = 1
    d[2] = 1
    d[3] = 2

    for i in range(4, n+1):
        d[i] = d[i-1] * 2 - d[i-3]

    print(d[n])

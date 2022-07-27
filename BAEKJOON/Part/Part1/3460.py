t = int(input())
n = [int(input()) for _ in range(t)]

for i in range(t):
    j = 0
    while n[i] > 0:
        if n[i] % 2 == 1:
            print(j, end=' ')
        n[i] //= 2
        j += 1
    print()

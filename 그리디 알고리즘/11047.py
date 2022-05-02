n, k = map(int, input().split())
data = [int(input()) for _ in range(n)]
data.sort(reverse=True)

result = 0

for coin in data:
    if k // coin == 0:
        continue
    result += k // coin
    k %= coin

print(result)
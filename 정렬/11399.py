n = int(input())
p = list(map(int, input().split()))
sum = 0

p.sort()
for i in range(n):
  sum += p[i] * (n-i)

print(sum)
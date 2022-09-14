# [참고] https://dreamtreeits.tistory.com/6
import sys

input = sys.stdin.readline
n = int(input())
t = []
for i in range(n):
    t.append(tuple(map(int, input().split())))

dp = [0] * (n+1)

cost = 0
for i in range(n):
    cost = max(cost, dp[i])
    if i + t[i][0] > n:
        continue
    dp[i + t[i][0]] = max(cost + t[i][1], dp[i + t[i][0]])

print(max(dp))

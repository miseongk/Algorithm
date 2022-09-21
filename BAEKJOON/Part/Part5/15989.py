# 참고 https://velog.io/@lchyung1998/%EC%96%B4%EB%A0%A4%EC%9B%8C%EC%9A%94%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-BOJ-15989-1-2-3-%EB%8D%94%ED%95%98%EA%B8%B0-4

t = int(input())
dp = [[0, 0, 0] for _ in range(10002)]

# dp[n][0] = dp[n-1][0] (1로 시작하고 1보다 작거나 같은 수를 사용해서 n을 만드는 경우)
# dp[n][1] = dp[n-2][0] + dp[n-2][1] (2로 시작하고 2보다 작거나 같은 수를 사용해서 n을 만드는 경우)
# dp[n][2] = dp[n-3][0] + dp[n-3][1] + dp[n-3][2] (3으로 시작하고 3보다 작거나 같은 수를 사용해서 n을 만드는 경우)

dp[1][0] = 1
dp[1][1] = 0
dp[1][2] = 0
dp[2][0] = 1
dp[2][1] = 1
dp[2][2] = 0
dp[3][0] = 1
dp[3][1] = 1
dp[3][2] = 1

for i in range(4, 10002):
    dp[i][0] = dp[i-1][0]
    dp[i][1] = dp[i-2][0] + dp[i-2][1]
    dp[i][2] = dp[i-3][0] + dp[i-3][1] + dp[i-3][2]

for _ in range(t):
    n = int(input())
    print(dp[n][0] + dp[n][1] + dp[n][2])

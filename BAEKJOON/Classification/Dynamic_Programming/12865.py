# [참고] - https://fbtmdwhd33.tistory.com/60
n, k = map(int, input().split())

dp = [[0] * (k+1) for _ in range(n+1)]

for i in range(1, n+1):
    w, v = map(int, input().split())
    for j in range(1, k+1):
        dp[i][j] = dp[i-1][j]
        if j - w >= 0:
            dp[i][j] = max(dp[i-1][j-w] + v, dp[i-1][j])

print(dp[n][k])

# [참고]
# N, max_weight = map(int, input().split())
# dp = {0: 0}

# for _ in range(N):
#     w, v = map(int, input().split())
#     tmp = {}
#     for prev_w, prev_v in dp.items():
#         if prev_w + w <= max_weight and dp.get(prev_w + w, 0) < prev_v + v:
#             tmp[prev_w + w] = prev_v + v
#     dp.update(tmp)

# print(max(dp.values()))
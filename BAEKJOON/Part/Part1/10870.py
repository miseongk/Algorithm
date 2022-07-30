n = int(input())

dp = [0] * 21
dp[0] = 0
dp[1] = 1


def fibonacci(x):
    if x == 0 or x == 1:
        return dp[x]
    if dp[x] != 0:
        return dp[x]

    dp[x] = fibonacci(x-1) + fibonacci(x-2)
    return dp[x]


print(fibonacci(n))

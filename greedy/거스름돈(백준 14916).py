dp = [-1] * 100001

dp[2] = 1
for i in range(3, 100001):
    if dp[i - 2] != -1:
        dp[i] = dp[i - 2] + 1

dp[5] = 1
for i in range(6, 100001):
    if dp[i - 5] != -1:
        dp[i] = dp[i - 5] + 1
n = int(input())
print(dp[n])

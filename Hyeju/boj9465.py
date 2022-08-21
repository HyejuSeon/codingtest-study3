# 스티커
import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    dp = [list(map(int, sys.stdin.readline().split())) for _ in range(2)]

    for i in range(1, N):
        if i == 1:
            dp[0][i] += dp[1][i - 1]
            dp[1][i] += dp[0][i - 1]
        else:
            dp[0][i] += max(dp[1][i - 1], dp[1][i - 2])
            dp[1][i] += max(dp[0][i - 1], dp[0][i - 2])
    print(max(dp[0][N - 1], dp[1][N - 1]))
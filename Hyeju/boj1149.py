# RGB거리
import sys

N = int(sys.stdin.readline())
DP = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
for i in range(1, N):
   DP[i][0] += min(DP[i - 1][1], DP[i - 1][2])
   DP[i][1] += min(DP[i - 1][0], DP[i - 1][2])
   DP[i][2] += min(DP[i - 1][0], DP[i - 1][1])
print(min(DP[N - 1][0], min(DP[N - 1][1], DP[N - 1][2])))
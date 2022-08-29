# 평범한 배낭
import sys

N, K = map(int, sys.stdin.readline().split())
d = [[0] * (K + 1) for _ in range(N + 1)]
a = [[0, 0]]
for _ in range(N):
    a.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, N + 1):
    for j in range(1, K + 1):
        w = a[i][0]
        v = a[i][1]
        if j < w:
            d[i][j] = d[i - 1][j]
        else:
            d[i][j] = max(d[i - 1][j], d[i - 1][j - w] + v)
print(d[N][K])
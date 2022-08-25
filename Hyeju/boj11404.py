# 플로이드
import sys

INF = 10**9
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
d = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(n + 1):
    for j in range(n + 1):
        if i == j: d[i][j] = 0

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    d[a][b] = min(d[a][b], c)

for k in range(n + 1):
    for i in range(n + 1):
        for j in range(n + 1):
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if d[i][j] == INF: print(0, end=" ")
        else: print(d[i][j], end=" ")
    print()
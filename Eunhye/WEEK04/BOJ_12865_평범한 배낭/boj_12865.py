import sys

input = sys.stdin.readline

N, K = map(int, input().split())
cache = [[0 for _ in range(K+1)] for _ in range(N)]
for i in range(N):
    W, V = map(int, input().split())
    for j in range(K+1):
        if j >= W:
            if i == 0:
                cache[i][j] = V
            else:
                cache[i][j] = max(cache[i-1][j-W]+V, cache[i-1][j])
        elif i > 0:
            cache[i][j] = cache[i-1][j]
print(cache[N-1][K])
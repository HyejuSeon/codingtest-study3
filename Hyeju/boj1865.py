# 웜홀
from sys import stdin

INF = int(1e9)
def bellmanford():
    dist[1] = 0
    for i in range(N):
        for edge in edges:
            x, y, w = edge
            if dist[y] > dist[x] + w:
                if i == N - 1:
                    return True
                dist[y] = dist[x] + w
    return False

TC = int(stdin.readline())
for _ in range(TC):
    N, M, W = map(int, stdin.readline().split())
    edges = []
    for _ in range(M):
        S, E, T = map(int, stdin.readline().split())
        edges.append((S, E, T))
        edges.append((E, S, T))
    for _ in range(W):
        S, E, T = map(int, stdin.readline().split())
        edges.append((S, E, -T))
    dist = [INF for _ in range(N + 1)]
    if bellmanford():
        print("YES")
    else:
        print("NO")

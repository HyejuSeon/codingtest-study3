import sys

input = sys.stdin.readline

def bellman_ford(start, N, edges):
  dist = [10001 for _ in range(N+1)]
  dist[start] = 0
  for i in range(N):
    for S, E, T in edges:
      if dist[S] + T < dist[E]:
        dist[E] = dist[S] + T
        if i == N-1:
          return 1
  return 0

TC = int(input())
for _ in range(TC):
  N, M, W = map(int, input().split())
  edges = []
  
  for _ in range(M):
    S, E, T = map(int, input().split())
    edges.append((S, E, T))
    edges.append((E, S, T))

  for _ in range(W):
    S, E, T = map(int, input().split())
    edges.append((S, E, -T))
  
  print("YES" if bellman_ford(1, N, edges) else "NO")
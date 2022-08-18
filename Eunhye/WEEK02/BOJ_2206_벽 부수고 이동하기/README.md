## 풀이



## 코드

```python
import sys
from collections import deque
input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

N, M = map(int, input().split())
graph = [list(map(int, list(input().rstrip()))) for _ in range(N)]

visited = [[[0, 0] for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1

queue = deque([(0, 0, 0)])
broken = 0

while queue:
  y, x, broken = queue.popleft()
  if y == N-1 and x == M-1:
    break
  for i in range(4):
    ny, nx = y+dy[i], x+dx[i]
    if 0 <= ny < N and 0 <= nx < M:
      if not broken and graph[ny][nx]:
        visited[ny][nx][1] = visited[y][x][0] + 1
        queue.append((ny, nx, 1))
      elif not graph[ny][nx] and not visited[ny][nx][broken]:
        visited[ny][nx][broken] = visited[y][x][broken] + 1
        queue.append((ny, nx, broken))

print(visited[N-1][M-1][broken] if visited[N-1][M-1][broken] else -1)
```
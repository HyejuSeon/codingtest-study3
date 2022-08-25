## 풀이

플로이드 와샬(Floyd Warshall) 알고리즘을 이용해 풀어주었습니다.

i에서 k를 거쳐 j까지 간 거리가 현재 graph에 저장된 거리보다 짧다면 갱신해주었습니다.  

이후에 inf를 0으로 값을 바꿔주며 시작도시와 도착도시가 같은 경우도 0으로 바꾸어주었습니다.

## 코드

```python
import sys
import math
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[math.inf for _ in range(n)] for _ in range(n)]

for _ in range(m):
  a, b, c = map(int, input().split())
  if c < graph[a-1][b-1]: graph[a-1][b-1] = c

for k in range(n):
  for i in range(n):
    for j in range(n):
      if graph[i][k] + graph[k][j] < graph[i][j]:
        graph[i][j] = graph[i][k] + graph[k][j]

for a in range(n):
  for b in range(n):
    if graph[a][b] == math.inf or a == b:
      graph[a][b] = 0
for g in graph:
  print(*g, sep=" ")
```
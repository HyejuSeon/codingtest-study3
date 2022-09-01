## 풀이  

BFS를 이용하여 풀어주었습니다.  

visited를 여유롭게 500,000개의 math.inf로 초기화 해준 뒤 매번 visited를 더 짧은 time으로 갱신해주어 풀어주었습니다. time이 result보다 클 땐 더 이상 진행하지 않았고, 동생의 위치에 도착하게되면 result와 time을 비교하여 더 작은 값을 저장해주었습니다.

## 코드  
```python
from collections import deque
import math
import sys

input = sys.stdin.readline

N, K = map(int, input().split())
visited = [math.inf for _ in range(500001)]

result = math.inf
queue = deque([(N, 0)])
visited[N] = 1
while queue:
  src, time = queue.popleft()
  if src == K:
    result = min(result, time)
  if time < result:
    plus, minus, mul = src+1, src-1, src*2
    if 0 <= plus < 500001 and visited[plus] > time:
      visited[plus] = time+1
      queue.append((plus, time+1))
    if 0 <= minus < 500001 and visited[minus] > time:
      visited[minus] = time+1
      queue.append((minus, time+1))
    if 0 <= mul < 500001 and visited[mul] > time:
      visited[mul] = time
      queue.append((mul, time))
```
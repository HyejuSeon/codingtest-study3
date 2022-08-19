## 풀이

DFS로 풀어주었습니다.  

이미 풀었던 아래의 문제와 입력값을 받는 방식만 다를 뿐 풀이는 거의 동일합니다.
> [BOJ_1167_트리의 지름](https://github.com/kimeunh3/codingtest-study3/tree/main/Eunhye/WEEK01/BOJ_1167_%ED%8A%B8%EB%A6%AC%EC%9D%98%20%EC%A7%80%EB%A6%84)

## 코드

```python
import sys
sys.setrecursionlimit(10**7)

n = int(input())
tree = [[] for _ in range(n+1)]
result, max_node = 0, 0
for _ in range(n-1):
  p, ch, w = map(int, input().split())
  tree[p].append((ch, w))
  tree[ch].append((p, w))
  

def dfs(src, dist, visited):
  global result, max_node
  visited[src] = 1
  if dist > result:
    result = dist
    max_node = src
  for ch, w in tree[src]:
    if not visited[ch]:
      dfs(ch, dist+w, visited)

visited = [0 for _ in range(n+1)]

dfs(1, 0, visited[:])
dfs(max_node, 0, visited[:])

print(result)
```
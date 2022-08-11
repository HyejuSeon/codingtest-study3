## 풀이

DFS로 풀어주었습니다.  

이 문제를 풀기에 앞서 트리의 지름을 구하기 위해서는 먼저 알아야 할 부분은 다음과 같습니다.  
- 임의의 노드에서 가장 먼 거리를 가지는 노드는 트리의 지름을 이루는 두 노드 중 하나이다.

이것만 알게 된다면 트리의 지름을 선형 시간으로 구할 수 있게 됩니다.  

우선 인접리스트로 간선의 정보를 받아주었습니다. 그 후, DFS를 이용하여 dist가 result보다 큰 값을 가질 때마다 갱신해줄 때 가장 긴 거리를 가지는 노드인 max_node도 갱신해주었습니다.  

이 후에는 두 번의 DFS 호출만으로도 트리의 지름을 구할 수 있게 됩니다.  
- 임의의 노드에서 시작하는 DFS 호출
- 위의 호출에서 구해진 max_node에서 시작하는 DFS 호출

마지막에는 갱신된 result를 출력해주었습니다.  

## 코드

```python
V = int(input())
tree = [[] for _ in range(V+1)]
result, max_node = 0, 0
for _ in range(V):
  input_lst = list(map(int, input().split()))
  for i in range(1, len(input_lst)-1, 2):
    tree[input_lst[0]].append(tuple(input_lst[i:i+2]))

def dfs(src, dist, visited):
  global result, max_node
  visited[src] = 1
  if dist > result:
    result = dist
    max_node = src
  for v, d in tree[src]:
    if not visited[v]:
      dfs(v, dist+d, visited)

visited = [0 for _ in range(V+1)]

dfs(1, 0, visited[:])
dfs(max_node, 0, visited[:])

print(result)
```
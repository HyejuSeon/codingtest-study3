## 백준 1167 트리의 지름

### 알고리즘

```txt
 ✅ DFS
 ✅ 트리의 지름 구하기 증명
 1. 트리에서 임의의 정점 x를 잡는다(1로 잡음)
 2. 정점 x에서 가장 먼 정점 y를 찾는다.
 3. 정점 y에서 가장 먼 정점 z를 찾는다.
```

### 코드 구현

사용 언어 : **파이썬**

```python
import sys
sys.setrecursionlimit(10 ** 9)

def dfs(vt,dis):
    for a,b in graph[vt]:
        # a지점을 방문하지 않았다면
        if visited[a]==-1:
            # b(vt->a) + dis(다른 정점->vt)
            visited[a]=b+dis
            dfs(a,b+dis)

v=int(sys.stdin.readline())
graph=[[] for _ in range(v+1)]

for _ in range(v):
    arr=list(map(int, sys.stdin.readline().split()))
    for j in range(1,len(arr)-2,2):
        graph[arr[0]].append((arr[j],arr[j+1]))

# 1. 트리에서 임의의 정점 x를 잡는다 => x=1
visited=[-1]*(v+1)
visited[1]=0
dfs(1,0)

# 2. 정점 x에서 가장 먼 정점 y를 찾는다 => y=idx
idx=visited.index(max(visited))
visited=[-1]*(v+1)
visited[idx]=0
# 3. 정점 y에서 가장 먼 정점 z를 찾는다.
dfs(idx,0)

# z인덱스에 저장되어 있는 값이 곧 트리의 지름
print(max(visited))
```

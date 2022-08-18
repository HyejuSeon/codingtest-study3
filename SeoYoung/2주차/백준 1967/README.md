## 백준 1967 트리의 지름

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
def dfs(vt,dis):
    for a,b in graph[vt]:
        if visited[a]==-1:
            visited[a]=b+dis
            dfs(a,b+dis)

n=int(input())
graph=[[] for _ in range(n+1)]

for _ in range(n-1):
    a,b,c=list(map(int, input().split()))
    graph[a].append((b,c))
    graph[b].append((a,c))

visited=[-1]*(n+1)
visited[1]=0
dfs(1,0)

idx=visited.index(max(visited))
visited=[-1]*(n+1)
visited[idx]=0
dfs(idx,0)

print(max(visited))
```

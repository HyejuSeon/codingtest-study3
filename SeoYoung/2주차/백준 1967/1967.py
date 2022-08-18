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
import sys
sys.setrecursionlimit(10 ** 9)

def dfs(vt,dis):
    for a,b in graph[vt]:
        if visited[a]==-1:
            visited[a]=b+dis
            dfs(a,b+dis)

v=int(sys.stdin.readline())
graph=[[] for _ in range(v+1)]

for _ in range(v):
    arr=list(map(int, sys.stdin.readline().split()))
    for j in range(1,len(arr)-2,2):
        graph[arr[0]].append((arr[j],arr[j+1]))

visited=[-1]*(v+1)
visited[1]=0
dfs(1,0)

idx=visited.index(max(visited))
visited=[-1]*(v+1)
visited[idx]=0
dfs(idx,0)

print(max(visited))





#월드나라 n개의 지점 
# - n개의 지점 사이에는 m개의 도로와 w개의 웜홀이 있음
# 웜홀은 특이하게도 도착을 하게 되면 시작할 때보다 시간이 뒤로 감(웜홀은 시계가 거꾸로 간다)
# 출발하던 위치로 돌아왔을 때 출발했을 때보다 시간이 돌아가는 경우가 있는지 없는지 궁금
# dfs로 풀어보려다가.. 실패..!

def dfs(vt, dis,visited):
    for i in range(1,n+1):
        if visited[i]==-1 and len(graph[vt][i])!=0:
            d=dis+min(graph[vt][i])
            visited[i]=d
            dfs(i, d, visited)

tc=int(input())

for _ in range(tc):
    n,m,w= map(int, input().split())
    graph=[[ 0 for _ in range(n+1)] for _ in range(n+1)]
    for _ in range(m):
        s,e,t=map(int,input().split())
        graph[s][e].append(t)
        graph[e][s].append(t)
    for _ in range(w):
        s,e,t=map(int,input().split())
        graph[s][e].append(-t)
    
    isPossible=False
    for i in range(1, n+1):
         visited=[-1]*(n+1)
         visited[i]=0
         dfs(i,0, visited)
         for j in range(1,n+1):
            if i==j:
                continue
            if len(graph[j][i])!=0 and min(graph[j][i])+visited[j]<0:
                isPossible=True
                break
         if isPossible:
            break
    
    if isPossible:
        print("YES")
    else: 
        print("NO")

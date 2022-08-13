INF=int(1e9)

def bf(start):
    dis=[INF]*(n+1)
    dis[start]=0

    for i in range(n):
        for cur,next,cost in graph: 
            if dis[next]>cost+dis[cur]:
                dis[next]=cost+dis[cur]
                if i==n-1:
                    return True
    
    return False
           


tc=int(input())

for _ in range(tc):
    n,m,w= map(int, input().split())
    graph=[]

    for _ in range(m):
        s,e,t=map(int,input().split())
        graph.append((s,e,t))
        graph.append((e,s,t))
    for _ in range(w):
        s,e,t=map(int,input().split())
        graph.append((s,e,-t))
    
    isPossible=bf(1)
    if isPossible:
        print("YES")
    else:
        print("NO")
    
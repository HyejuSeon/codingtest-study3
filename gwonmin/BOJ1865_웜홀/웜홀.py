import sys

input = sys.stdin.readline

def bf(start):
    dis = [1e9] * (n+1) #최단거리 초기화
    dis[start] = 0

    #음의 사이클 판별을 위해 n번 반복
    for i in range(n):
        #반복마다 모든 간선 확인
        for edge in edges:
            cur = edge[0] #출발
            next_node = edge[1] #도착
            cost = edge[2] #비용

            #다음 노드로 이동하는 거리가 최단거리로 갱신가능한 경우
            if dis[next_node] > cost + dis[cur]:
                dis[next_node] = cost + dis[cur]
                #i=n-1이면 n번 돌린건데 이때도 갱신이 발생하면 음의 싸이클 존재
                if i == n - 1:
                    return True

    return False

tc = int(input())

for _ in range(tc):
    n, m, w = map(int,input().split())
    edges = []

    #도로 정보
    for _ in range(m):
        s, e, t = map(int, input().split())
        edges.append((s,e,t))
        edges.append((e,s,t))

    #웜홀 정보
    for _ in range(w):
        s, e, t = map(int, input().split())
        edges.append((s, e, -t))

    # bf알고리즘 조건에 dis[cur]!=INF 조건이 없으므로
    # 시작 위치는 무관
    # bf는 음의 싸이클의 유무 판별 알고리즘
    key = bf(1)
    if key:
        print("YES")
    else:
        print("NO")



'''
from collections import deque
tc = int(input())

for _ in range(tc):
    n, m, w = map(int,input().split())

    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        s, e, t = map(int,input().split())
        graph[s].append([e,t])
        graph[e].append([s,t])

    for _ in range(w):
        s, e, t = map(int,input().split())
        graph[s].append([e,-t])

    def bfs(start,end):
        visited = []
        visit = deque()
        visit.append(start)
        visited.append(start)

        min_time = 1e9

        while visit:
            pos,time = visit.popleft()

            if pos == end:
                min_time = min(min_time,time)

            for data in graph[pos]:
                if data not in visited:
                    visited.append(data)
                    visit.append([data[0],data[1]+time])

        return min_time

    result = 'NO'

    for i in range(1,m+1):
        a = bfs([i,0],m)
        b = bfs([m,0],i)

        if a+b < 0:
            result = 'YES'

    print(result)
    
'''
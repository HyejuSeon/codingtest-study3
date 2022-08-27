# 동생과 숨바꼭질을 하고 있다
# 수빈이는 점 n에 있고 동생은 k에 있다. 수빈이는 걷거나 순간이동 가능, 수빈이의 위치가 x일 때 걷는다면 1초 후에 x-1 혹은 x+1로 순간이동을 한다면 2*x의 위치
# 수빈이와 동생의 위치가 주어졌을 때 수빈이가 동생을 찾을 수 있는 가장 빠른 시간은 몇 초 후인가?

from collections import deque

def bfs(v):
    queue=deque([v])
    dis[v]=0

    while queue:
        v=queue.popleft()

        if v==k:
            print(dis[v])
            break

        for i in (v-1, v+1, v*2):
            if 0<=i<=100000 and dis[i]==-1:
                if i==v*2:
                    # 순간이동은 0초 걸림
                    dis[i]=dis[v]
                    # 순간이동이 훨씬 시간이 적게 걸리므로 큐의 앞에 넣어서 우선순위를 높임
                    queue.appendleft(i)
                else:
                    dis[i]=dis[v]+1
                    queue.append(i)
    
n,k=map(int, input().split())
dis=[-1]*100001
bfs(n)
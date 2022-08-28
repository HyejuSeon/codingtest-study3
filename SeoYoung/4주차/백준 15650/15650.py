# 1부터 n까지 자연수 중에서 중복없이 m개를 고른 수열
# 고른 수열은 오름차순이어야 한다

n,m=map(int,input().split())
arr=[]

def dfs(v):
    if len(arr)==m:
        print(' '.join(map(str, arr)))
        return
    
    for i in range(v, n+1):
        if i not in arr:
            arr.append(i)
            dfs(i+1)
            arr.pop()

dfs(1)
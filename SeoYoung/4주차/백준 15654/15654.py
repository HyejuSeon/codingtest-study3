n,m=map(int,input().split())
nums=list(map(int,input().split()))
arr=[]
nums.sort()

def dfs():
    if len(arr)==m:
        print(' '.join(map(str, arr)))
        return
    
    for i in nums:
        if i not in arr:
            arr.append(i)
            dfs()
            arr.pop()

dfs()
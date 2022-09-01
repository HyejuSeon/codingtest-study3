## 백준 15650 N과 M(5)

### 알고리즘

```txt
 ✅ 백트래킹
 ✅ dfs
```

### 코드 구현

사용 언어 : **파이썬**

```python
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
```

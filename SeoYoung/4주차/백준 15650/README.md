## 백준 15650 N과 M(2)

### 알고리즘

```txt
 ✅ 백트래킹
 ✅ dfs
```

### 코드 구현

사용 언어 : **파이썬**

```python
n,m=map(int,input().split())
arr=[]

def dfs(v):
    # 길이가 m인 수열을 만족할 시 출력
    if len(arr)==m:
        print(' '.join(map(str, arr)))
        return

    for i in range(v, n+1):
        if i not in arr:
            arr.append(i)
            # 수열이 오름차순이어야 하므로 현재 숫자보다 큰 숫자로 재귀호출
            dfs(i+1)
            arr.pop()

dfs(1)
```

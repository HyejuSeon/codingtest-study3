## 백준 9465 스티커

### 알고리즘

```txt
 ✅ dp
 ✅ 예외처리를 잘해줘야 함.. 안 그러면 인덱스 에러나요^^
```

### 코드 구현

사용 언어 : **파이썬**

```python
tc=int(input())

for _ in range(tc):
    n=int(input())
    s=[list(map(int,input().split())) for _ in range(2)]

    s[0][1]+=s[1][0]
    s[1][1]+=s[0][0]

    for i in range(2,n):
        s[0][i]+=max(s[1][i-1],s[1][i-2])
        s[1][i]+=max(s[0][i-1],s[0][i-2])

    print(max(s[0][n-1],s[1][n-1]))
```

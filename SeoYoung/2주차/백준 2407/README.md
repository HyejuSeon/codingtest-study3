## 백준 2407 조합

### 알고리즘

```txt
 ✅ 조합 공식(n!/(n-m)!* m!)
```

### 코드 구현

사용 언어 : **파이썬**

```python
import math
n,m=map(int,input().split())

numerator=math.factorial(n)
denominator=math.factorial(n-m)*math.factorial(m)
print(numerator//denominator)
```

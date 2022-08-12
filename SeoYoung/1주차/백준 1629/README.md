## 백준 1629 곱셈

### 알고리즘

```txt
 ✅ 수학
 ✅ a^b
    => b가 짝수일 때는 (a^(b//2))^2
    => b가 홀수일 때는 (a^(b//2))^2 * a
 ✅ 나머지 분배 법칙 = (AxB)%C = (A%C) *(B%C) % C
    => b가 짝수일 때는 (a^(b//2)%c) * (a^(b//2)%c)%c
    => b가 홀수일 때는 ((a^(b//2)%c) * (a^(b//2)%c) * a)%c
```

### 코드 구현

사용 언어 : **파이썬**

```python
a,b,c=map(int, input().split())

def multiplication(a,b):
    if b==1:
        return a%c
    else:
        # tmp에는 (a^(b//2)%c)가 저장됨
        tmp=multiplication(a,b//2)
        if b%2==0:
            return (tmp * tmp) % c
        else:
            return (tmp* tmp * a) % c

print(multiplication(a,b))
```

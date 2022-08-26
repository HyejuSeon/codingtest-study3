## 풀이

[풀이](https://kimeunh3.github.io/problem%20solving/boj_11444/)

이 문제는 행렬의 거듭제곱을 이용하여 풀 수 있습니다. 아래의 행렬을 거듭제곱했을 때의 결과를 지켜보면 피보나치 수를 발견할 수 있습니다.  

 $$\begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}^{1}=\begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}$$  

 $$\begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}^{2}=\begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}$$  

 $$\begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}^{3}=\begin{pmatrix} 3 & 2 \\ 2 & 1 \end{pmatrix}$$  

 $$\begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}^{n}=\begin{pmatrix} F_{n+1} & F_n \\ F_n & F_{n-1} \end{pmatrix}$$  

규칙을 찾았다면 아래의 행렬의 거듭제곱을 구하는 문제를 이용하여 풀어주면 됩니다.  
 >[[백준 BOJ_2740] 행렬 제곱 Python 풀이](https://kimeunh3.github.io/problem%20solving/boj_10830/)  

## 코드

```python
def multiply(a, b):
    n = len(a)
    c = [[0] * n  for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i][j] = (c[i][j]+a[i][k]*b[k][j])%p
    return c
def identity(n):
    c = [[0] * n for _ in range(n)]
    for i in range(n):
        c[i][i] = 1
    return c
def power(a, exp):
    if exp == 0:
        return identity(len(a))
    if exp % 2:
        return multiply(power(a, exp-1), a)
    half = power(a, exp // 2)
    return multiply(half, half)
N = int(input())
fib = [[1, 1], [1, 0]]
p = 1000000007
print(power(fib, N-1)[0][0])
```
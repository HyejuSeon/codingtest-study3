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
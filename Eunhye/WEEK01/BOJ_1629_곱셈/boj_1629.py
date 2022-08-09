def power(n, exp):
    if exp == 0:
        return 1
    half = power(n, exp // 2)
    if exp % 2:
        return (half*half*n)%C
    return (half*half)%C
A, B, C = map(int, input().split())
print(power(A, B))
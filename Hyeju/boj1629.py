# 곱셈
import sys
sys.setrecursionlimit(10000)
A, B, C = map(int, sys.stdin.readline().split())

def power(a, b, c):
    if b == 1:
        return a % c
    if b == 2:
        return a * a % c
    if b % 2:
        return ((power(a, b // 2, c) ** 2) * a) % c
    else:
        return ((power(a, b // 2, c) ** 2)) % c

print(power(A, B, C))
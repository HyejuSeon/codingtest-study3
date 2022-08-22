# 피보나치 수 6
import sys
sys.setrecursionlimit(10**9)
MOD = 1000000007

n = int(sys.stdin.readline())
dic = {0: 0, 1: 1, 2: 1}
def fibo(n):
    if n not in dic:
        if n % 2 == 0:
            dic[n] = (fibo(n + 1) - fibo(n - 1)) % MOD
        else:
            a = (n + 1) // 2
            dic[n] = (fibo(a) ** 2 + fibo(a - 1) ** 2) % MOD
    return dic[n]

print(fibo(n))

# 피보나치 수 6
import sys
sys.setrecursionlimit(10**9)

n = int(sys.stdin.readline())
dic = {0: 0, 1: 1, 2: 1}
def fibo(n):
    if not dic.get(n):
        if n % 2 == 0:
            dic[n] = (fibo(n + 1) - fibo(n - 1)) % 1000000007
        else:
            dic[n] = (fibo((n + 1) // 2) ** 2 + fibo((n + 1) // 2 - 1) ** 2) % 1000000007
    return dic[n]

print(fibo(n))



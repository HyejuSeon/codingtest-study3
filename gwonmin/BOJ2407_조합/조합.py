n, m = map(int,input().split())

def facto(num):
    result = 1
    for i in range(1,num+1):
        result *= i

    return result

print(facto(n)//(facto(n-m)*facto(m)))

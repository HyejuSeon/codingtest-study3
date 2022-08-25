import sys
input=sys.stdin.readline
p=1000000007
#제곱을 구하는 분할정복
def power(adj,n):
    if n==1:
        return adj
    elif n%2:
        return multi(power(adj,n-1),adj)
    else:
        return power(multi(adj,adj),n//2)
#행렬의 곱셈
def multi(a,b):
    temp=[[0]*len(b[0]) for _ in range(2)]
    for i in range(2):
        for j in range(len(b[0])):
            sum=0
            for k in range(2):
                sum+=a[i][k]*b[k][j]
            temp[i][j]=sum%p
    return temp
#초기 행렬
adj=[[1,1],[1,0]]
#피보나치 초기값
start=[[1],[1]]
n=int(input())
if n<3:
    print(1)
else:
    print(multi(power(adj,n-2),start)[0][0])

'''
import sys
import copy

input = sys.stdin.readline

n = int(input())

matrix = [[1,1],
          [1,0]]

result = [[1,1],
          [1,0]]

while n != 1:
    temp = copy.deepcopy(result)
    result[0][0] = (temp[0][0]*matrix[0][0])+(temp[0][1]*matrix[1][0])
    result[0][1] = (temp[0][0]*matrix[0][1])+(temp[0][1]*matrix[1][1])
    result[1][0] = (temp[1][0]*matrix[0][0])+(temp[1][1]*matrix[1][0])
    result[1][1] = (temp[1][0]*matrix[0][1])+(temp[1][1]*matrix[1][1])
    n-=1

print(result[0][1] % 1000000007)

'''
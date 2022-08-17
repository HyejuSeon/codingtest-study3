import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

def preorder(in_start, in_end, post_start, post_end):
    if in_start>in_end or post_start>post_end:
        return
    # 후위순회는 왼-오-루트의 순서 : 완전 최상위 원소는 postorder 배열의 마지막 원소
    root=postorder[post_end]

    left_num=node[root]-in_start #왼쪽 서브트리의 노드 수
    right_num=in_end-node[root] # 오른쪽 서브트리의 노드 수 

    print(root, end=" ")
    
    preorder(in_start, in_start+left_num-1, post_start, post_start+left_num-1)
    preorder(in_end-right_num+1, in_end, post_end-right_num, post_end-1)

n=int(input())

inorder=list(map(int, input().split()))
postorder=list(map(int,input().split()))

node=[0]*(n+1)
for i in range(n):
    node[inorder[i]]=i

preorder(0, n-1, 0, n-1)

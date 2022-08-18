## 백준 1991 트리

### 알고리즘

```txt
 ✅ 트리
 ✅ 재귀
```

### 코드 구현

사용 언어 : **파이썬**

```python
n=int(input())
tree={}

for _ in range(n):
    root, left, right=input().split()
    tree[root]=[left,right]

# 전위순회 - 루트->왼->오
def preorder(root):
    if root!='.':
        print(root, end="")
        preorder(tree[root][0])
        preorder(tree[root][1])
# 중위순회 - 왼->루트->오
def inorder(root):
    if root!='.':
        inorder(tree[root][0])
        print(root,end='')
        inorder(tree[root][1])

# 후위순회 - 왼->오->루트
def postorder(root):
    if root!='.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end="")

preorder('A')
print()
inorder('A')
print()
postorder('A')
```

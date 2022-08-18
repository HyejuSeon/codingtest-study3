from collections import defaultdict

n = int(input())
tree = defaultdict(list)

for _ in range(n):
    node, left, right = input().split()
    tree[node] = [left, right]

def preorder(root):
    if root == '.':
        return
    left = tree[root][0]
    right = tree[root][1]

    print(root,end='')

    if left != '.':
        preorder(left)

    if right != '.':
        preorder(right)

preorder('A')
print()

def inorder(root):
    if root == '.':
        return

    left = tree[root][0]
    right = tree[root][1]

    if left != '.':
        inorder(left)

    print(root,end='')

    if right != '.':
        inorder(right)


inorder('A')
print()

def postorder(root):

    if root == '.':
        return

    left = tree[root][0]
    right = tree[root][1]

    if left != '.':
        postorder(left)

    if right != '.':
        postorder(right)

    print(root,end='')

postorder('A')






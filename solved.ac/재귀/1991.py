import sys
input=sys.stdin.readline

n=int(input())
tree={}
for _ in range(n):
    node,left,right=map(str,input().split())
    tree[node]=(left,right)

def front(node):
    if node=='.':
        return
    print(node,end='')
    front(tree[node][0])
    front(tree[node][1])

def middle(node):
    if node=='.':
        return
    middle(tree[node][0])
    print(node,end='')
    middle(tree[node][1])

def rear(node):
    if node=='.':
        return
    rear(tree[node][0])
    rear(tree[node][1])
    print(node,end='')

front('A')
print()
middle('A')
print()
rear('A')

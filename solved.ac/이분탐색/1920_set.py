import sys
input=sys.stdin.readline

n=int(input())
nSet=set(map(int,input().split()))
m=int(input())
mList=list(map(int,input().split()))

for i in range(m):
    if mList[i] in nSet:
        print(1)
    else:
        print(0)
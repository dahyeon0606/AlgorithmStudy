import sys
input=sys.stdin.readline

n=int(input())
nList=set(map(int,input().split()))
m=int(input())
mList=list(map(int,input().split()))

for i in range(m): #O(m) = O(500,000)
    if mList[i] in nList: #set에서 in 명령어는 O(1)
        print(1,end=' ')
    else:
        print(0, end=' ')
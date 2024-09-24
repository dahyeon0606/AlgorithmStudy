import sys
input=sys.stdin.readline

n=int(input())
nList=list(map(int,input().split()))
nList.sort()
m=int(input())
mList=list(map(int,input().split()))

for i in range(m):
    now=mList[i]
    start=0
    end=len(nList)-1
    while start<=end:
        mid=(start+end)//2
        if nList[mid]==now:
            print(1)
            break
        elif nList[mid]>now:
            end=mid-1
        else:
            start=mid+1
    else:
        print(0)
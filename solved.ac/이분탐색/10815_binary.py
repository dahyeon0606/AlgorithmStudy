import sys
input=sys.stdin.readline

n=int(input())
nList=sorted(list(map(int,input().split()))) #이 중에서 있는 지 찾아야 함 array, 오름차순 정렬
m=int(input())
mList=list(map(int,input().split())) #이 리스트에 있는 숫자 하나하나가 key

for i in range(m):
    key=mList[i] #찾아야 하는 숫자
    
    start=0
    end=len(nList)-1
    check=False

    #상근이의 n개 숫자카드안에 key가 있는지 검사
    while start<=end: 
        mid=(start+end)//2
        if nList[mid]==key:
            check=True
            break
        elif nList[mid]<key:
            start=mid+1
        else:
            end=mid-1
    
    #상근이가 아는지 모르는 지에 따라 1,0 출력
    if check:
        print(1,end=' ')
    else:
        print(0,end=' ')
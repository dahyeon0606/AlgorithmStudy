import sys
input=sys.stdin.readline

x,y=map(int,input().split())
z=(y*100)//x

#승률이 변할 수 없는 경우
if z>=99:
    print(-1)

#승률이 변할 수 있는 경우
else:
    start=1
    end=1000000000 #몇씩 증가 시킬 지 결정
    answer=0
    while start<=end:
        mid=(start+end)//2
        if ((y+mid)*100)//(x+mid) > z:
            end=mid-1                                                                                                                                                                                                                 
            answer=mid
        else:
            start=mid+1

    print(answer)                         
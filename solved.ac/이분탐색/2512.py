import sys
input=sys.stdin.readline

N=int(input()) #지방 N개
requests=list(map(int,input().split())) #예산요청
M=int(input()) #총예산 M
answer=0
start=min(requests) #상한액
end=max(requests)
while start<=end:
    mid=(start+end)//2
    temp=0 #예산 총합

    for r in requests:
        if mid<r: #상한액 초과
            temp+=mid
        else: #상한액 이하
            temp+=r

    if temp>M:
        end=mid-1
    elif temp<=M:
        start=mid+1
        answer=mid
if answer!=0:   
    print(answer)
else:
    print(M//N)
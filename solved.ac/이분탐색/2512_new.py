import sys
input=sys.stdin.readline

N=int(input()) #지방 N개
requests=list(map(int,input().split())) #예산요청
M=int(input()) #총예산 M

start=0  #상한액
end=max(requests)

while start<=end:
    mid=(start+end)//2
    temp=0
    for r in requests:
        if mid < r: #상한액 초과
            temp+=mid
        else: #상한액 이하
            temp+=r
    #총예산 초과, 상한액 감소
    if temp>M:
        end=mid-1 
    #총예산 이하, 상한액 증가,  주의) start를 증가시키는데 등호가 있어야 함
    elif temp<=M:
        start=mid+1
print(end)
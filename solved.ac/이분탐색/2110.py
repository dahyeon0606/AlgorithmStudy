
import sys
input=sys.stdin.readline

n,c=map(int,input().split()) #집 개수, 공유기 개수
houses=[]
for _ in range(n):
    houses.append(int(input()))
houses.sort() #오름차순 정렬

answer=0
start=1 #공유기 사이의 최소 거리, 1
end=houses[-1]-houses[0] #공유기 사이의 최대 거리, (9-1)= 8 

#공유기 사이 거리를 구하는 이분탐색
while start<=end:
    mid=(start+end)//2 #구하고자 하는 공유기 사이의 거리
    cur=houses[0]
    count=1

    for i in range(1,len(houses)):
        if houses[i]>=cur+mid: #현위치 + 공유기사이 거리 <= 집위치
            count+=1
            cur=houses[i]
    
    #공유기 개수가 넘친다면, 공유기 간격을 늘려야함
    if count>=c:
        start=mid+1
        answer=mid
    #공유기 개수가 모자라다면, 공유기 간격을 좁혀야함
    else:
        end=mid-1
print(answer)

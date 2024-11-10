import sys
input=sys.stdin.readline

N=int(input())
lope=[]
for _ in range(N):
    lope.append(int(input()))

lope.sort() # 가장 적게 들 수 있는 로프부터 최대 중량을 계산하기 위해 오름차순 정렬

answer=0
length=len(lope)

for minLope in lope: 
    temp=minLope*length #최대중량 = 최소 무게 * 로프의 개수
    if temp>answer: 
        answer=temp
    length-=1

print(answer)
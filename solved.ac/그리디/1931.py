
import sys
input=sys.stdin.readline

n=int(input())
room=[] #start, end
for _ in range(n):
    start,end=map(int,input().split())
    room.append([start,end])
room.sort(key=lambda x:(x[1],x[0])) #끝나는 시간이 이른 순으로 정렬

answer=1
end=room[0][1]
for i in range(1,n):
    if room[i][0]>=end:
        end=room[i][1]
        answer+=1
print(answer)
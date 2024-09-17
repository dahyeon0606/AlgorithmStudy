import sys
input=sys.stdin.readline

current=list(input().strip())
dx=[-2,-2,-1,1,2,2,-1,1] #상 우 하 좌
dy=[-1,1,2,2,-1,1,-2,-2]

x=int(current[1])
# yList={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}
# y=yList[current[0]]

yList='0abcdefgh'
y=yList.index(current[0])

answer=0
for i in range(8):
    nx=x+dx[i]
    ny=y+dy[i]

    if 0<nx<9 and 0<ny<9:
        answer+=1
print(answer)
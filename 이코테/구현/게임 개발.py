import sys
input=sys.stdin.readline

n,m=map(int,input().split())
x,y,direction=map(int,input().split())

visited=[[0]*m for _ in range(n)] #방문여부 미방문0, 방문1
visited[x][y]=1

maps=[] #육지 0, 바다 1로 이루어진 맵
for _ in range(n):
    maps.append(list(map(int,input().split())))

dx=[-1,0,1,0] #북동남서
dy=[0,1,0,-1]

answer=1 #방문한 칸 수
turnTime=0 #도는 횟수 제한 - 4번
while True:
    #1. 왼쪽으로 회전한 좌표 구하기
    direction-=1
    if direction==-1:
        direction=3
    nx=x+dx[direction]
    ny=y+dy[direction]

    #2. 왼쪽이 갈 수 있는 경우 - 가본적 없고, 육지
    if visited[nx][ny]==0 and maps[nx][ny]==0:
        #이동, 방문처리
        x=nx
        y=ny
        visited[x][y]=1
        answer+=1
        turnTime=0
        continue #이동했으니 다시 다음 위치에서 4방향 검사하기 위해서
    #2. 왼쪽이 갈 수 없는 경우 - 가본적 없고 바다, 가본적 있고 육지, 가본적 있고 바다
    else: 
        turnTime+=1 #다음 왼쪽도 갈 수 있는지 검사하기 위해서
    
    #3. 갈 수 없는 방향이 누적되어서 4방향 모두 못 감
    if turnTime==4:
        nx=x-dx[direction] #회전 방향 유지한 채로 뒤의 좌표 구하기
        ny=y-dy[direction]

        if maps[nx][ny]==1: #뒤가 바다이면 종료
            break
        else: #뒤가 육지이면 뒤로 이동
            x=nx
            y=ny
        
        turnTime=0 #4방향 못가는 걸 인지 후, 방향 카운트를 다시 새기 위한 초기화

print(answer)
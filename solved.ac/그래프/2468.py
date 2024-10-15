import sys
input=sys.stdin.readline

region=[]
dx=[1,-1,0,0]
dy=[0,0,-1,1]
answer=-1

#지역 2차원 배열
N=int(input())
for _ in range(N):
    region.append(list(map(int,input().split())))

#1개의 안전한 영역 구하기
def BFS(sx,sy,h):
    queue=[[sx,sy]]
    visited[sx][sy]=True
    while queue:
        x,y=queue.pop(0)
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<N and 0<=ny<N and region[nx][ny]>h and not visited[nx][ny]:
                queue.append([nx,ny])
                visited[nx][ny]=True


for h in range(0,100): #h-잠기는 높이
    count=0 #h만큼 잠길 때, 안전 지역의 갯수 
    visited=[[False]*N for _ in range(N)] #지역 방문여부

    #지역 전체 순회하여 안전 지역 갯수 세기
    for i in range(N): 
        for j in range(N):
            if region[i][j]>h and not visited[i][j]:
                BFS(i,j,h)
                count+=1

    #안전 지역 갯수의 최댓값
    answer=max(answer,count)

print(answer)


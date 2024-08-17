import sys
input=sys.stdin.readline

dx=[-1,1,0,0] #상하좌우
dy=[0,0,-1,1]

def bfs():
    while len(queue)!=0:
        x,y=queue.pop(0)

        for i in range(4): #상하좌우 반복하여
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<= nx < m and 0 <= ny < n:
                if matrix[nx][ny] == 1: #지렁이가 이동 가능한 위치이면,
                    matrix[nx][ny]=0 
                    queue.append([nx,ny])

T=int(input())
for _ in range(T):
    m,n,k=map(int,input().split())

    #배추 행렬 만들기
    matrix=[[0 for _ in range(n)]for _ in range(m)] #m: x좌표, n: y좌표
    for _ in range(k):
        x,y=map(int,input().split())
        matrix[x][y]=1 #배추 위치 표시
    
    queue=[]
    count=0
    for i in range(m): #좌표 전체를 순회하다가
        for j in range(n):
            if matrix[i][j]==1: #배추가 있으면
                matrix[i][j]=0
                queue.append([i,j])
                bfs()
                count+=1
    print(count)  

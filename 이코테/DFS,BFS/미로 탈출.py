import sys
input=sys.stdin.readline

graph=[]
dx=[-1,1,0,0,]
dy=[0,0,-1,1]
n,m=map(int,input().split())
for _ in range(n):
    graph.append(list(map(int,input().strip())))

def bfs():
    queue=[]
    queue.append((0,0))
    while len(queue)!=0:
        x,y=queue.pop(0)
        for i in range(4):
            nx=dx[i]+x
            ny=dy[i]+y

            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny]==1: #방문하지 않았을 경우에만
                    graph[nx][ny]=graph[x][y]+1 #새로운 좌표에 이전 좌표+1
                    queue.append((nx,ny))
bfs()
print(graph[n-1][m-1])
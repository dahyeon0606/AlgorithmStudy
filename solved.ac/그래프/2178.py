import sys
input=sys.stdin.readline

n,m=map(int,input().split())
maze=[]
for _ in range(n):
    maze.append(list(map(int,input().strip())))

dx=[0,1,0,-1] #북동남서
dy=[1,0,-1,0]
visited=[[False]*m for _ in range(n)]
queue=[[0,0]]
def BFS():
    while queue:
        x,y=queue.pop(0)
        for i in range(4):
            nx=dx[i]+x
            ny=dy[i]+y

            if 0<=nx<n and 0<=ny<m and maze[nx][ny]==1:
                if not visited[nx][ny]:
                    visited[nx][ny]=True
                    queue.append([nx,ny])
                    maze[nx][ny]=maze[x][y]+1
                   

BFS()
print(maze)
print(maze[n-1][m-1])
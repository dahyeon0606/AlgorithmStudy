import sys
input=sys.stdin.readline

n,m=map(int,input().split())
graph=[]
for _ in range(n):
    temp=list(map(int,input().strip()))
    graph.append(temp)

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def dfs(i,j):
    visited[i][j]=True
    for r in range(4):
        nx=dx[r]+i
        ny=dy[r]+j

        if 0<=nx<n and 0<=ny<m:
            if graph[nx][ny]==0 and not visited[nx][ny]:
                graph[nx][ny]=1
                dfs(nx,ny)
    

count=0
for i in range(n): #세로
    for j in range(m): #가로
        if graph[i][j]==0:
            visited=[[False for _ in range(m)] for _ in range(n)]
            dfs(i,j)
            count+=1
print(count)
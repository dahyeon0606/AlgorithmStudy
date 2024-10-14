import sys
input=sys.stdin.readline

n=int(input())
matrix=[]
for _ in range(n):
    matrix.append(list(map(int,input().strip())))
visited=[[False]*n for _ in range(n)]
dx=[1,-1,0,0] #동서남북
dy=[0,0,-1,1]

def BFS(i,j):
    queue=[[i,j]]
    count=0
    while queue:
        x,y=queue.pop(0)
        count+=1 # if문 안에 있으면 처음 큐에 들어오는 좌표를 못셈
        for r in range(4):
            nx=dx[r]+x
            ny=dy[r]+y

            if 0<=nx<n and 0<=ny<n:
                if not visited[nx][ny] and matrix[nx][ny]==1:
                    queue.append([nx,ny])
                    visited[nx][ny]=True
    return count


house=0
houses=[]
for i in range(n):
    for j in range(n):
        if not visited[i][j] and matrix[i][j]==1:
            house+=1
            visited[i][j]=True # 처음 큐에 넣을 좌표를 방문처리 안하면 2번 방문하게 됨
            count=BFS(i,j)
            houses.append(count)

print(house)
houses.sort()
for h in houses:
    print(h)
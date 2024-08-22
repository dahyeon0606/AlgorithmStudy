import sys
input=sys.stdin.readline

n,m=map(int,input().split())
link=[[]for _ in range(n)]
for _ in range(m):
    a,b=map(int,input().split())
    link[a].append(b)
    link[b].append(a)

arrive=False
def dfs(i,count):
    global arrive
    if count==4:
        arrive=True
        return
    for l in link[i]:
        if not visited[l]:
            visited[l]=True
            dfs(l,count+1)
            visited[l]=False ##백트래킹

for i in range(n): #시작 노드를 바꿔가며 진행
    visited=[False for _ in range(n)]
    visited[i]=True
    count=0
    dfs(i,count)

    if arrive:
        print(1)
        sys.exit()
print(0)
    
import sys
input=sys.stdin. readline

N,M=map(int,input().split()) #정점, 간선
linkedList=[[] for _ in range(N+1)] #행이 N+1개인 2차원 배열을 만들 수 있음
visited=[False]*(N+1)
answer=0

for _ in range(M):
    u,v=map(int,input().split())
    linkedList[u].append(v)
    linkedList[v].append(u)
def BFS():
    while queue:
        temp=queue.pop(0)
        for l in linkedList[temp]:
            if not visited[l]:
                visited[l]=True
                queue.append(l)


for i in range(1,N+1):
    if not visited[i]: #BFS의 시작은 노드가 되어야함(노드의 인접한 노드들이 아님, 인접 노드로 할 경우 시작 노드를 나중에 세게 됨)
        answer+=1
        queue=[i]
        visited[i]=True
        BFS()

print(answer)
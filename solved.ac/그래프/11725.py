import sys
input=sys.stdin.readline

N=int(input())
linkedList=[[] for _ in range(N+1)]
for _ in range(N-1):
    u,v=map(int,input().split())
    linkedList[u].append(v)
    linkedList[v].append(u)
visited=[False for _ in range(N+1)]
answer=[]

def BFS(start):
    queue=[start]
    visited[start]=True
    while queue:
        now=queue.pop(0)
        for l in linkedList[now]:
            if not visited[l]:
                answer.append([l,now]) #[child, parent]
                queue.append(l)
                visited[l]=True


BFS(1)#루트 노드부터 탐색 시작
answer.sort(key=lambda x:x) #첫번째 원소를 오름차순 정렬
for child,parent in answer:
    print(parent)
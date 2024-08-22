import sys
input=sys.stdin.readline


node=int(input()) #max 100
line=int(input())
adj=[[] for _ in range(node+1)] #O(n)
visited=[False for _ in range(node+1)] #O(n)
answer=-1 #1은 계산에 포함시키지 않음

def bfs(): #O(node+line) 노드 수 + 간선 수
    global answer
    queue=[]
    queue.append(1)
    visited[1]=True
    while len(queue)!=0:
        temp=queue.pop(0)
        answer+=1
        for a in adj[temp]:
            if not visited[a]:
                visited[a]=True
                queue.append(a)
# cf
# 노드 수: n 일때, 
# 간선 수: n(n-1)/2 (비방향성 그래프), n(n-1) (방향성 그래프), n-1 (트리)

for _ in range(line): #O(n)
    i,j=map(int,input().split())
    adj[i].append(j)
    adj[j].append(i)

bfs()
print(answer)
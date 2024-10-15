
import sys
input=sys.stdin.readline


N,K=map(int,input().split())

MAX=10**5 #수빈이가 갈 수 있는 가능한 모든 좌표
visited=[False]*(MAX+1)
queue=[[N,0]] #[수빈위치, 시간]
visited[N]=True

def BFS():
    while queue:
        x,time=queue.pop(0)
        if x==K:
            print(time)
            break
        
        for a in (x+1,x-1,2*x):
            if 0<=a<=MAX and not visited[a]:
                queue.append([a,time+1])
                visited[a]=True
BFS()
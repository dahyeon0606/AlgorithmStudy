
linkedList=[[],[2,3],[4,5],[1],[2],[2]]
visited=[False]*6

def dfs(node):
    print(node,end=' ')
    for l in linkedList[node]:
        if not visited[l]:
            visited[l]=True
            dfs(l)

visited[1]=True
dfs(1)

print()
queue=[]
def bfs(first_node):
    visited=[False]*6
    visited[1]=True
    queue.append(first_node)
    while len(queue)!=0:
        node=queue.pop(0)
        print(node,end=' ')
        for l in linkedList[node]:
            if not visited[l]:
                visited[l]=True
                queue.append(l)

bfs(1)
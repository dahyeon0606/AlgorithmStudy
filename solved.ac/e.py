def DFS(s):
    global result
 
    if len(s) == 1:
        result = "AKARAKA"
        return
    else:
        if s != s[::-1]:
            return
        else:
            N = len(s) // 2
            DFS(s[:N])
            DFS(s[-N:])
 
S = input()
 
result = "IPSELENTI"
DFS(S)
 
print(result)
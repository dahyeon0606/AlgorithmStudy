import sys
input=sys.stdin.readline

T=int(input())
for _ in range(T):
    zeroCount=[1,0]
    oneCount=[0,1]
    n=int(input())
    if n>1:
        for i in range(n-1):
            zeroCount.append(oneCount[-1])
            oneCount.append(oneCount[-1]+oneCount[-2])
    print(zeroCount[n],oneCount[n])
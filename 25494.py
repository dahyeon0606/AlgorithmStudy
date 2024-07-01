
T=int(input())

for _ in range(T):
    a,b,c,=map(int,input().split())
    xList=[i for i in range(1,a+1)]
    yList=[i for i in range(1,b+1)]
    zList=[i for i in range(1,c+1)]

    count=0
    for x in xList:
        for y in yList:
            for z in zList:
                if x%y == y%z == z%x:
                    count+=1
    print(count)
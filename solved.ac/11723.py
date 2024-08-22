# add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
# remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
# check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
# toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
# all: S를 {1, 2, ..., 20} 으로 바꾼다.
# empty: S를 공집합으로 바꾼다.

import sys
input=sys.stdin.readline

m=int(input())
S=set()

for _ in range(m):
    temp=input().split()
    if len(temp)==1:
        if temp[0]=='all':
            S=set(range(1,21))
        else:
            S.clear()
    else:
        method,x=temp[0],temp[1]
        x=int(x)

        if method=='add':
            S.add(x)
        elif method=='remove':
            S.discard(x)
        elif method=='check':
            print(1 if x in S else 0)
        elif method=='toggle':
            if x in S:
                S.discard(x)
            else:
                S.add(x)
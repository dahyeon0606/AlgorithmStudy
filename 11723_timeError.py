# add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
# remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
# check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
# toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
# all: S를 {1, 2, ..., 20} 으로 바꾼다.
# empty: S를 공집합으로 바꾼다.

m=int(input())
S=[]
# check=[]


for _ in range(m):
    temp=list(map(str,input().split()))
    
    if temp[0]=='add' and temp[1] not in S:
        S.append(temp[1])
    elif temp[0]=='remove' and temp[1] in S:
        S.remove(temp[1])
    elif temp[0]=='check':
        if temp[1] in S:
            # check.append(1)
            print(1)
        else:
            # check.append(0)
            print(0)
    elif temp[0]=='toggle':
        if temp[1] in S:
            S.remove(temp[1])
        else:
            S.append(temp[1])
    elif temp[0]=='all':
        S.clear()
        for i in range(1,21):
            S.append(str(i))
    elif temp[0]=='empty':
        S.clear()
    # print(temp)
    # print(S)
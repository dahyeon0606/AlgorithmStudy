n=int(input())

bar=[]
for _ in range(n):
    bar.append(int(input()))

count=1
bar.reverse()
current=bar[0]
# print(bar)
for i in range(1,len(bar)):
    if current<bar[i]:
        count+=1
        current=bar[i]
    else:
        continue
print(count)
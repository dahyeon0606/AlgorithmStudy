
a=[1,2,3]
sa=[0]*4

for i in range(1,4):
    sa[i]=sa[i-1]+a[i-1]

print(sa)
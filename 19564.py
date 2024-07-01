
muse=input()

count=1
for i in range(len(muse)-1):
    current=muse[i]
    if current>=muse[i+1]: #등호 빠트림
        count+=1
    else:
        continue
        
print(count)

# abcdefghijklmnopqrstuvwxyz

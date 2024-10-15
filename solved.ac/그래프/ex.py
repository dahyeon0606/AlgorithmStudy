
temp=[('apple',3),('orange',4),('blueberry',2),('cherry',6)]
newTemp=sorted(temp,key=lambda x:x[1])
print(newTemp)


temp=[['orangeeeee',1],['app',2],['mango',3]]
newTemp=sorted(temp,key=lambda x: len(x[0]))
print(newTemp)
lst1 = [[1, 'Alice'], [2, 'Bob'], [3, 'Cara']]
lst2 = [[1, 'Delhi'], [2, 'Mumbai'], [3, 'Chennai']]
lst1.extend(lst2)
x=[]
res=[]
for i in lst1:
    if i[0] not in x:
        x.append(i[0])
for i in x:
    p=[]
    p.append(i)
    for j in lst1:
        if(j[0]==i):
            p.append(j[1])
    res.append(p)
     
print(res)
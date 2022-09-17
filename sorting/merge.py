l3=[]
l1=[1,7,9,11]
l2=[0,4,8,9]
i=0
j=0
while(i<len(l1) and j<len(l2)):
    if(l1[i]<=l2[j]):
        l3.append(l1[i])
        i=i+1
        print(l3)
    if(l1[i]>l2[j]):
        l3.append(l2[j])
        j=j+1
        print(l3)
while(i<len(l1)):
    l3.append(l1[i])
    i=i+1
while(j<len(l2)):
    l3.append(l2[j])
    j=j+1
# for i in range(0,len(l3)):
#     print(l3[i])
print(l3)

    

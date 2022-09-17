l3=[]
l1=[1,2,3,4]
l2=[0,6,7,8]
i=0
j=0
c=0
while(i<len(l1)-1 and j<len(l2)-1):
    if(l1[i]<=l2[j]):
        l3.append(l1[i])
        i=i+1
    if(l1[i]>l2[j]):
        l3.append(l2[j])
        j=j+1
while(i<len(l1)):
    l3.append(l1[i])
    i=i+1
while(j<len(l2)):
    l3.append(l2[j])
    j=j+1
print(l3)
    

l = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())
    l.append(ele) 
      
print(l)

for i in range(0,len(l)):
    min=i
    for j in range(i+1,len(l)):
        if(l[j]<l[min]):
            min=j
    l[min],l[i]=l[i],l[min]
    print(l)

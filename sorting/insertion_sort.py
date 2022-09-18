l=[]
n=eval(input("enter the no. of elements"))
for i in range(0,n):
    e=eval(input())
    l.append(e)
print(l)
for i in range(1,n):
    j=i-1
    key=l[i]
    while(j>=0 and key<l[j]):
        l[j+1]=l[j]
        print(l)
        j=j-1
    l[j+1]=key 
    print(l)

n=int(input("enter the number of elements:"))
print("enter the binary numbers:")
l=[input() for i in range(n)]
for i in range(n):
    for j in range(i+1,n):
        if int(l[i],2)>int(l[j],2):
            l[i],l[j]=l[j],l[i]
li=[int(i,2) for i in l]
print("the ascending order is:",li,"(binary:",l,")")


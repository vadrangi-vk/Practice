n=int(input("enter the number of binary numbers:"))
print("enter the binary numbers:")
l=[input() for i in range(n)]
lar=int(l[0],2)
for i in range(n):
    x=int(l[i],2)
    if x>lar:
        lar=x
print("the largest number is :",lar,"(binary:",bin(lar),")")

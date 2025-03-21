print("MUX (4X1)")
i=int(input("enter the i0 value:(0 or 1)"))
j=int(input("enter the i1 value:(0 or 1)"))
k=int(input("enter the i0 value:(0 or 1)"))
l=int(input("enter the i1 value:(0 or 1)"))
print("Enter the two selection line values:")
t=[int(input()) for i in range(2)]
print(t)
if t[0]==0 and t[1]==0:
    print("the outut is:",i)
elif t[0]==0 and t[1]==1:
    print("the outut is:",j)
elif t[0]==1 and t[1]==0:
    print("the outut is:",k)
elif t[0]==1 and t[1]==1:
    print("the outut is:",l)


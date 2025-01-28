a=input("enter the binary number:")
b=input("enter the binary number:")
a_i=int(a,2)
b_i=int(b,2)
print(a_i,b_i)
sum=a_i+b_i
dif=a_i-b_i
mul=a_i*b_i
div=a_i//b_i
print("addition of binary",bin(sum)[2:])
print("subtraction of binary",bin(dif)[2:])
print("multiplication of binary",bin(mul))
print("division of binary",bin(div)[2:])

#for binary base 2
#for octa base 8
#for hexadecimal base 16

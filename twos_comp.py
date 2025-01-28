import ones_comp as oc
b=input("enter the binary number:")
b2=oc.ones(b)
print("the ones",b2)
twos_comp = bin(int(b2, 2) + 1)[2:]
print("the twos comp is:",twos_comp)

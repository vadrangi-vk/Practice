#a xor b =(A.B')+(A'.B)

'''
Odd number of 1’s: The result is 1.
Even number of 1’s: The result is 0.
'''
def XOR(x):
    if (x.count(0)%2==0):
        return 0
    else:
        return 1
if __name__=="__main__":
    n=int(input("emter the number of inputs :"))
    print("enetr the inputs:")
    i=[int(input()) for i in range(n)]
    o=print("the XOR of that input bits is:",XOR(i))

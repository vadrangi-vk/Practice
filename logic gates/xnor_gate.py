'''
An even number of 1s in the inputs results in 1.
An odd number of 1s results in 0.
'''

def XNOR(x):
    if (x.count(0)%2==0):
        return 1
    else:
        return 0
if __name__=="__main__":
    n=int(input("emter the number of inputs :"))
    print("enetr the inputs:")
    i=[int(input()) for i in range(n)]
    o=print("the XNOR of that input bits is:",XNOR(i))


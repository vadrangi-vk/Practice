from and_gate import AND
from not_gate import NOT
def NAND(x):
    y=AND(x)
    return NOT(y)
if __name__=="__main__":
    n=int(input("emter the number of inputs :"))
    print("enetr the inputs:")
    i=[int(input()) for i in range(n)]
    o=print("the NAND of that input bits is:",NAND(i))

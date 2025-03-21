from or_gate import OR
from not_gate import NOT
def NOR(x):
    y=OR(x)
    return NOT(y)
if __name__=="__main__":
    n=int(input("emter the number of inputs :"))
    print("enetr the inputs:")
    i=[int(input()) for i in range(n)]
    o=print("the NOR of that input bits is:",NOR(i))

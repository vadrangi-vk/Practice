def OR(a):
    for i in a:
        if i==1:
            return 1
    return 0
if __name__=="__main__":
    n=int(input("emter the number of inputs :"))
    print("enetr the inputs:")
    i=[int(input()) for _ in range(n)]
    o=print("the OR of that input bits is:",OR(i))


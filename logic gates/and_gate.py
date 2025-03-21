def AND(a):
    for i in a:
        if i==0:
            return 0
    return 1
if __name__=="__main__":
    n=int(input("emter the number of inputs :"))
    print("enetr the inputs:")
    i=[int(input()) for _ in range(n)]
    o=print("the AND of that input bits is:",AND(i))


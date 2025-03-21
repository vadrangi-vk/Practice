def ones(b):
    b2 = ''
    for i in range(len(b)):
        if b[i] == '0':
            b2 += '1'
        else:
            b2 += '0'
    return b2

if __name__ == "__main__":
    b1 = input("Enter a binary number: ")
    print("The one's complement is:", ones(b1))

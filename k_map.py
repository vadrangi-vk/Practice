def generate_map(var):
    rows, column = 0, 0
    if var == 2:
        rows, column = 2, 2
    elif var == 3:
        rows, column = 2, 4
    elif var == 4:
        rows, column = 4, 4
    else:
        print("Works only up to 4 variables!")
        return 0, 0
    return rows, column

def fill_kmap(kmap, minterms, rows, columns):
    for minterm in minterms:
        row, col = get_position(minterm, rows, columns)
        if row < rows and col < columns:
            kmap[row][col] = 1
    return kmap

def get_position(minterm, rows, columns):
    row = minterm // columns
    col = minterm % columns
    return row, col

def print_kmap(kmap, rows, columns):
    print("K-map:")
    for i in range(rows):
        for j in range(columns):
            print(f"| {kmap[i][j]} ", end=" ")
        print("|")
        print("-" * (columns * 4 + 1))

n = int(input("Enter the number of variables (2, 3, or 4): "))
v = input("Enter the variables (separated by spaces): ").split()
fxn = input("Enter the minterm values (separated by spaces): ").split()

minterms = list(map(int, fxn))

cells = 2 ** n

if len(minterms) > cells:
    print("More values than expected!")
else:
    r, c = generate_map(n)
    kmap = [[0 for _ in range(c)] for _ in range(r)]

    kmap = fill_kmap(kmap, minterms, r, c)

    print_kmap(kmap, r, c)

from pyeda.inter import expr, truthtable
import numpy as np
import matplotlib.pyplot as plt

def build_kmap(expression):
    parsed_expr = expr(expression)
    tt = truthtable(parsed_expr.vars, parsed_expr)
    num_vars = len(parsed_expr.vars)

    if num_vars not in [2, 3, 4]:
        raise ValueError("This implementation supports only 2, 3, 4 variables")

    # For 2 variables (2x2 K-map)
    if num_vars == 2:
        kmap = np.zeros((2, 2), dtype=int)
        for minterm in tt:
            if minterm[1]:
                kmap[minterm[0][0], minterm[0][1]] = 1

    # For 3 variables (2x4 K-map)
    elif num_vars == 3:
        kmap = np.zeros((2, 4), dtype=int)
        for minterm in tt:
            if minterm[1]:
                kmap[minterm[0][0], minterm[0][1] + 2 * minterm[0][2]] = 1

    # For 4 variables (4x4 K-map)
    elif num_vars == 4:
        kmap = np.zeros((4, 4), dtype=int)
        for minterm in tt:
            if minterm[1]:
                kmap[minterm[0][0] + 2 * minterm[0][1], minterm[0][2] + 2 * minterm[0][3]] = 1

    return kmap

def plot_kmap(kmap, num_vars):
    if num_vars == 2:
        labels = ['00', '01', '11', '10']
        plt.imshow(kmap, cmap='Greys', extent=[0, 2, 0, 2])
        plt.xticks([0.5, 1.5], labels[:2])
        plt.yticks([0.5, 1.5], labels[2:])
        plt.title('K-map for 2 variables')
    elif num_vars == 3:
        labels = ['000', '001', '011', '010', '110', '111', '101', '100']
        plt.imshow(kmap, cmap='Greys', extent=[0, 4, 0, 2])
        plt.xticks([0.5, 1.5, 2.5, 3.5], labels[:4])
        plt.yticks([0.5, 1.5], labels[4:])
        plt.title('K-map for 3 variables')
    elif num_vars == 4:
        labels = ['0000', '0001', '0011', '0010', '0110', '0111', '0101', '0100',
                  '1100', '1101', '1111', '1110', '1010', '1011', '1001', '1000']
        plt.imshow(kmap, cmap='Greys', extent=[0, 4, 0, 4])
        plt.xticks([0.5, 1.5, 2.5, 3.5], labels[:4])
        plt.yticks([0.5, 1.5, 2.5, 3.5], labels[4:])
        plt.title('K-map for 4 variables')

    # Plot the values in the grid
    for (i, j), value in np.ndenumerate(kmap):
        plt.text(j + 0.5, i + 0.5, str(int(value)), ha='center', va='center')

    plt.colorbar(label='Value')
    plt.grid(False)
    plt.show()

# Main program
boolean_expression = input("Enter Boolean expression (e.g., 'A*B+C'): ")
kmap = build_kmap(boolean_expression)
num_vars = len(expr(boolean_expression).vars)
plot_kmap(kmap, num_vars)

class JKFlipFlop:
    def __init__(self):
        self.q = 0  # Initial state of Q is 0

    def update(self, j, k, clk):
        if clk:  # If clock signal is high
            if j == 0 and k == 0:
                # No change
                self.q = self.q
            elif j == 0 and k == 1:
                # Reset Q
                self.q = 0
            elif j == 1 and k == 0:
                # Set Q to 1
                self.q = 1
            elif j == 1 and k == 1:
                # Toggle Q
                self.q = 1 - self.q

    def get_output(self):
        return self.q


class DFlipFlop:
    def __init__(self):
        self.q = 0  # Initial state of Q is 0

    def update(self, d, clk):
        if clk:  # If clock signal is high
            self.q = d

    def get_output(self):
        return self.q


def jk_flipflop_interactive():
    jk_ff = JKFlipFlop()
    print("JK Flip-Flop Simulation:")
    while True:
        try:
            j = int(input("Enter J (0 or 1, or -1 to quit): "))
            if j == -1:
                break
            k = int(input("Enter K (0 or 1): "))
            clk = int(input("Enter Clock (0 for low, 1 for high): "))

            if j not in [0, 1] or k not in [0, 1] or clk not in [0, 1]:
                print("Invalid input! J, K, and Clock must be 0 or 1.")
                continue

            jk_ff.update(j, k, clk)
            print(f"J={j}, K={k}, Clock={clk} -> Q={jk_ff.get_output()}")
        except ValueError:
            print("Invalid input! Please enter integers 0 or 1.")

def d_flipflop_interactive():
    d_ff = DFlipFlop()
    print("\nD Flip-Flop Simulation:")
    while True:
        try:
            d = int(input("Enter D (0 or 1, or -1 to quit): "))
            if d == -1:
                break
            clk = int(input("Enter Clock (0 for low, 1 for high): "))

            if d not in [0, 1] or clk not in [0, 1]:
                print("Invalid input! D and Clock must be 0 or 1.")
                continue

            d_ff.update(d, clk)
            print(f"D={d}, Clock={clk} -> Q={d_ff.get_output()}")
        except ValueError:
            print("Invalid input! Please enter integers 0 or 1.")

def main():
    print("Welcome to the Flip-Flop Simulation!")
    while True:
        print("\nChoose the flip-flop to simulate:")
        print("1. JK Flip-Flop")
        print("2. D Flip-Flop")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            jk_flipflop_interactive()
        elif choice == '2':
            d_flipflop_interactive()
        elif choice == '3':
            print("Exiting the simulation. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()

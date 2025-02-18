<<<<<<< HEAD
class KMapSOP:
    def __init__(self, num_variables):
        self.num_variables = num_variables
        self.size = 2 ** num_variables  # Number of cells in the K-map (2^n)
        self.kmap = [0] * self.size  # Initialize K-map with zeros
        self.sop_expression = ''
    
    def set_values(self):
        """
        Allow user to input the truth values for the K-map.
        """
        print(f"Please input the truth table for {self.size} combinations (0 or 1).")
        print(f"Each entry corresponds to a combination of {self.num_variables} variables in binary order (from 000... to 111...).")
        
        for i in range(self.size):
            while True:
                try:
                    value = int(input(f"f({self.get_binary_representation(i)}) = "))
                    if value in [0, 1]:
                        self.kmap[i] = value
                        break
                    else:
                        print("Please enter either 0 or 1.")
                except ValueError:
                    print("Invalid input. Please enter 0 or 1.")
    
    def get_sop_expression(self):
        """
        Generates the SOP expression by finding all the 1's in the K-map
        and then forming the sum of products.
        """
        sop_terms = []
        for i in range(self.size):
            if self.kmap[i] == 1:
                # Generate the corresponding product term for this 1
                term = self.get_product_term(i)
                sop_terms.append(f"({term})")
        
        self.sop_expression = " + ".join(sop_terms)
        return self.sop_expression
    
    def get_product_term(self, index):
        """
        Given an index in the K-map, return the corresponding product term.
        The product term is built using variables and their negations.
        """
        # Convert the index to binary (truth value for each variable)
        binary = format(index, f"0{self.num_variables}b")
        
        product_term = []
        for i, bit in enumerate(binary):
            var = chr(ord('A') + i)  # Variable names: A, B, C, etc.
            if bit == '0':
                product_term.append(f"!{var}")  # Negated variable
            else:
                product_term.append(f"{var}")  # Non-negated variable
        
        return " * ".join(product_term)
    
    def print_kmap(self):
        """ Print the K-map in a grid format for visualization """
        print(f"K-map (Size: {self.size} cells):")
        for i in range(0, self.size, 2):
            print(self.kmap[i:i+2])
    
    def get_binary_representation(self, index):
        """ Returns the binary representation of the index for the given number of variables """
        return format(index, f"0{self.num_variables}b")

# Example of how to use the K-map class with user input for SOP
def create_kmap_for_sop():
    # Get the number of variables from the user
    while True:
        try:
            num_variables = int(input("Enter the number of variables: "))
            if num_variables > 0:
                break
            else:
                print("Number of variables must be greater than 0.")
        except ValueError:
            print("Invalid input. Please enter an integer.")
    
    # Create the K-map for the given number of variables
    kmap = KMapSOP(num_variables)
    
    # Set the truth values based on user input
    kmap.set_values()
    
    # Print K-map for visualization
    kmap.print_kmap()
    
    # Get the SOP expression from the K-map
    sop_expression = kmap.get_sop_expression()
    print("SOP Expression:", sop_expression)

# Run the interactive function for SOP
create_kmap_for_sop()
=======
class KMapSOP:
    def __init__(self, num_variables):
        self.num_variables = num_variables
        self.size = 2 ** num_variables  # Number of cells in the K-map (2^n)
        self.kmap = [0] * self.size  # Initialize K-map with zeros
        self.sop_expression = ''
    
    def set_values(self):
        """
        Allow user to input the truth values for the K-map.
        """
        print(f"Please input the truth table for {self.size} combinations (0 or 1).")
        print(f"Each entry corresponds to a combination of {self.num_variables} variables in binary order (from 000... to 111...).")
        
        for i in range(self.size):
            while True:
                try:
                    value = int(input(f"f({self.get_binary_representation(i)}) = "))
                    if value in [0, 1]:
                        self.kmap[i] = value
                        break
                    else:
                        print("Please enter either 0 or 1.")
                except ValueError:
                    print("Invalid input. Please enter 0 or 1.")
    
    def get_sop_expression(self):
        """
        Generates the SOP expression by finding all the 1's in the K-map
        and then forming the sum of products.
        """
        sop_terms = []
        for i in range(self.size):
            if self.kmap[i] == 1:
                # Generate the corresponding product term for this 1
                term = self.get_product_term(i)
                sop_terms.append(f"({term})")
        
        self.sop_expression = " + ".join(sop_terms)
        return self.sop_expression
    
    def get_product_term(self, index):
        """
        Given an index in the K-map, return the corresponding product term.
        The product term is built using variables and their negations.
        """
        # Convert the index to binary (truth value for each variable)
        binary = format(index, f"0{self.num_variables}b")
        
        product_term = []
        for i, bit in enumerate(binary):
            var = chr(ord('A') + i)  # Variable names: A, B, C, etc.
            if bit == '0':
                product_term.append(f"!{var}")  # Negated variable
            else:
                product_term.append(f"{var}")  # Non-negated variable
        
        return " * ".join(product_term)
    
    def print_kmap(self):
        """ Print the K-map in a grid format for visualization """
        print(f"K-map (Size: {self.size} cells):")
        for i in range(0, self.size, 2):
            print(self.kmap[i:i+2])
    
    def get_binary_representation(self, index):
        """ Returns the binary representation of the index for the given number of variables """
        return format(index, f"0{self.num_variables}b")

# Example of how to use the K-map class with user input for SOP
def create_kmap_for_sop():
    # Get the number of variables from the user
    while True:
        try:
            num_variables = int(input("Enter the number of variables: "))
            if num_variables > 0:
                break
            else:
                print("Number of variables must be greater than 0.")
        except ValueError:
            print("Invalid input. Please enter an integer.")
    
    # Create the K-map for the given number of variables
    kmap = KMapSOP(num_variables)
    
    # Set the truth values based on user input
    kmap.set_values()
    
    # Print K-map for visualization
    kmap.print_kmap()
    
    # Get the SOP expression from the K-map
    sop_expression = kmap.get_sop_expression()
    print("SOP Expression:", sop_expression)

# Run the interactive function for SOP
create_kmap_for_sop()
>>>>>>> 07e8b5564a7d700508d565b6f851596056731ebe

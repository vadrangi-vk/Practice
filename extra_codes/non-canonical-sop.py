def non_canonical_sop(minterms):
    # Given a list of minterms (decimal values)
    return ' + '.join([f"m{term}" for term in minterms])

# Example usage
minterms =int(input("enter the number of terms:"))  # These minterms correspond to a simplified Boolean expression
l=[int(input()) for i in range(minterms)]
result = non_canonical_sop(l)
print(f"Non-canonical SOP: {result}")

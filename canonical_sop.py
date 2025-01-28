def canonical_sop(truth_table):
    # Given the truth table (1 for minterms and 0 for others), generate the canonical SOP
    sop_terms = []
    for i, value in enumerate(truth_table):
        if value == 1:
            bin_term = bin(i)[2:].zfill(len(truth_table).bit_length())
            sop_terms.append(bin_term)
    return ' + '.join(sop_terms)

# Example usage

truth_table = [1, 0, 1, 1, 0, 1, 1, 1]  # Corresponding to some truth values
result = canonical_sop(truth_table)
print(f"Canonical SOP: {result}")

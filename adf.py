def binary_to_hex(binary_number):
    decimal = binary_to_decimal(binary_number)
    if isinstance(decimal, int):
        return decimal_to_hex(decimal)
    return decimal

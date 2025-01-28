
# Convert Decimal to Binary
def decimal_to_binary(decimal_number):
    if decimal_number < 0:
        return "Error: Negative numbers not supported"
    return bin(decimal_number)[2:]

# Convert Decimal to Octal
def decimal_to_octal(decimal_number):
    if decimal_number < 0:
        return "Error: Negative numbers not supported"
    return oct(decimal_number)[2:]

# Convert Decimal to Hexadecimal
def decimal_to_hex(decimal_number):
    if decimal_number < 0:
        return "Error: Negative numbers not supported"
    return hex(decimal_number)[2:]

# Convert Binary to Decimal
def binary_to_decimal(binary_number):
    try:
        return int(binary_number, 2)
    except ValueError:
        return "Error: Invalid binary number"

# Convert Octal to Decimal
def octal_to_decimal(octal_number):
    try:
        return int(octal_number, 8)
    except ValueError:
        return "Error: Invalid octal number"

# Convert Hexadecimal to Decimal
def hex_to_decimal(hex_number):
    try:
        return int(hex_number, 16)
    except ValueError:
        return "Error: Invalid hexadecimal number"

# Convert Binary to Octal
def binary_to_octal(binary_number):
    decimal = binary_to_decimal(binary_number)
    if isinstance(decimal, int):
        return decimal_to_octal(decimal)
    return decimal

# Convert Binary to Hexadecimal
def binary_to_hex(binary_number):
    decimal = binary_to_decimal(binary_number)
    if isinstance(decimal, int):
        return decimal_to_hex(decimal)
    return decimal

# Convert Octal to Binary
def octal_to_binary(octal_number):
    decimal = octal_to_decimal(octal_number)
    if isinstance(decimal, int):
        return decimal_to_binary(decimal)
    return decimal

# Convert Octal to Hexadecimal
def octal_to_hex(octal_number):
    decimal = octal_to_decimal(octal_number)
    if isinstance(decimal, int):
        return decimal_to_hex(decimal)
    return decimal

# Convert Hexadecimal to Binary
def hex_to_binary(hex_number):
    decimal = hex_to_decimal(hex_number)
    if isinstance(decimal, int):
        return decimal_to_binary(decimal)
    return decimal

# Convert Hexadecimal to Octal
def hex_to_octal(hex_number):
    decimal = hex_to_decimal(hex_number)
    if isinstance(decimal, int):
        return decimal_to_octal(decimal)
    return decimal

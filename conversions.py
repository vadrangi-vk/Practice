import number_system_conversion as nsc

# Display options
print("---------------NUMBER SYSTEM CONVERSION---------------")
print("Enter:")
print("1 for binary to decimal", "2 for binary to octal", "3 for binary to hexadecimal", sep=" ")
print("4 for decimal to binary", "5 for decimal to octal", "6 for decimal to hexadecimal", sep=" ")
print("7 for octal to binary", "8 for octal to decimal", "9 for octal to hexadecimal", sep=" ")
print("10 for hexadecimal to binary", "11 for hexadecimal to decimal", "12 for hexadecimal to octal", sep=" ")

# Get the user's choice
choice = int(input("Enter choice: "))
n = input("Enter the input accordingly: ")

# Perform the conversion based on user's choice using if-elif-else
if choice == 1:
    print("The result is:", nsc.binary_to_decimal(n))
elif choice == 2:
    print("The result is:", nsc.binary_to_octal(n))
elif choice == 3:
    print("The result is:", nsc.binary_to_hex(n))
elif choice == 4:
    print("The result is:", nsc.decimal_to_binary(n))
elif choice == 5:
    print("The result is:", nsc.decimal_to_octal(n))
elif choice == 6:
    print("The result is:", nsc.decimal_to_hex(n))
elif choice == 7:
    print("The result is:", nsc.octal_to_binary(n))
elif choice == 8:
    print("The result is:", nsc.octal_to_decimal(n))
elif choice == 9:
    print("The result is:", nsc.octal_to_hex(n))
elif choice == 10:
    print("The result is:", nsc.hex_to_binary(n))
elif choice == 11:
    print("The result is:", nsc.hex_to_decimal(n))
elif choice == 12:
    print("The result is:", nsc.hex_to_octal(n))
else:
    print("Invalid choice, please enter a valid number between 1 and 12.")

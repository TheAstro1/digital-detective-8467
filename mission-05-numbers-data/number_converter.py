#Convert a decimal integer to its binary and hexadecimal representations.


def main():
    value = input("Decimal number: ")

    try:
        number = int(value)
        
    except ValueError:
        print("Please enter a valid whole number.")
        return

    print(f"Binary: {bin(number)}")
    print(f"Hexadecimal: {hex(number)}")

main()

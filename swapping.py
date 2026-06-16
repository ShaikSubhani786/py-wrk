

def swap(a, b, choice):

    if choice == 1:
        # Method 1: Using Temporary Variable
        temp = a
        a = b
        b = temp
        print("Method: Temporary Variable")

    elif choice == 2:
        # Method 2: Using Addition and Subtraction
        a = a + b
        b = a - b
        a = a - b
        print("Method: Addition & Subtraction")

    elif choice == 3:
        # Method 3: Using Multiplication and Division
        if a == 0 or b == 0:
            print("Cannot use this method when a or b is 0!")
            return
        a = a * b
        b = a // b
        a = a // b
        print("Method: Multiplication & Division")

    elif choice == 4:
        # Method 4: Using XOR Bitwise Operator
        a = a ^ b
        b = a ^ b
        a = a ^ b
        print("Method: XOR Bitwise Operator")

    elif choice == 5:
        # Method 5: Python Tuple Unpacking
        a, b = b, a
        print("Method: Python Tuple Unpacking")

    else:
        print("Invalid choice!")
        return

    print("After Swap: a =", a, ", b =", b)


# ---- Main Program ----

print("Number Swapping Program")

a = int(input("Enter first number  (a): "))
b = int(input("Enter second number (b): "))

print("\nBefore Swap: a =", a, ", b =", b)

print("\nChoose a swapping method:")
print("1. Temporary Variable")
print("2. Addition & Subtraction")
print("3. Multiplication & Division")
print("4. XOR Bitwise Operator")
print("5. Python Tuple Unpacking")

choice = int(input("\nEnter your choice (1-5): "))

swap(a, b, choice)

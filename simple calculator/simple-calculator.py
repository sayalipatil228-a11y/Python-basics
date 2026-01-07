num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print('''Choose an operation : 
            + Addition
            - Subtraction
            * Multiplication
            / Division''')

choice = input("Enter operation (+, -, *, /): ")

if choice == '+':
    print("Result: ", num1 + num2)
elif choice == '-':
    print("Result: ", num1 - num2)
elif choice == '*':
    print("Result: ", num1 * num2)
elif choice == '/':
    if num2 != 0:
        print("Result: ", num1 / num2)
    else:
        print("Error: Division by zero is not allowed.")

else:
    print("Invalid operation selected.")
#This is a simple calculator program that performs basic arithmetic opetations😊
num_1 = float(input("Enter the first number:"))
num_2 = float(input("Enter the second number:"))

# Get the operation from the user
operation = input("Enter the operation (+, -, *, /):")

# Perform the operation based on user input
if operation == '+':
    result = num_1 + num_2
    print(f"{num_1} + {num_2} = {result}")

elif operation == '-':
    result = num_1 - num_2
    print(f"{num_1} - {num_2} = {result}")

elif operation == '*':
    result = num_1 * num_2
    print(f"{num_1} * {num_2} = {result}")

elif operation == '/':
    if num_2 != 0:
        result = num_1 / num_2
        print(f"{num_1} / {num_2} = {result}")
    else:
        print("Error! Division by zero.")

else:
    print("Operation is not valid!")

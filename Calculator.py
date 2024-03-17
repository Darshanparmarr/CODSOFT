def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Cannot divide by zero."

def calculator():
    print("Simple Calculator")
    print("Operations:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operation = input("Enter operation (1/2/3/4): ")

        if operation in ('1', '2', '3', '4'):
            if operation == '1':
                result = add(num1, num2)
                print(f"Result: {result}")
            elif operation == '2':
                result = subtract(num1, num2)
                print(f"Result: {result}")
            elif operation == '3':
                result = multiply(num1, num2)
                print(f"Result: {result}")
            elif operation == '4':
                result = divide(num1, num2)
                print(f"Result: {result}")
        else:
            print("Invalid operation. Please enter a valid operation (1/2/3/4).")

    except ValueError:
        print("Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    calculator()

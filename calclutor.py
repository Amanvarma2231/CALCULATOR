def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

def calculator():
    print("Simple Calculator")
    print("Operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    while True:
        try:
            choice = int(input("Enter operation choice (1-4): "))
            if choice not in [1, 2, 3, 4]:
                print("Invalid choice. Please enter a number between 1 and 4.")
                continue

            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == 1:
                print(f"Result: {add(num1, num2)}")
            elif choice == 2:
                print(f"Result: {subtract(num1, num2)}")
            elif choice == 3:
                print(f"Result: {multiply(num1, num2)}")
            elif choice == 4:
                print(f"Result: {divide(num1, num2)}")

            another = input("Do another calculation? (y/n): ")
            if another.lower() != 'y':
                break

        except ValueError:
            print("Invalid input. Please enter valid numbers.")
        except Exception as e:
            print(f"An error occurred: {e}")

    print("Thank you for using the calculator!")

if __name__ == "__main__":
    calculator()
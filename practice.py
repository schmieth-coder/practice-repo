# Import the operator module for mathematical operations
# This library provides functions for standard operators as functions
import operator

# Define the main calculator function
# This function takes two numbers and an operation, then returns the result
def calculator(num1, num2, operation):
    # Dictionary mapping operation symbols to operator functions
    # This allows us to look up the correct function based on user input
    operations = {
        '+': operator.add,      # Addition
        '-': operator.sub,      # Subtraction
        '*': operator.mul,      # Multiplication
        '/': operator.truediv,  # Division (returns float)
        '**': operator.pow,     # Exponentiation
        '%': operator.mod       # Modulo (remainder)
    }

    # Check if the operation exists in our dictionary
    if operation in operations:
        # Call the appropriate operator function and return the result
        return operations[operation](num1, num2)
    else:
        # Return error message for invalid operations
        return "Invalid operation"

# Main program execution starts here
if __name__ == "__main__":
    # Display welcome message to user
    print("=== Simple Calculator ===")

    # Get first number from user and convert to float
    num1 = float(input("Enter first number: "))

    # Get operation symbol from user
    operation = input("Enter operation (+, -, *, /, **, %): ")

    # Get second number from user and convert to float
    num2 = float(input("Enter second number: "))

    # Call calculator function with user inputs
    result = calculator(num1, num2, operation)

    # Display the result to the user
    print(f"Result: {num1} {operation} {num2} = {result}")
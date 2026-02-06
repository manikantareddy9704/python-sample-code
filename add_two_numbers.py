"""Simple program to add two numbers."""

def add_two_numbers(first_number: float, second_number: float) -> float:
    """Return the sum of two numbers."""
    return first_number + second_number


if __name__ == "__main__":
    first_input = float(input("Enter the first number: "))
    second_input = float(input("Enter the second number: "))
    print(f"Sum: {add_two_numbers(first_input, second_input)}")

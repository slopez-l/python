import sys  # To access arguments passed from the command line.


def process_argument():
    args = sys.argv[1:]  # Get all arguments except the script name (index 0).

    try:
        if not args:
            exit()  # Exit silently if no arguments are provided.

        # If more than one argument is provided.
        # Raise a custom error message.
        if len(args) > 1:
            raise AssertionError("more than one argument are provided")

        # If the argument is not a valid integer (allows "+" or "-" prefixes).
        # Raise error if argument is not an integer.
        if not args[0].lstrip("+-").isdigit():
            raise AssertionError("argument is not an integer")

        number = int(args[0])  # Convert the argument to an integer.

        if number % 2 == 0:  # If the number is divisible by 2.
            print("I'm Even.")
        else:
            print("I'm Odd.")

    # Print only the error message, without full traceback.
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    process_argument()

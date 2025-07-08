"""
Counts different types of characters in a given string:
uppercase letters, lowercase letters, punctuation, spaces and digits.
"""

import sys
import string


def analyze_text(text):
    """
    Analyzes the given text and returns a dictionary with counts:
    uppercase, lowercase, punctuation, spaces, and digits.
    """
    return {
        "total": len(text),
        "upper": sum(1 for c in text if c.isupper()),
        "lower": sum(1 for c in text if c.islower()),
        "punctuation": sum(1 for c in text if c in string.punctuation),
        "spaces": sum(1 for c in text if c.isspace()),
        "digits": sum(1 for c in text if c.isdigit()),
    }


def main():
    """
    Entry point of the program.
    Handles input arguments, error conditions, and prints character counts.
    """
    try:
        args = sys.argv[1:]

        if len(args) > 1:
            raise AssertionError("more than one argument are provided")

        if args:
            texto = args[0]

        else:
            print("What is the text to count?")
            # Reads a full line until the user presses Enter.
            # includes the line break (\n) at the end of the text.
            texto = sys.stdin.readline()

        result = analyze_text(texto)

        print(f"The text contains {result['total']} characters:")
        print(f"{result['upper']} upper letters")
        print(f"{result['lower']} lower letters")
        print(f"{result['punctuation']} punctuation marks")
        print(f"{result['spaces']} spaces")
        print(f"{result['digits']} digits")

    except AssertionError as err:
        print(f"AssertionError: {err}")
    except Exception as err:
        print(f"Unexpected error: {err}")


if __name__ == "__main__":
    main()

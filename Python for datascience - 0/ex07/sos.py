import sys

# Dictionary that maps each letter, number,
# and space to its Morse code equivalent.
NESTED_MORSE = {
    "A": ".- ",
    "B": "-... ",
    "C": "-.-. ",
    "D": "-.. ",
    "E": ". ",
    "F": "..-. ",
    "G": "--. ",
    "H": ".... ",
    "I": ".. ",
    "J": ".--- ",
    "K": "-.- ",
    "L": ".-.. ",
    "M": "-- ",
    "N": "-. ",
    "O": "--- ",
    "P": ".--. ",
    "Q": "--.- ",
    "R": ".-. ",
    "S": "... ",
    "T": "- ",
    "U": "..- ",
    "V": "...- ",
    "W": ".-- ",
    "X": "-..- ",
    "Y": "-.-- ",
    "Z": "--.. ",
    "0": "----- ",
    "1": ".---- ",
    "2": "..--- ",
    "3": "...-- ",
    "4": "....- ",
    "5": "..... ",
    "6": "-.... ",
    "7": "--... ",
    "8": "---.. ",
    "9": "----. ",
    " ": "/ "
}


def main():
    """
    Main function of the program.
    Converts a text string into Morse code
    using the NESTED_MORSE dictionary.
    Only letters, numbers, and spaces are allowed.
    """
    try:
        args = sys.argv[1:]

        if len(args) != 1:
            raise AssertionError("the arguments are bad")

        # Converts the text to uppercase so it matches
        # the keys in the dictionary.
        text = args[0].upper()

        # Verifies that all characters in the text are
        # present in the Morse dictionary.
        if not all(c in NESTED_MORSE for c in text):
            raise AssertionError("the arguments are bad")

        # Converts each character to Morse and joins them with spaces
        morse = ' '.join(NESTED_MORSE[c] for c in text)
        print(morse)  # Prints the result in Morse code

    except AssertionError as e:
        print(f"AssertionError: {e}")
    except Exception:
        print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    main()

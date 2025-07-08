import sys
# We import our custom version of filter.
from ft_filter import ft_filter


def main():
    """
    Program that accepts a string and a number as arguments,
    and displays the words from the string whose length is
    greater than the number.
    """
    try:
        args = sys.argv[1:]

        if len(args) != 2:
            raise AssertionError("the arguments are bad")

        texto, numeros = args[0], args[1]

        if not numeros.isdigit():
            raise AssertionError("the arguments are bad")

        n = int(numeros)
        palabras = texto.split()  # We split the text into words by spaces

        # We use a lambda directly inside ft_filter
        # to filter out long words.
        filtro = list(ft_filter(lambda p: len(p) > n, palabras))

        print(filtro)

    except AssertionError as e:
        print(f"AssertionError: {e}")
    # Catches any other unexpected error.
    except Exception:
        print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    main()  # Entry point of the program.

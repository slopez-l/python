""" Imports the datetime class from the datetime module
 (used for working with current date and time)."""
from datetime import datetime
# Imports the time module (used to get time as a timestamp)
import time

""" Gets the number of seconds since January 1, 1970 (Epoch time)
 and stores it in current_timestamp."""
current_timestamp = time.time()

"""Gets the current date and time, and formats it as a string:
 abbreviated month, day, year."""
current_date = datetime.now().strftime("%b %d %Y")

# Prints the number of seconds since 1970 in two formats:
# - decimal format with thousand separators and 4 decimal places
# - scientific notation with 2 decimal places
print(
    f"Seconds since January 1, 1970: {current_timestamp:,.4f}"
    f"or {current_timestamp:.2e} in scientific notation"
    )

print(current_date)  # Prints the formatted current date, e.g.: "Jul 01 2025"

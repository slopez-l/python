from datetime import datetime
from time import time

seconds = time()
print(f"Seconds since January 1, 1970: {seconds:.4f} or {seconds:.2e}")

now = datetime.now()
print(now.strftime("%b %d %Y"))

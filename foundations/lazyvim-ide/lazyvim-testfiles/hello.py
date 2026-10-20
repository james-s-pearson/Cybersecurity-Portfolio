"""Test script for the Python runner (F5 in an IPython terminal).

Safe and self-contained: no input, no files, no network.
"""

import sys
from datetime import datetime

print("--- Python Runner Test Start ---")
print("Status: Success")
print(f"Python Version: {sys.version.split()[0]}")
print(f"Current Timestamp: {datetime.now().isoformat(timespec='seconds')}")


def add(a, b):
    return a + b


num1 = 5
num2 = 10
result = add(num1, num2)
print(f"Math Check: {num1} + {num2} = {result}")
print("Logic Check: PASSED" if result == 15 else "Logic Check: FAILED")

# Uncomment the next line to see how your runner shows an error.
# raise ValueError("Intentional test error")

print("--- Python Runner Test End ---")

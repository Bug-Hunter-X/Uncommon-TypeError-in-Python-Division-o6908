# Uncommon TypeError in Python Division

This repository demonstrates an uncommon TypeError that can occur in Python when performing division.  The code attempts to divide a string by an integer, resulting in a TypeError instead of the expected ZeroDivisionError. This is a subtle bug that can be difficult to track down, especially if the developer is only expecting a ZeroDivisionError. The solution provides a more robust error-handling approach, which is useful in cases with multiple exception types that needs to be handled.

## How to run the code

1. Clone this repository.
2. Run the `bug.py` file to see the unexpected TypeError.
3. Run the `bugSolution.py` file to see the corrected handling of exceptions.
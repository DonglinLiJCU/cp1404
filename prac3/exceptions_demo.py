"""
CP1404 - Practical
Answer the following questions:
1. When will a ValueError occur?
    When input is not a number a ValueError will occur.
2. When will a ZeroDivisionError occur?
    When denominator is 0 a ZeroDivisionError will occur
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        denominator = int(input("denominator can't be 0, enter another one: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")


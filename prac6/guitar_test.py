"""
Guitar test
Estimate: 5 minutes
Actual:   4 minutes
"""

from prac6.guitar import Guitar

guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.4)
guitar2 = Guitar("Another Guitar", 2013)


def main():
    print(test("get_age", guitar1, 100))
    print(test("get_age", guitar2, 9))
    print(test("is_vintage", guitar1, True))
    print(test("is_vintage", guitar2, False))


def test(method, guitar, expected):
    if method == "get_age":
        return f"{guitar.name} {method}() - Expected {expected}. Got {guitar.get_age()}"
    elif method == "is_vintage":
        return f"{guitar.name} {method}() - Expected {expected}. Got {guitar.is_vintage()}"


main()

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']


def main():
    numbers = []
    for i in range(5):
        num = int(input("Number: "))
        numbers.append(num)
    result = analyse(numbers)
    print(f"The first number is {result[0]}")
    print(f"The last number is {result[1]}")
    print(f"The smallest number is {result[2]}")
    print(f"The largest number is {result[3]}")
    print(f"The average of the numbers is {result[4]}")

    username = input("Please enter your username: ")
    if username in usernames:
        print("Access granted")
    else:
        print("Access denied")


def analyse(numbers):
    return numbers[0], numbers[-1], min(numbers), max(numbers), sum(numbers) / len(numbers)


main()

import random


def main():
    cnt = int(input("How many quick picks? "))
    for i in range(cnt):
        numbers = generate_picks()
        for numbers in numbers:
            print(f"{numbers:>2}", end=' ')
        print()


def generate_picks():
    numbers = []
    for i in range(6):
        tmp = random.randint(1, 45)
        while tmp in numbers:
            tmp = random.randint(1, 45)
        numbers.append(tmp)
    numbers.sort()
    return numbers


main()

def main():
    password = get_password()
    print_star(password)


def get_password():
    min_length = 10
    passwd = input("Please enter your password: ")
    while len(passwd) < min_length:
        print("Password length doesn't meet the minimum length!")
        passwd = input("Please enter your password: ")
    return passwd


def print_star(passwd):
    for i in range(len(passwd)):
        print("*", end='')
    print()


main()

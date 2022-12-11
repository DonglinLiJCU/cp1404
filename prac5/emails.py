"""
Emails
Estimate: 10 minutes
Actual:   15 minutes
"""

email_name = {}


def main():
    email = input("Email: ")
    while email != "":
        choice = input(f"Is your name {analyse_name(email)}? (Y/n) ")
        if str.upper(choice) == 'Y' or choice == '':
            email_name[email] = analyse_name(email)
        else:
            name = input("Name: ")
            email_name[email] = name
        email = input("Email: ")
    print()
    for item in email_name.items():
        print(f"{item[1]} ({item[0]})")


def analyse_name(email: str):
    tmp = email[:email.find('@')].split('.')
    name = ' '.join(tmp).title()
    return name


main()

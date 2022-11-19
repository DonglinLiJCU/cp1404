def main():
    score = float(input("Enter your score: "))
    MENU = """(G)et a valid score
    (P)rint result
    (S)how stars
    (Q)uit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != 'Q':
        if choice == 'G':
            score = float(input("Enter your score: "))
        elif choice == 'P':
            print(cal_rank(score))
        elif choice == 'S':
            print(show_stars(score))
        else:
            print("Invalid choice")
        choice = input(">>> ").upper()
    print("Finished.")


def cal_rank(score):
    if 0 <= score <= 100:
        if score < 50:
            return "Bad"
        elif score < 90:
            return "Pass"
        else:
            return "Excellent"
    else:
        return "Invalid score"


def show_stars(score):
    stars = str()
    for i in range(int(score)):
        stars += '*'
    return stars


main()

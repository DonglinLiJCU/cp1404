import random


def main():
    score = float(input("Enter score: "))
    print(cal_rank(score))
    random_score = random.uniform(0, 100)
    print(f"Your random score is {random_score:.2f}")
    print(cal_rank(random_score))


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


main()

"""
CP1404 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    month_cnt = int(input("How many months? "))

    for month in range(1, month_cnt + 1):
        income = float(input(f"Enter income for month {str(month)}: "))
        incomes.append(income)

    print("\nIncome Report\n-------------")
    out = print_report(incomes, month_cnt)
    for i in out:
        print(i)


def print_report(incomes, month_cnt):
    total = 0
    out = []
    for month in range(1, month_cnt + 1):
        income = incomes[month - 1]
        total += income
        out.append("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))
    return out


main()

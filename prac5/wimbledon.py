"""
Wimbledon
Estimate: 15 minutes
Actual:   18 minutes
"""

countries = set()
champions = {}


def main():
    with open('wimbledon.csv', "r", encoding="utf-8-sig") as in_file:
        lines = in_file.readlines()[1:]
    for line in lines:
        result = analyse(line)
        cal_champion(result[0], result[1])

    for item in champions.items():
        print(f"{item[0]} {item[1]}")

    print()
    print(countries_count())


def analyse(line: str):
    tmp = line.split(",")
    country = tmp[1]
    name = tmp[2]
    return country, name


def cal_champion(country, name):
    if country not in countries:
        countries.add(country)
    if name in champions:
        champions[name] += 1
    else:
        champions[name] = 1


def countries_count():
    countries_out = []
    for country in countries:
        countries_out.append(country)
    countries_out.sort()
    return ", ".join(countries_out)


main()

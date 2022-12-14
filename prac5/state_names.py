"""
CP1404 Practical
State names in a dictionary
File needs reformatting
"""

CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(CODE_TO_NAME)

state_code = input("Enter short state: ")
while state_code != "":
    try:
        print(state_code, "is", CODE_TO_NAME[str.upper(state_code)])
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ")

    # if str.upper(state_code) in CODE_TO_NAME:
    #     print(state_code, "is", CODE_TO_NAME[str.upper(state_code)])
    # else:
    #     print("Invalid short state")
    # state_code = input("Enter short state: ")

for item in CODE_TO_NAME.items():
    print(f"{item[0]:<3} is {item[1]}")

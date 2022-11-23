CODE_TO_HEX_COLOR = {"ABSOLUTE ZERO": "#0048ba", "ACID GREEN": "#b0bf1a", "ALICEBLUE": "#f0f8ff",
                     "ALIZARIN CRIMSON": "#e32636",
                     "AMARANTH": "#e52b50", "AMBER": "#ffbf00", "AMETHYST": "#9966cc", "ANTIQUEWHITE": "#faebd7",
                     "ANTIQUEWHITE1": "#ffefdb"}

color_name = input("Enter color name: ")
while color_name != "":
    try:
        print(color_name, "is", CODE_TO_HEX_COLOR[str.upper(color_name)])
    except KeyError:
        print("Invalid color name")
    color_name = input("Enter color name: ")

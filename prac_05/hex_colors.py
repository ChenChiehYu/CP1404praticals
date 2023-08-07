CODE_TO_COLOR = {"AMBER": "#ffbf00",
                 "ANTIQUEWHITE": "#faebd7",
                 "AQUA": "#00ffff",
                 "BLACK": "#000000",
                 "CAMEL": "#c19a6b",
                 "EGGPLANT": "#614051",
                 "EMERALD": "#50c878",
                 "GRAY": "#bebebe",
                 "ICEBERG": "#71a6d2",
                 "IRIS": "#5a4fcf"
                 }
print(CODE_TO_COLOR)

color_code = input("Enter a color name: ")
while color_code != "":
    color_code = color_code.upper()
    if color_code in CODE_TO_COLOR:
        print(color_code, " is ", CODE_TO_COLOR[color_code])
    else:
        print("Invalid color name")
    color_code = input("Enter a color name: ")

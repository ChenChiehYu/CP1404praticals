from prac_06.guitar import Guitar

name = "1"
print("My guitars!")
guitars = []
i = 0
while True:
    name = input("Name: ")
    if name == "":
        break
    year = input("Year: ")
    cost = input("Cost: $")
    guitars.append(Guitar(name, year, cost))
    print(guitars[i], " added.")
    i += 1

print("These are my guitars:")
i = 0
for objects in guitars:
    vintage_string = "(vintage)" if objects.is_vintage() else ""
    print(f"Guitar {i + 1}: {objects.name:>20} ({objects.year}), worth ${float(objects.cost):10,.2f} {vintage_string}")
    i += 1

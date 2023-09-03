from guitar import Guitar

guitars = []

in_file = open('guitars.csv', 'r')
files = in_file.read().splitlines()
in_file.close()
for line in files:
    parts = line.strip().split(',')
    guita = Guitar(parts[0], parts[1], parts[2])
    guitars.append(guita)
    print("added {}".format(line))

# Complete first part of More Guitars exercise

print("Add your Guitar")
name = "1"
i = 0
while True:
    name = input("Name: ")
    if name == "":
        break
    year = input("Year: ")
    cost = input("Cost: $")
    guitars.append(Guitar(name, year, cost))
    print(f"{name:25} ({year}) : ${float(cost):5.2f} added.")
    i += 1

in_file = open('guitars.csv', 'w')
i = 0
for line in sorted(guitars):
    print(line)
    guitar = line.name + "," + line.year + "," + str(line.cost)
    if i < len(guitars) - 1:
        guitar += "\n"
    in_file.write(guitar)
    i += 1
in_file.close()
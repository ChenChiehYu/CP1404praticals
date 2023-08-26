from prac_06.guitar import Guitar
name = "Gibson L-5 CES"
year = 1922
cost = 16035.40

gibson = Guitar(name, year, cost)
another = Guitar("Another Guitar", 2013, 100)
print(f"{gibson.name} get_age() - Excepted 101. Get {gibson.get_age()}")
print(f"{another.name} get_age() - Excepted 10. Get {another.get_age()}")
print(f"{gibson.name} is_vintage() - Excepted Ture. Get {gibson.is_vintage()}")
print(f"{another.name} is_vintage() - Excepted False. Get {another.is_vintage()}")


"""
CP1404/CP5632 - Practical
shop calculator
"""
items = int(input("Number of items: "))
while(items<0):
    print("Invalid number of items!")
    items = int(input("Number of items: "))
total = 0
for i in range(items):
    price = float(input("Price of item: "))
    total += price
if total>=100:
    total=total*0.9
print(f"Total price for {items} items is ${total:.2f}")
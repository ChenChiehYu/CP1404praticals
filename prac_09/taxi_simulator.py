from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"
taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
print("Let's drive!")
print(MENU)
user_input = input().lower()
total_fee = 0.00
current_taxi = None
while user_input != "q":
    if user_input == "d":
        if current_taxi is None:
            print("You need to choose a taxi before you can drive")
        else:
            distance = int(input("Drive how far? "))
            taxis[current_taxi].drive(distance)
            taxis[current_taxi].fuel
            print(f"Your {taxis[current_taxi].name} trip cost you ${taxis[current_taxi].get_fare():.2f}")
            total_fee += taxis[current_taxi].get_fare()
            taxis[current_taxi].start_fare()
    elif user_input == "c":
        i = 0
        print("Taxis available: ")
        for taxi in taxis:
            print(f"{i} - {taxi}")
            i += 1
        current_taxi = int(input("Choose taxi: "))
        if current_taxi >= len(taxis):
            print("Invalid taxi choice")
    else:
        print("Invalid option")
    print(f"Bill to date: ${total_fee:.2f}")
    print(MENU)
    user_input = input().lower()

i = 0
print(f"Total trip cost: ${total_fee}")
print("Taxis are now:")
for taxi in taxis:
    print(f"{i} - {taxi}")
    i += 1

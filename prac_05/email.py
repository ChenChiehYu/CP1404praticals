EMAILS = dict()

user_email = input("Email: ")
while user_email != "":
    user_name = user_email.split("@")[0]
    option = input(f"Is your name {user_name}? (Y/n)").lower()
    if option == "y" or option == "":
        user_email = input("Email: ")
    else:
        user_name=input("Name: ")

EMAILS = dict()
user_email = input("Email: ")
while user_email != "":
    user_name = user_email.split("@")[0]
    symbol = " "
    user_name= user_name.split(".")
    user_name= symbol.join(user_name)
    option = input(f"Is your name {user_name}? (Y/n)").lower()
    EMAILS[user_email]=user_name.title()
    if option == "y" or option == "":
        user_email = input("Email: ")
    else:
        user_name=input("Name: ")
        EMAILS[user_email]=user_name.title()
        user_email = input("Email: ")
for key in EMAILS:
    print(EMAILS[key], f"({key})")
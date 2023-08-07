EMAILS = dict()

user_email=input("Email: ")
while user_email != "":
    last_name = user_email.split("@")[0]
    print(f"Is your name {last_name}? (Y/n)")
    user_email=input("Email: ")
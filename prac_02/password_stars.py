MIN_LEN = 5
def main():
    input_password = get_password()
    method_name(input_password)


def method_name(input_password):
    print(len(input_password) * "*")


def get_password():
    input_password = input("Enter your password: ")
    while len(input_password) < MIN_LEN:
        print("Invalid length")
        input_password = input("Enter your password: ")
    return input_password


main()

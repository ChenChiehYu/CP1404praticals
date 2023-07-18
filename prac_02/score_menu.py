"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""
MIN_SCORE=0
MAX_SCORE=100
def main():
    print(MENU)
    score = get_score()
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score=get_score()
        elif choice == "P":
            print(get_result(score))
        elif choice == "S":
            print(score*"*")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("See you")


def get_score():
    score = float(input("Enter score: "))
    while score<MIN_SCORE or score>MAX_SCORE:
        print("Invalid Score")
        score = float(input("Enter score: "))
    return score

def get_result(score):
    if score < 0 or score>100:
        result= str("Invalid score")
    elif score >= 50:
        result= str("Passable")
    elif score >= 90:
        result= str("Excellent")
    else:
        result= str("Bad")
    return result

main()
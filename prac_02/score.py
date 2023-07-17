"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

def main():
    score = get_score()
    print(get_result(score))

def get_score():
    score = float(input("Enter your score: "))
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
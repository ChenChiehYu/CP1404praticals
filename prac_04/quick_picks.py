import random

MIN_NUM = 1
MAX_NUM = 45
numbers=[]
number_list = []
lines = int(input("How many quick picks? "))
for j in range(MIN_NUM, MAX_NUM + 1):
    number_list.append(j)
for i in range(0,lines):
    random.shuffle(number_list)
    numbers = number_list[:6]
    print("{:2} {:2} {:2} {:2} {:2} {:2} ".format(numbers[0],numbers[1],numbers[2],numbers[3],numbers[4],numbers[5]))




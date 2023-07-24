NAME_FILE= "name.txt"
NUMBER_FILE= "number.txt"

input_name = input("Enter your name: ")
out_file = open(NAME_FILE, 'w')
out_file.write(input_name)
out_file.close()

input_file = open(NAME_FILE, 'r')
name = input_file.read()
print(f"Your name is {name}")
input_file.close()

input_file = open(NUMBER_FILE,'r')
number = input_file.readlines()
print(int(number[0])+int(number[1]))
input_file.close()

input_file=open(NUMBER_FILE,'r')
result = 0
lines = input_file.readlines()
for line in lines:
    if line.strip():
        result+=1
input_file.close()
print(f"There's {result} lines in this file")
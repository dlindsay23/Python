# Devin Lindsay
# A02235901


# 3.4
# created a nested for loop that prints two lines of 7 @ symbols

for i in range(2):
    for j in range(7):
        print('@', end="")
    print()


# # 3.9
# # Get user input, get length and turn input into int

entry = input("Enter a number 7 to 10 digits: ")
length = len(entry)
num = int(entry)

# # create loop subtract length each time and print the number. 
# # The // starts with the first number and adds the next number each iteration and % takes the number on the right allowing to single out number.

for i in range(length):
    length -= 1
    print((num // 10 ** (length)) % 10)
    

# # 3.11
# # Set variables, get user inputs and set condition that if -1 break loop

gallons = 0
total_miles = 0
total_gallons = 0

while gallons != -1:
    
    gallons = eval(input("Enter the gallons used (-1 to end): "))
    if gallons == -1:
        break
    miles = eval(input("Enter the miles driven: "))
    
# # Get the miles/gallon and well as totals for miles and gallons and display results needed

    tank = miles / gallons
    total_miles += miles
    total_gallons += gallons
    
    print("The miles/gallon for this tank was " + str(round(tank, 6)))
    
avg_tank = total_miles / total_gallons
print("The overall average miles/gallon was " + str(round(avg_tank, 6)))
    


# # 3.12
# # get user input, determine if palindrom by making bolean statements that test the first and last number and middle numbers to see if they are the same
# # Print result

integer = int(input("Enter a 5 digit integer: "))


first_last_num = (integer // 10000) == (integer // 1 % 10)
middle_numbers = (integer // 1000 % 10) == (integer // 10 % 10)

if first_last_num and middle_numbers:
    print("Palindrome!!!")
else:
    print("Not a palindrome...")

# # 3.14
# # calculate for pi using a for loop and step by 2 for the denominator. Use the variable pi to get a cummunialtive pi 
# # and use n stepping by 1 to determine if to add or subtract if it's odd or even
# # First get 3.14 when n is 627 and 628
# # 3.141 when n is 2454 and 2455

# pi = 0
# n = 1
# for i in range(1, 6000, 2):
#     if n % 2 == 1:
#         pi += 4/(i)
#     else:
#         pi -= 4/(i)
#     n += 1
# print(pi)
    
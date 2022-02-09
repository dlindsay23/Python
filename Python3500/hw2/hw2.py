# Q 2.3
# Demonstrate an if statement

grade = 91

if grade >= 90:
    print("Congratulations! Your grade of " + str(grade)  + " earns you an A in this course")
    
    
# Q 2.4
# Demonstrate different algorithms

print("\n")
print(27.5 + 2)
print(27.5 - 2)
print(27.5 * 2)
print(27.5 / 2)
print(27.5 // 2)
print(27.5 ** 2)


# Q 2.5
# Combining algorithms and text into a print statement.

radius = 2

diameter = 2 * radius
circumference = 2 * 3.14159 * radius
area = 3.14159 * radius ** 2

print("\nDiameter: " + str(diameter) + "\nCircumference: " + str(circumference) + "\nArea: " + str(area))



# Q 2.6
# Get input and determine if odd or even

num = eval(input("\nInput a number: "))

num1 = num % 2


if num1 == 0:
    print("Even")
else:
    print("Odd")
 
    
# Q 2.7
# Use if statements to determine if numbers are multiples

print("\n")
if 1024 % 4 == 0:
    print("1024 is a multiple of 4")
else: 
    print("1024 is not a multiple of 4")
    
if 2 % 10 == 0:
    print("2 is a multiple of 10")
else: 
    print("2 is not a multiple of 10")



# Q 2.8
# Use a for loop to demonstrate simple formatting

print("\nnumber\tsquare\tcube")
    
for i in range(6):
    square = i ** 2
    cube = i ** 3
    
    print(str(i) + "\t" + str(square) + "\t" + str(cube))
    
    

# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter a second number: "))


# table = []

# for i in range(num1):
#     table.append([])


# for number in range(1,num2):
#     for j in range(1,num1+1):
#         value = number * j
#         table[number-1].append(value)
# print(table)

done = False

while not done:
    
    choice = int(input("Enter choice: "))
    
    if choice == 1:
        name = input("enter a name or press enter when done: ")
        while name != "":
            if name != "" and len(name) < 30:
                print("saved")
            else:
                print("Enter a valid name")
            name = input("enter a name or press enter when done: ")
        
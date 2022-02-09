
# num = int(input("Enter a 3 digit number: "))

# first_num = num // 100

# last_num = num % 10

# if first_num == last_num:
#     print("Palindrome!!!")
# else:
#     print("Not palindrome")
    
    

# x = 0
# for i in range(1, 1001):
#     x += 1/(2 ** i)
#     if x == 1.0:
#         print(i)
# print(x)


pi = 0
n = 1
for i in range(1, 3000, 2):
    if n % 2 == 1:
        pi += 4/(i)
    else:
        pi -= 4/(i)
    n += 1
print(pi)



# age = int(input("Childs Age: "))
# weight = int(input("Childs Weight: "))

# old_enough = (age >= 12)
# big_kid = (age == 11) and (weight > 90)
# very_big_kid = (age < 11) and (weight > 100)

# if old_enough:
#     print("You can right in the front")
# elif big_kid:
#     print("You can right in the front")
# elif very_big_kid:
#     print("You can right in the front")
# else:
#     print("Sorry no front seat for you")


   


from random import randint



# colors = ["red", "blue", "black"]


# for color in colors:
#     print("\n")
#     for letter in color:
#         print(letter)


    
# print("\n")
# lst = []

# for i in range(10):
#     lst.append(randint(0,100))

# for j in range(len(lst)):
#     before = lst[j - 1]
#     current = lst[j]
#     if j >= 0:
#         if before % 2 == 0 and current % 2 == 0:
#             print(str(before) + " and " + str(current) + " are even")

    
# print(lst)

# print("\n")
# lst_a = ["a", "b", "c", "d", "e", "f", "g"]

# print(lst_a[2:6])



######################################################################################


lst = open("Week7/adbe.txt").readlines()

for st in range(len(lst)):
    lst[st] = float(lst[st])

end = 0
start = 0
for i in range(1,len(lst),5):
    average = (lst[i] + lst[i-1] + lst[i-2] + lst[i-3] + lst[i-4])/5
    print(average)
    end += 5
    for j in lst[start:end]:
        print("j: ", j)
    start += 5    


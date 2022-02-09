import numpy
import random
# import json

# age = int(input("Age: "))
# favorite_color = input("Favorite Color: ")


# dictionary = {}
# dictionary["age"] = age
# dictionary["favorite_color"] = favorite_color

# for item in dictionary.keys():
#     print(item+":", dictionary[item])
    
    
# json.dump(dictionary, open("Week8/results.json" , "w"))

# dictionary1 = json.load(open("Week8/results.json"))




rand = numpy.random.randint(100, size=100)
print(rand)

print("")

np1 = numpy.zeros(100)

for i in range(100):
    np1[i] = random.randint(0,100)
    
print(np1)
        
print(int(-5/2))

lst = [1,2,3,4,5]
print(lst[4:1:-1])
# with open() as file:
#     file.write()

# import json

# name = input("Enter your name: ")
# color = input("Enter your favorite color: ")

# sentence = (name + "'s favorite color is " + color + "\n")

# with open("/home/ubuntu/environment/Week12/sentence.txt", "a") as file:
#     file.write(sentence)



# results = {"name" : "Devin", "Color" : "Blue", "Age" : 22 }

# json.dump(results, open("/home/ubuntu/environment/Week12/person.json", "w"), indent=4)

# dictionary = json.load(open("person.json"))

import numpy as np
import requests
import json

url = "https://api.datamuse.com/words?rel_trg=madison"

req1 = requests.get(url)

dct1 = json.loads(req1.text)

key1 = "word"
key2 = "score"

# print(dct1[][][])

for i in dct1:
    if i[key2] % 10 == 0:
        print(i)


        

    







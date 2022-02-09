# Program Activity #1

year = eval(input("What year were you born: "))

if year >= 1997:
    print("You are a Zoomer")
elif year >= 1981:
    print("You are a millenial")
elif year >= 1965:
    print("You are Gen X")
else:
    print("You are a Baby Boomer")
    

# Program activity #2

age = eval(input("What is your age: "))
year = 2021

while age >= 1:
    print("You were alive in year: " + str(year))
    age -= 1
    year -= 1
else:    
    print("You were born in year: " + str(year))
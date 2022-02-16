import random


done = False

while not done:
    
    print("\tWelcome to 'Guess My Number'!")
    print("\tI'm thinking of a number between 1 and 100.")
    print("\tTry to guess it in as few attempts as possible.\n")
    
    guess = 0
    number = random.randint(1,100)
    tries = 0
    
    while number != guess:
        
        guess = eval(input("Take a guess: "))
        tries += 1
        
        if guess > number:
            print("Lower ...")
        elif guess < number:
            print("Higher ...")
    
    print("You guessed it! The number was", number)
    print("And it only took you " + str(tries) + " tries!")
        
    done = input("Would you like to play again? (y/n) ")  
    
    if done == "y":
        done = False
    elif done == "n":
        done = True
from DeckOfCards import *
import time

# start game and create variable to keep going
print("Welcome to Blackjack")
done = False

while not done:
    
    # Create deck and print both the unshuffled and shuffled deck
    deck = DeckOfCards()
    deck.print_deck()
    deck.shuffle_deck()
    print()
    deck.print_deck()
    
    # Create list for cards and total for user
    users_card = []
    user_total = 0
    
    # Give user their first two cards and get value
    user_card = deck.get_card()
    user_total += user_card.val
    users_card.append(str(user_card))
    user_card = deck.get_card()
    user_total += user_card.val
    users_card.append(str(user_card))
    
    # create Variable to start users turn
    turn = False
    
    while not turn:
        # Show users score and ask if they want a hit
        print("\nYour Cards:")
        for card in users_card:
            print(card)
        print("Your current score:",user_total)
        
        choice = input("Would you like a hit(y/n): ")
        
        # if user wants hit give them another card if not continue to users turn
        if choice == "y":
            user_card = deck.get_card()
            users_card.append(str(user_card))
            user_total += user_card.val
            
            # If card is ace and would bust then make work 1
            if user_card.val == 11 and user_total > 21:
                user_total -= 10
            
        elif choice == "n":
            turn = True
        
        # If user goes over end turn and tell them they lost
        if user_total > 21:
            print("Sorry you busted")
            break
        
        # If user gets 21 they win
        if user_total == 21:
            break
    
    # Start dealers turn and create variables to keep track of cards and score 
    print("Dealers turn")
    
    dealers_cards = []
    dealers_total = 0
    
    # Give dealer cards and score and print it out
    dealer_card = deck.get_card()
    dealers_total += dealer_card.val
    dealers_cards.append(str(dealer_card))
    dealer_card = deck.get_card()
    dealers_total += dealer_card.val
    dealers_cards.append(str(dealer_card))
    print("\nDealers cards")
    for card in dealers_cards:
        print(card)
    print("Dealers Score:", dealers_total)

    # while dealers score is under 17 keep giving them cards and print them
    while dealers_total < 17:
        
        dealer_card = deck.get_card()
        dealers_total += dealer_card.val
        dealers_cards.append(str(dealer_card))
        time.sleep(2)
        
        print("\nDealers cards")
        for card in dealers_cards:
            print(card)
        print("Dealers Score:", dealers_total)
    
    # Give criteria on who wins the game 
    if dealers_total > user_total and dealers_total < 21:
        print("Dealer won")
    
    elif dealers_total < user_total and user_total < 21:
        print("Congrats, You Won!")
        
    elif user_total == 21:
        print("Congrats, You Won!")
    
    elif dealers_total == 21 and dealers_total > user_total:
        print("Dealer Won")
    
    elif dealers_total > 21 and user_total < 21:
        print("Congrats, You Won!")
    
    # Ask user if they want to play again 
    finished = input("\nWould you like to play again(y/n):")
    
    # If they want to play again start again
    if finished == "y":
        done = False
    elif finished == "n":
        done = True

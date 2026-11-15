import random
import sys
import pyfiglet
import time

def show_spinner(duration_seconds=5):
        spinner_chars =  ["|", "/", "-", "\\",]
        end_time = time.time() + duration_seconds
        i = 0

        print("Rolling the wheel...   ", end="", flush=True)
        while time.time() < end_time:
            sys.stdout.write(spinner_chars[i % len(spinner_chars)])
            sys.stdout.flush()
            time.sleep(0.1)
            sys.stdout.write("\b")
            i +=1

print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print("")
print("")

print(pyfiglet.figlet_format("Anish's  Casino"))
print("𝕐𝕠𝕦 𝕔𝕒𝕟 𝕖𝕚𝕥𝕙𝕖𝕣 𝕞 𝕒𝕜𝕖 𝕚𝕥 𝕒𝕝𝕝 𝕠𝕣 𝕝𝕠𝕤𝕖 𝕚𝕥 𝕒𝕝𝕝!")
#La peace bros
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print("____________________________________________________ ")

username = input("Enter your username: ")
captcha = input("Ok " + str(username) + ", now, lets make sure that you are human, type banana here, exactly as it is spelled: ")
if captcha == "banana":
    print("You have passed, you are human!")
    print("")

else: 
    print("You are a robot, you may not play my game.") 
    print("")
    sys.exit()

while True:
    try:
        userage = int(input("Enter your age. Use an age of at least 18: "))
        break  #hello, this is an easter egg ig bro
    except ValueError: 
        print("Invalid input. Please enter your age as a whole number without decimals or letters.")
if userage >= 18:
    print("Thank you for entering your age, you are allowed to play.")
    print(" ")
elif userage < 18:
    print("You aren't allowed to play, you must be 18 or older. I would never tell you to lie tho. ͡~ ͜ʖ ͡°")
    print("")
    sys.exit()

money = 1000

while True:
    print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print(pyfiglet.figlet_format("Home  Screen"))
    print(" ")
    print("Welcome " + username + ". Have a great time!")
    print("")
    print("")
    print("Current Balance: " + str(money) + "$ dollars.")
    print("")
    print("")
    print("")
    print("Owner: Just remember, if you are winning, keep on going, and if you are losing, keep trying, never give up.")

    game_choice = input("Your options are slot-machine, blackjack and roulette: ")

    if game_choice == "slot-machine":
        print("Starting slot-machine...")
        print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print(pyfiglet.figlet_format("Blackjack!"))
        print("")
        print("")
        print("")
        print("")
        print

    elif game_choice == "blackjack":
        print("Starting blackjack...")
        print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        print("")
        print("")
        print("")
        print("")
        print(pyfiglet.figlet_format("Blackjack!"))
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("___________________________________________________")
        #aight bet im doing blackjack!
        dealers_names = ["Vinny", "Elena", "Marcus", "Sophia", "Sal", 
         "Chloe", "Dante", "Natasha", "Leo", "Victoria", 
         "Frankie", "Maya", "Julian", "Camila", "Tony", 
         "Isabella", "Rocco", "Bianca", "Gino", "Sienna", 
        "Nico", "Valerie", "Marco", "Carmen", "Johnny"]

        dealer_name = random.choice(dealers_names)
        #these are the cards names
        print("")
        print("Alright, welcome! I'm " + dealer_name + ", your dealer for today. I'll always be different every time you interact with blackjack! Lets begin!")

        print("")

        while True:
            try:
                user_blackjack_cash = float(input("How much money would you like to bet on this game? You currently have " + str(money) + " dollars right now: "))

                if 1 <= user_blackjack_cash <= money:
                    break

                elif user_blackjack_cash > money:
                    print("You cannot bet more than the amount of money you have.")

                else:
                    print("You cannot bet less than 1 dollar, you have to bet at least 1 dollar(s)")

            except ValueError:
                print("Invalid input. Please enter a number.")

        print(" ")
        cards = ["2 of Hearts", "3 of Hearts", "4 of Hearts", "5 of Hearts", "6 of Hearts", "7 of Hearts", "8 of Hearts", "9 of Hearts", "10 of Hearts", "Jack of Hearts", "Queen of Hearts", "King of Hearts", "Ace of Hearts",
        "2 of Diamonds", "3 of Diamonds", "4 of Diamonds", "5 of Diamonds", "6 of Diamonds", "7 of Diamonds", "8 of Diamonds", "9 of Diamonds", "10 of Diamonds", "Jack of Diamonds", "Queen of Diamonds", "King of Diamonds", "Ace of Diamonds",
        "2 of Clubs", "3 of Clubs", "4 of Clubs", "5 of Clubs", "6 of Clubs", "7 of Clubs", "8 of Clubs", "9 of Clubs", "10 of Clubs", "Jack of Clubs", "Queen of Clubs", "King of Clubs", "Ace of Clubs",
        "2 of Spades", "3 of Spades", "4 of Spades", "5 of Spades", "6 of Spades", "7 of Spades", "8 of Spades", "9 of Spades", "10 of Spades", "Jack of Spades", "Queen of Spades", "King of Spades", "Ace of Spades"]

        #These are the card's values
        card_values = { 
        "2 of Hearts": 2, "3 of Hearts": 3, "4 of Hearts": 4, "5 of Hearts": 5, "6 of Hearts": 6, "7 of Hearts": 7, "8 of Hearts": 8, "9 of Hearts": 9, "10 of Hearts": 10, "Jack of Hearts": 10, "Queen of Hearts": 10, "King of Hearts": 10, "Ace of Hearts": 11,
        "2 of Diamonds": 2, "3 of Diamonds": 3, "4 of Diamonds": 4, "5 of Diamonds": 5, "6 of Diamonds": 6, "7 of Diamonds": 7, "8 of Diamonds": 8, "9 of Diamonds": 9, "10 of Diamonds": 10, "Jack of Diamonds": 10, "Queen of Diamonds": 10, "King of Diamonds": 10, "Ace of Diamonds": 11,
        "2 of Clubs": 2, "3 of Clubs": 3, "4 of Clubs": 4, "5 of Clubs": 5, "6 of Clubs": 6, "7 of Clubs": 7, "8 of Clubs": 8, "9 of Clubs": 9, "10 of Clubs": 10, "Jack of Clubs": 10, "Queen of Clubs": 10, "King of Clubs": 10, "Ace of Clubs": 11,
        "2 of Spades": 2, "3 of Spades": 3, "4 of Spades": 4, "5 of Spades": 5, "6 of Spades": 6, "7 of Spades": 7, "8 of Spades": 8, "9 of Spades": 9, "10 of Spades": 10, "Jack of Spades": 10, "Queen of Spades": 10, "King of Spades": 10, "Ace of Spades": 11}

        card1, card2 = random.sample(cards, 2)

        dealer1, dealer2 = random.sample(cards, 2)

        dealer_visible_points = card_values[dealer1]

        dealer_complete_points = card_values[dealer1] + card_values[dealer2]

        print("Drumroll please! Your first card is " + card1 + " and your second is " + card2 + ". Obviously you cannot see the dealers cards though! Ha, Ha. Just kidding, in Blackjack, you are entitled to see one of the dealer's cards. One of their cards are the " + dealer1 + " which is worth " + str(dealer_visible_points) + " points.")
        print("")
        input("Press enter to show how many points you have and progress: ")
        cards = list(card_values.keys())
        total_value_of_dealer_cards = card_values[dealer1] + card_values[dealer2]
        total_value_of_cards_without_hit = card_values[card1] + card_values[card2]


        print(" ")
        print("Both of your cards values are " + str(total_value_of_cards_without_hit) + " points. Remember, your goal is to get as close to 21 while not going over 21")
        print("")
        #Please dont toich this little bro, i know ur checking my code for AI, only AI here is Anish Intelligence little boiii
        
        hit_card = ""

        while True:
            blackjack_input = input("What do you want to do? You can either hit or stand... ")
            if blackjack_input == "hit":
                hit_card = random.sample(cards, 1)
                hit_card_value = card_values[hit_card[0]]
                print("")
                print("By hitting, you gain 1 extra card and gain extra points.")
                print("Your new card is " + str(hit_card) + ". It is worth " + str(hit_card_value) + " points. ") 
                print("")
                break

            if blackjack_input == "stand":
                print("Alright, standing until the dealer's turn!")
                print(" ")
                break
        print("")
        print("Dealers turn!")
        print("‾‾‾‾‾‾‾‾‾‾‾‾‾")
        print(" ")
        print("Dealer: now, I must reveal my cards. I had the " + dealer1 + " and the " + dealer2 + ". Together, they were worth " +  str(total_value_of_dealer_cards) + " points.")
        print(" ")
        print("Now, you must reveal your cards. You had the " + str(card1) + " and the " + str(card2)+ ".")
        if hit_card == "":
            print(" ")
            print("Since you didn't choose to hit, your score will be counted with just your beggining points. You had " + str(total_value_of_cards_without_hit) + " points.")
            player_total = total_value_of_cards_without_hit

        else:
            print(" ")
            print("Since you did choose to hit, your score will account for the extra card which you gained.")
            player_total = total_value_of_cards_without_hit + hit_card_value
            print("You had " + str(player_total) + " points.")
            print("")

        if player_total > 21:
            print("Aww man you lost. You went over 21! Better luck next time! Come back again.")
            money -= user_blackjack_cash
            print("")
        elif total_value_of_dealer_cards > 21:
            print("Congrats, you won! The dealer went over 21. The money you have bet will land in your account. Great job!")
            money += user_blackjack_cash
            print("")
        elif player_total > total_value_of_dealer_cards:
            print("Congrats, you won! You were closer to 21 than the dealer. The money you have bet will land in your account. Great job!")
            money += user_blackjack_cash
            print("")
        elif player_total < total_value_of_dealer_cards:
            print("Sorry, you lost. The dealer was closer to 21 than you were. The exact amount of money you bet will be drained from your account. Better luck next time!")
            money -= user_blackjack_cash
            print("")
        else:
            print("Wow you got exactly the same amount of points as the dealer! A tie occurs and you don't lose or gain any money!")
            print("")
            
        print("You now have " + str(money) + " dollars.")
        print("")
        input("Press enter to go back home. Hope you return!")


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    elif game_choice == "roulette":
        print("Starting roulette...")
        print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        print(" ")
        print("")
        print("")
        print("")
        print("")
        print(pyfiglet.figlet_format("Roulette!"))
        print("")
        print("")
        print("Roulette Table")
        print("0 – 28 – 9 – 26 – 30 – 11 – 7 – 20 – 32 – 17 – 5 – 22 – 34 – 15 – 3 – 24 – 36 – 13 – 1 – 00 – 27 – 10 – 25 – 29 – 12 – 8 – 19 – 31 – 18 – 6 – 21 – 33 – 16 – 4 – 23 – 35 – 14 – 2")
        print(" ")
        user_roulette = input("Choose a color, red or black: ").lower()
        while user_roulette != "red" and user_roulette != "black":
            print("Invalid choice. Please choose either red or black.")
            user_roulette = input("Choose a color, red or black: ").lower()
        user_roulette_cash = float(input("How much money would you like to bet? You currently have " + str(money) + " dollars right now: "))
        while user_roulette_cash > money:
            print("You cannot bet more than the amount of money you have.")
            user_roulette_cash = float(input("How much money would you like to bet? "))
        while user_roulette_cash < 1:
            print("You cannot bet less than 1 dollar, you have to bet at least 1 dollar(s)")
            user_roulette_cash = float(input("How much money would you like to bet? "))


        print("Rolling the wheel, Usually takes around 10-15 seconds")
        print("")
        if user_roulette == "red" or user_roulette == "black":
            show_spinner(12)
        roulette_result = random.choice([1, 2])

        #btw red is 1 and black is 2
        if roulette_result == 1 and user_roulette == "red":
            print("Congrats you won, you get the amount of money you bet, exactly into your account")
            money += user_roulette_cash
            print("You now have " + str(money) + " dollars." ) 

        elif roulette_result == 1 and user_roulette == "black":
            print("Aww man you lost, don't give up champ, we at Anish's Casino believe in you. As NickEh30 states, never give up never what?")
            money -= user_roulette_cash
            print("You now have " + str(money) + " dollars." ) 

        elif roulette_result == 2 and user_roulette == "black":
            print("Congrats you won, you get the amount of money you bet, exactly into your account. Enjoy your free drinks, as NickEh30 says, never give up never what?")
            money += user_roulette_cash
            print("You now have " + str(money) + " dollars." ) 

        elif roulette_result == 2 and user_roulette == "red":
            print("Aww man you lost, don't give up champ, we at Anish's Casino believe in you. As NickEh30 states, never give up never what?")
            money -= user_roulette_cash
            print("You now have " + str(money) + " dollars." ) 
        
        input("Press enter to go back home: ")

else:
    print("Type the name of the game exactly as it is shown!")

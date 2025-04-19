import random #Loads Python’s random tools so you can use them

def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"] #List of valid choices
    user_choice = input("Enter rock, paper, or scissors: ").lower() #Ask user for input

    if user_choice not in choices: #Validate user input
        print("Invalid choice! Please enter rock, paper, or scissors.")
        return

    computer_choice = random.choice(choices) #It’s a function from Python’s random module that lets you pick a random item from a list (or any sequence like a string or tuple).

    print(f"\nYou chose:",user_choice) #Show choices
    print(f"Computer chose:",computer_choice)

    if user_choice == computer_choice: #Decide outcome
        print("It's a draw!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("You win! ")
    else:
        print("You lose! ")

# Calling the function Start the game
rock_paper_scissors()

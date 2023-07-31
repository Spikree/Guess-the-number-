import random
from art import logo

EASY = 10
HARD = 5

def check_answers(guess, answer, turns):
    if guess > answer:
        print("Too high")
        return turns - 1
    elif guess < answer:
        print("Too low")
        return turns - 1 
    else:
        print(f"You got the right answer, it was {answer}")

def set_difficulty():
    level = input("choose a difficulty, type 'easy' for easy and 'hard' for hard :").lower()
    if level == "easy":
        return EASY
    elif level == "hard":
        return HARD
    
def final_game():
    print(logo)
    print("Welcome to the number guessing game")
    print("I'm thinking of a number between 1 to 100")
    answer = random.randint(1,100)

    turns = set_difficulty()
    guess = 0
    
    while guess != answer:
        print(f"you have {turns} attempts remaining")
        guess = int(input("Make a guess:"))
        
        turns = check_answers(guess = guess, answer = answer, turns = turns)
        if turns == 0 :
            print("You've run out of lives, you loose")
            return
        elif guess != answer:
            print("Guess again:")


final_game()
import random
import art

easyTurns = 10
hardTurns = 5

def answerCheck(userGuess, actualGuess, turns):
    if userGuess > actualGuess:
        print("Too High!")
        return turns - 1
    elif userGuess < actualGuess:
        print("Too Low!")
        return turns - 1
    elif userGuess == actualGuess:
        print(f"Correct! The Number Was {actualGuess}.")
        return turns          # Added

def difficultyCheck():
    level = input("Choose Your Difficulty (Easy Or Hard):  ").lower()
    if level == "easy":
        return easyTurns
    elif level == "hard":
        return hardTurns

def gameStart():
    print(art.logo)
    print("Welcome To The Number Guessing Game!")
    print("I am Thinking Of A Number Between 1 and 100.")
    answer = random.randint(1, 100)
    # print(f"The Correct Answer Is {answer}")

    turns = difficultyCheck()
    guess = 0
    while guess != answer:
        print(f"You Have {turns} Attempts Remaining.")
        guess = int(input("Make A Guess: "))
        turns = answerCheck(guess, answer, turns)   # Fixed function name
        if turns == 0:
            print("You Are Out Of Guesses. YOU LOSE. :(")
            return
        elif guess != answer:
            print("Guess again.")

gameStart()
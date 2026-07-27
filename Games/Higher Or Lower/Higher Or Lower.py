from art import logo, vs
from game_data import info
import random

def data(account):
    accountName = account["name"]
    accountDes = account["description"]
    accountCountry = account["country"]
    return {f"Account: {accountName}, {accountDes}, From {accountCountry}."}

def answerCheck(userGuess, aFollowers, bFollowers):
    if aFollowers > bFollowers:
        return userGuess == "a"
    else:
        return userGuess == "b"

print(logo)
score = 0
gameContinue = True

accountB = random.choice(info)

while gameContinue:
    accountA = accountB
    accountB = random.choice(info)

    if accountA == accountB:
        accountB = random.choice(info)

    print(f"Compare A: {data(accountA)}")
    print(vs)
    print(f"Compare B: {data(accountB)}")

    guess = input("Who Has More Followers (A or B): ").lower()
    print("\n" * 20)
    print(logo)

    aFollowerCount = accountA["follower_count"]
    bFollowerCount = accountB["follower_count"]

    correct = answerCheck(guess, aFollowerCount, bFollowerCount)

    if correct:
        score += 1
        print(f"You Are Right! Current Score: {score}")
    else:
        print(f"Incorrect. Final Score: {score}")
        gameContinue = False


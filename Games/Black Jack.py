import random
import art

print(art.logo)

def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate(cards):
    """Calculates the score of a hand."""

    # Blackjack (Ace + 10-value card)
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    # Convert Ace from 11 to 1 if score exceeds 21
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(userScore, computerScore):
    """Compares scores and returns the game result."""

    if userScore == computerScore:
        return "🤝 Draw!"

    elif computerScore == 0:
        return "😞 You Lose! Opponent has Blackjack."

    elif userScore == 0:
        return "🎉 You Win! You have Blackjack."

    elif userScore > 21:
        return "💥 You went over 21. You Lose!"

    elif computerScore > 21:
        return "🎉 Opponent went over 21. You Win!"

    elif userScore > computerScore:
        return "🎉 You Win!"

    else:
        return "😞 You Lose!"

# GAME START

user_cards = []
computer_cards = []
isGameOver = False

for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

while not isGameOver:

    userScore = calculate(user_cards)
    compScore = calculate(computer_cards)

    print(f"\nYour cards: {user_cards}, current score: {userScore}")
    print(f"Computer's first card: {computer_cards[0]}")

    if userScore == 0 or compScore == 0 or userScore > 21:
        isGameOver = True
    else:
        userDeal = input("Type 'y' to get another card, 'n' to pass: ").lower()

        if userDeal == "y":
            user_cards.append(deal_card())
        else:
            isGameOver = True

compScore = calculate(computer_cards)

while compScore != 0 and compScore < 17:
    computer_cards.append(deal_card())
    compScore = calculate(computer_cards)

userScore = calculate(user_cards)
compScore = calculate(computer_cards)

print("\n----------- FINAL RESULT -----------")
print(f"Your final hand: {user_cards}, final score: {userScore}")
print(f"Computer's final hand: {computer_cards}, final score: {compScore}")

print(compare(userScore, compScore))

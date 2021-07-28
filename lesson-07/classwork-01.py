import random


def get_card_sum(user_cards):
    card_value = {
        "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 2, "D": 3, "K": 4, "A": 11
    }
    card_sum = 0
    for card in user_cards:
        key = card.split("-")[-1]
        card_sum += card_value[key]
        return card_sum


def get_card(user_cards):
    card_suit_list = ["N", "D", "C", "S"]
    card_list = ['6', '7', '8', '9', '10', 'J', 'D', 'K', 'A']
    current = None
    while True:
        index = random.randint(0, len(card_suit_list) - 1)
        card_suit = card_suit_list[index]
        index = random.randint(0, len(card_list) - 1)
        card = card_list[index]
        current = (f"{card_suit}-{card}")
        if current not in user_cards:
            return current


user_cards = []
while True:
    choise = input('Get new card?[y/n]: ')
    if choise == "y":
        current = get_card(user_cards)
        user_cards.append(current)
        print(user_cards)
        card_sum = get_card_sum(user_cards)
        print(card_sum)
        if card_sum > 21:
            print("Game over")
            break
        if card_sum == 21:
            print("You win")
            break
    else:
        card_sum = get_card_sum(user_cards)
        print("You current sum:", card_sum)
        break

import random
from replit import clear
from art import logo, vs
from game_data import data


def format_data(account):
    """Takes the account data and returns printable format"""
    account_name = account.get('name')
    account_descr = account.get('description')
    account_country = account.get('country')
    return f"{account_name}, a {account_descr}, from {account_country}"


def check_answer(guess, a_account, b_account):
    """Checks followers against user's guess
     and returns True if they got it right.
     Or False if they got it wrong."""
    if a_account.get('follower_count') > b_account.get('follower_count'):
        return guess == "a"
    else:
        return guess == "b"


def game():
    print(logo)
    score = 0
    game_should_continue = True
    account_b = random.choice(data)

    while game_should_continue:
        account_a = account_b
        account_b = random.choice(data)
        if account_a == account_b:
            account_b = random.choice(data)
        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Against B: {format_data(account_b)}.")
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        is_correct = check_answer(guess, account_a, account_b)
        clear()
        print(logo)
        if is_correct:
            score += 1
            print(f'You right! Current score: {score}.')
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score {score}")


game()
